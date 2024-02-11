from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import OrderStatus
from app.db import get_session
from sqlmodel import select


router = APIRouter()


@router.get("/order-statuses", response_model=list[OrderStatus])
async def get_order_statuses(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(OrderStatus))
    order_statuses = result.scalars().all()
    return [OrderStatus(id=order_status.id, name=order_status.name, slug=order_status.slug) for order_status in order_statuses]

@router.post("/order-status")
async def add_order_status(order_status: OrderStatus, session: AsyncSession = Depends(get_session)):
    new_order_status = OrderStatus(name=order_status.name, slug=order_status.slug)
    session.add(new_order_status)
    await session.commit()
    await session.refresh(new_order_status)
    return new_order_status

@router.put("/order-status/{order_status_id}")
async def update_order_status(order_status_id: int, updated_order_status: OrderStatus, session: AsyncSession = Depends(get_session)):
    existing_order_status = await session.get(OrderStatus, order_status_id)
    if existing_order_status is None:
        raise HTTPException(status_code=404, detail="Статус заказа не найден")
    existing_order_status.name = updated_order_status.name
    existing_order_status.slug = updated_order_status.slug
    await session.commit()
    await session.refresh(existing_order_status)
    return existing_order_status

@router.delete("/order-status/{order_status_id}")
async def delete_big_category(order_status_id: int, session: AsyncSession = Depends(get_session)):
    order_status = await session.get(OrderStatus, order_status_id)
    if order_status is None:
        raise HTTPException(status_code=404, detail="Статус заказа не найден")
    try:
        await session.delete(order_status)
        await session.commit()
        return {"message": "Раздел успешно удален"}
    except Exception as e:
        print(f"Ошибка при удалении Раздела: {e}")
        await session.rollback()  # Откат изменений в случае ошибки