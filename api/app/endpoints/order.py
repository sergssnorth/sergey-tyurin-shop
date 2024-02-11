from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Order
from app.db import get_session
from sqlmodel import select


router = APIRouter()


@router.get("/orders", response_model=list[Order])
async def get_orders(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Order))
    orders = result.scalars().all()
    return [Order(id=order.id, name=order.name, slug=order.slug, client_id=order.client_id, order_status_id = order.order_status_id) for order in orders]

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