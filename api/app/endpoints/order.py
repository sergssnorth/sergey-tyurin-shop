from typing import List, Optional, Union
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Order, OrderStatus
from app.db import get_session
from sqlmodel import select, and_, join
from pydantic import BaseModel 

router = APIRouter()

class ModelResponse(BaseModel):
    id: int
    name: str
    slug: str
    client_id: int
    order_status : str
    order_status_slug  : str


@router.get("/orders")
async def get_orders(
    client_id: Optional[int] = None,
    session: AsyncSession = Depends(get_session)
    ):

    query = select(Order, OrderStatus).join(OrderStatus)

    if client_id is not None:
        query = query.filter(Order.client_id == client_id)

    orders = await session.execute(query)
    orders_list = list(orders)

    result_list = []

    for order, order_status in orders_list:
        result_list.append(
            ModelResponse(
                id=order.id,
                name=order.name,
                slug=order.slug,
                client_id=order.client_id,
                order_status=order_status.name,
                order_status_slug=order_status.slug,
            )
        )

    return result_list


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