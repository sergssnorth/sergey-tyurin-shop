
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import OrderStatus
from app.db import get_session

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, func, or_
from typing import List
from math import ceil
from pydantic import BaseModel


router = APIRouter()

class OrderStatusesResponseModel(BaseModel):
    total_count: int
    total_pages: int
    order_statuses: List[OrderStatus]


@router.get("/order-statuses", response_model=OrderStatusesResponseModel)
async def get_order_statuses(offset: int = Query(0, ge=0),
                            limit: int = Query(50, gt=0),
                            search: str = Query(None),
                            session: AsyncSession = Depends(get_session)):
    
    query = select(OrderStatus)

    if search:
        query = query.where(OrderStatus.name.ilike(f"%{search}%"))

    total_count_query = select(func.count()).select_from(query)
    total_count_result = await session.execute(total_count_query)
    total_count = total_count_result.scalar()
    total_pages = ceil(total_count / limit)

    query = query.offset(offset).limit(limit)
    colors_result = await session.execute(query)
    colors = colors_result.scalars().all()
    

    result = await session.execute(select(OrderStatus))
    order_statuses = result.scalars().all()

    return OrderStatusesResponseModel(
        total_count=total_count,
        total_pages=total_pages,
        order_statuses=[
            OrderStatus(
                id=order_status.id,
                name=order_status.name,
                slug=order_status.slug,
            ) for order_status in order_statuses
        ]
    )

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