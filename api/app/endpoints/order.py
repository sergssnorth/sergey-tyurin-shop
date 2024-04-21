from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Order, Employee, OrderStatus
from app.db import get_session

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, and_, join, or_, func
from typing import List
from math import ceil
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

router = APIRouter()

class OrderResponseModel(BaseModel):
    id: int
    user_id: Optional[int]
    name: str
    sname: str
    lname: str
    phone: str
    email: str
    region: str
    city: str
    postal_code: str
    employee_id: Optional[int]
    order_status_id: Optional[int]
    created_at: datetime
    updated_at: Optional[datetime]
    employee_name: Optional[str]
    employee_sname: Optional[str]
    order_status_name: Optional[str]

class OrdersResponseModel(BaseModel):
    total_count: int
    total_pages: int
    orders: List[OrderResponseModel]


@router.get("/orders", response_model=OrdersResponseModel)
async def get_orders(offset: int = Query(0, ge=0),
                     limit: int = Query(50, gt=0),
                     search: str = Query(None),

                     user_id: int = Query(None),
                     order_status_id: int = Query(None),

                     sort_by: str = Query(None, description="Sort by 'name' or 'id'."),
                     order: str = Query("desc", description="Sort order: 'asc' or 'desc'."),

                     session: AsyncSession = Depends(get_session)):

    query = (
        select(Order, Employee, OrderStatus)
        .join(Order.employee, isouter=True)
        .join(Order.order_status, isouter=True)
    )

    if search:
        query = query.filter(or_(
            Order.id.ilike(f"%{search}%")
        ))    

    if user_id:
        query = query.filter(Order.user_id == user_id)

    if order_status_id:
        query = query.filter(Order.order_status_id == order_status_id)

    if sort_by and order:
        if sort_by == "id":
            query = query.order_by(Order.id.desc() if order == "desc" else Order.id.asc())
    else:
        #Сортировака по умолчанию
        query = query.order_by(Order.id.desc() if order == "desc" else Order.id.asc())


    total_count_query = select(func.count()).select_from(Order)
    total_count_result = await session.execute(total_count_query)
    total_count = total_count_result.scalar()
    total_pages = ceil(total_count / limit)

    query = query.offset(offset).limit(limit)
    orders_elements = await session.execute(query)

    print("orders_elements")
    print(orders_elements)
    print("orders_elements")

    response_data = []
    for order, employee, orderStatus in orders_elements:
        employee_name = employee.name if employee else None
        employee_sname = employee.sname if employee else None
        order_status_name = orderStatus.name if orderStatus else None

        response_data.append(
            OrderResponseModel(
                id=order.id,
                user_id=order.user_id,
                name=order.name,
                sname=order.sname,
                lname=order.lname,
                phone=order.phone,
                email=order.email,
                region=order.region,
                city=order.city,
                postal_code=order.postal_code,
                employee_id=order.employee_id,
                order_status_id=order.order_status_id,
                created_at=order.created_at,
                updated_at=order.updated_at,
                employee_name=employee_name,
                employee_sname=employee_sname,
                order_status_name=order_status_name,
            )
        )

    return OrdersResponseModel(
        total_count=total_count,
        total_pages=total_pages,
        orders=response_data
    ) 


@router.post("/order")
async def add_order(order: Order, session: AsyncSession = Depends(get_session)):
    new_order = Order(
                id=order.id,
                user_id=order.user_id,
                name=order.name,
                sname=order.sname,
                lname=order.lname,
                phone=order.phone,
                email=order.email,
                region=order.region,
                city=order.city,
                postal_code=order.postal_code,
                employee_id=order.employee_id,
                order_status_id=order.order_status_id,
                created_at=datetime.now())
    session.add(new_order)
    await session.commit()
    await session.refresh(new_order)
    return new_order

@router.put("/order/{order_id}")
async def update_order(order_id: int, updated_order: Order, session: AsyncSession = Depends(get_session)):
    existing_order = await session.get(Order, order_id)
    if existing_order is None:
        raise HTTPException(status_code=404, detail="Заказ не найден")
    existing_order.name = updated_order.name
    existing_order.sname = updated_order.sname
    existing_order.lname = updated_order.lname
    existing_order.phone = updated_order.phone
    existing_order.email = updated_order.email
    existing_order.city = updated_order.city
    existing_order.postal_code = updated_order.postal_code
    existing_order.employee_id = updated_order.employee_id
    existing_order.order_status_id = updated_order.order_status_id
    existing_order.updated_at = updated_order.datetime.now()

    await session.commit()
    await session.refresh(existing_order)
    return existing_order

@router.delete("/order/{order_id}")
async def delete_order(order_id: int, session: AsyncSession = Depends(get_session)):
    order = await session.get(Order, order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Заказа не найден")
    try:
        await session.delete(order)
        await session.commit()
        return {"message": "Заказ успешно удален"}
    except Exception as e:
        print(f"Ошибка при удалении Заказа: {e}")
        await session.rollback()  # Откат изменений в случае ошибки