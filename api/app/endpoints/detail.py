from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Detail
from app.db import get_session


from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, func, or_
from typing import List
from math import ceil
from pydantic import BaseModel


router = APIRouter()

class DetailResponseModel(BaseModel):
    total_count: int
    total_pages: int
    details: List[Detail]

@router.get("/details", response_model=DetailResponseModel)
async def get_details(offset: int = Query(0, ge=0),
                     limit: int = Query(50, gt=0),
                     search: str = Query(None),

                     sort_by: str = Query(None, description="Sort by 'name' or 'id'."),
                     order: str = Query("desc", description="Sort order: 'asc' or 'desc'."),

                     session: AsyncSession = Depends(get_session)):
    
    query = select(Detail)

    if search:
        query = query.where(Detail.name.ilike(f"%{search}%"))

    if sort_by and order:
        if sort_by == "name":
            query = query.order_by(Detail.name.desc() if order == "desc" else Detail.name.asc())
        elif sort_by == "id":
            query = query.order_by(Detail.id.desc() if order == "desc" else Detail.id.asc())
    else:
        #Сортировака по умолчанию
        query = query.order_by(Detail.id.desc() if order == "desc" else Detail.id.asc())

    total_count_query = select(func.count()).select_from(query)
    total_count_result = await session.execute(total_count_query)
    total_count = total_count_result.scalar()
    total_pages = ceil(total_count / limit)

    query = query.offset(offset).limit(limit)
    details_result = await session.execute(query)
    details = details_result.scalars().all()

    return DetailResponseModel(
        total_count=total_count,
        total_pages=total_pages,
        details=[
            Detail(
                id=detail.id,
                name=detail.name,
                description=detail.description,
            ) for detail in details]
    )


@router.post("/detail")
async def add_detail(detail: Detail, session: AsyncSession = Depends(get_session)):
    new_detail = Detail(name=detail.name, description=detail.description)
    session.add(new_detail)
    await session.commit()
    await session.refresh(new_detail)
    return new_detail

@router.put("/detail/{detail_id}")
async def update_Detail(detail_id: int, updated_detail: Detail, session: AsyncSession = Depends(get_session)):
    existing_detail = await session.get(Detail, detail_id)
    if existing_detail is None:
        raise HTTPException(status_code=404, detail="Цвет не найден")
    existing_detail.name = updated_detail.name
    existing_detail.description = updated_detail.description
    await session.commit()
    await session.refresh(existing_detail)
    return existing_detail

@router.delete("/detail/{detail_id}")
async def delete_Detail(detail_id: int, session: AsyncSession = Depends(get_session)):
    existing_detail = await session.get(Detail, detail_id)
    if existing_detail is None:
        raise HTTPException(status_code=404, detail="Цвет не найден")
    try:
        await session.delete(existing_detail)
        await session.commit()
        return {"message": "Цвет успешно удален"}
    except Exception as e:
        print(f"Ошибка при удалении Цвета: {e}")
        await session.rollback()  # Откат изменений в случае ошибки