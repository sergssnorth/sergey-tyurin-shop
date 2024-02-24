
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import BigCategory
from app.db import get_session

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, func
from typing import List
from math import ceil
from pydantic import BaseModel

router = APIRouter()

class BigCategoryResponseModel(BaseModel):
    total_count: int
    total_pages: int
    big_categories: List[BigCategory]


@router.get("/big_categories", response_model=BigCategoryResponseModel)
async def get_big_categories(offset: int = Query(0, ge=0),
                            limit: int = Query(50, gt=0),
                            search: str = Query(None),
                            session: AsyncSession = Depends(get_session)):
    base_query = select(BigCategory)

    if search:
        base_query = base_query.where(BigCategory.name.ilike(f"%{search}%"))

    base_query = base_query.offset(offset).limit(limit)

    total_count_query = select(func.count(BigCategory.id)).where(base_query)
    total_count_result = await session.execute(total_count_query)
    total_count = total_count_result.scalar()

    total_pages = ceil(total_count / limit)

    big_category_result = await session.execute(base_query)
    big_category = big_category_result.scalars().all()

    response_model = BigCategoryResponseModel(
        total_count=total_count,
        total_pages=total_pages,
        big_categories=big_category
    )

    return response_model

   
@router.post("/big_category")
async def add_big_categories(big_category: BigCategory, session: AsyncSession = Depends(get_session)):
    new_big_category = BigCategory(name=big_category.name, slug=big_category.slug)
    session.add(new_big_category)
    await session.commit()
    await session.refresh(new_big_category)
    return new_big_category

@router.put("/big_category/{big_category_id}")
async def update_big_category(big_category_id: int, updated_big_category: BigCategory, session: AsyncSession = Depends(get_session)):
    existing_big_category = await session.get(BigCategory, big_category_id)
    if existing_big_category is None:
        raise HTTPException(status_code=404, detail="Раздел не найден")
    existing_big_category.name = updated_big_category.name
    existing_big_category.slug = updated_big_category.slug
    await session.commit()
    await session.refresh(existing_big_category)
    return existing_big_category

@router.delete("/big_category/{big_category_id}")
async def delete_big_category(big_category_id: int, session: AsyncSession = Depends(get_session)):
    big_category = await session.get(BigCategory, big_category_id)
    if big_category is None:
        raise HTTPException(status_code=404, detail="Раздел не найден")
    try:
        await session.delete(big_category)
        await session.commit()
        return {"message": "Раздел успешно удален"}
    except Exception as e:
        print(f"Ошибка при удалении Раздела: {e}")
        await session.rollback()  # Откат изменений в случае ошибки