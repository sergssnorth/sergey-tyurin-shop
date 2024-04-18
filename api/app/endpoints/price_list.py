from datetime import datetime, timezone
from math import ceil
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import PriceList
from app.db import get_session

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, func, or_
from typing import List
from math import ceil
from pydantic import BaseModel

router = APIRouter()

class PriceListResponseModel(BaseModel):
    total_count: int
    total_pages: int
    price_lists: List[PriceList]

@router.get("/price-lists", response_model=PriceListResponseModel)
async def get_price_lists(offset: int = Query(0, ge=0),
                    limit: int = Query(50, gt=0),
                    search: str = Query(None),
                    
                    sort_by: str = Query(None, description="Sort by 'name' or 'id'."),
                    order: str = Query("desc", description="Sort order: 'asc' or 'desc'."),
                    
                    session: AsyncSession = Depends(get_session)):

    query = select(PriceList)

    if search:
        query = query.filter(or_(
            PriceList.name.ilike(f"%{search}%")
        ))


    if sort_by and order:
        if sort_by == "name":
            query = query.order_by(PriceList.name.desc() if order == "desc" else PriceList.name.asc())
        elif sort_by == "id":
            query = query.order_by(PriceList.id.desc() if order == "desc" else PriceList.id.asc())
    else:
        #Сортировака по умолчанию
        query = query.order_by(PriceList.id.desc() if order == "desc" else PriceList.id.asc())

    total_count_query = select(func.count()).select_from(query)
    total_count_result = await session.execute(total_count_query)
    total_count = total_count_result.scalar()
    total_pages = ceil(total_count / limit)


    query = query.offset(offset).limit(limit)
    price_list_result = await session.execute(query)
    price_lists = price_list_result.scalars().all()

    return PriceListResponseModel(
        total_count=total_count,
        total_pages=total_pages,
        price_lists=[
            PriceList(
                id=price_list.id,
                name=price_list.name,
                created_at=price_list.created_at,
                beginning_at=price_list.beginning_at,
                completion_at=price_list.completion_at
            ) for price_list in price_lists
        ]
    )



@router.post("/price-list")
async def add_price_list(price_list: PriceList, session: AsyncSession = Depends(get_session)):

    beginning_at = datetime.fromisoformat(price_list.beginning_at).replace(tzinfo=None)
    completion_at = datetime.fromisoformat(price_list.completion_at).replace(tzinfo=None)


    new_price_list = PriceList(
        name=price_list.name,
        created_at = datetime.now(),
        beginning_at = beginning_at, 
        completion_at = completion_at, # Убедитесь, что это поле устанавливается автоматически, если необходимо
    )
    session.add(new_price_list)
    await session.commit()
    await session.refresh(new_price_list)
    return new_price_list

@router.put("/price-list/{price_list_id}")
async def update_client(price_list_id: int, updated_price_list: PriceList, session: AsyncSession = Depends(get_session)):
    existing_price_list = await session.get(PriceList, price_list_id)
    if existing_price_list is None:
        raise HTTPException(status_code=404, detail="Клиент не найден")
    
    existing_price_list.name = updated_price_list.name
    existing_price_list.beginning_at = updated_price_list.beginning_at
    existing_price_list.completion_at = updated_price_list.completion_at
    
    await session.commit()
    await session.refresh(existing_price_list)
    return existing_price_list

@router.delete("/price-list/{price_list_id}")
async def delete_price_list(price_list_id: int, session: AsyncSession = Depends(get_session)):
    price_list = await session.get(PriceList, price_list_id)
    if price_list is None:
        raise HTTPException(status_code=404, detail="Клиент не найден")
    try:
        await session.delete(price_list)
        await session.commit()
        return {"message": "Клиент успешно удален"}
    except Exception as e:
        print(f"Ошибка при удалении Заказа: {e}")
        await session.rollback()  # Откат изменений в случае ошибки