from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Order, OrderStatus
from app.db import get_session

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, and_, join, or_, func
from typing import List
from math import ceil
from pydantic import BaseModel


router = APIRouter()

class OrderResponseModel(BaseModel):
    id: int
    name: str
    slug: str
    client_id: int
    order_status: str
    order_status_slug: str

class OrdersResponseModel(BaseModel):
    total_count: int
    total_pages: int
    orders: List[OrderResponseModel]


@router.get("/orders", response_model=OrdersResponseModel)
async def get_orders(offset: int = Query(0, ge=0),
                     limit: int = Query(50, gt=0),
                     search: str = Query(None),

                     client_id: int = Query(None),
                     order_status_id: int = Query(None),

                     sort_by: str = Query(None, description="Sort by 'name' or 'id'."),
                     order: str = Query("desc", description="Sort order: 'asc' or 'desc'."),

                     session: AsyncSession = Depends(get_session)):

    query = select(Order, OrderStatus).join(OrderStatus)

    if search:
        query = query.filter(or_(
            Order.id.ilike(f"%{search}%")
        ))    

    if client_id:
        query = query.filter(Order.client_id == client_id)

    if order_status_id:
        query = query.filter(Order.order_status_id == order_status_id)

    if sort_by and order:
        if sort_by == "name":
            query = query.order_by(Order.name.desc() if order == "desc" else Category.name.asc())
        elif sort_by == "id":
            query = query.order_by(Category.id.desc() if order == "desc" else Category.id.asc())
    else:
        #Сортировака по умолчанию
        query = query.order_by(Category.id.desc() if order == "desc" else Category.id.asc())


    total_count_query = select(func.count()).select_from(query)
    total_count_result = await session.execute(total_count_query)
    total_count = total_count_result.scalar()
    total_pages = ceil(total_count / limit)

    query = query.offset(offset).limit(limit)
    orders_and_order_status = await session.execute(query)

    orders = [OrderResponseModel(
            id=order.id,
            name=order.name,
            slug=order.slug,
            client_id=order.client_id,
            order_status=order_status.name,
            order_status_slug=order_status.slug,
        ) for order, order_status in orders_and_order_status]

    return OrdersResponseModel(
        total_count=total_count,
        total_pages=total_pages,
        orders=orders
    )


@router.post("/order")
async def add_order(order: Order, session: AsyncSession = Depends(get_session)):
    new_order = Order(name=order.name, slug=order.slug, client_id=order.client_id, order_status_id = order.order_status_id)
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
    existing_order.slug = updated_order.slug
    existing_order.client_id = updated_order.client_id
    existing_order.order_status_id = updated_order.order_status_id
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