
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import BigCategory
from app.db import get_session

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, func
from typing import List
from math import ceil
from pydantic import BaseModel

router = APIRouter()

class BigCategoriesResponseModel(BaseModel):
    total_count: int
    total_pages: int
    big_categories: List[BigCategory]


@router.get("/big-categories", response_model=BigCategoriesResponseModel)
async def get_big_categories(offset: int = Query(0, ge=0),
                            limit: int = Query(50, gt=0),
                            search: str = Query(None),
                            sort_by: str = Query(None, description="Sort by 'name' or 'id'."),
                            order: str = Query("desc", description="Sort order: 'asc' or 'desc'."),
                            session: AsyncSession = Depends(get_session)):
    query = select(BigCategory)

    if search:
        query = query.where(BigCategory.name.ilike(f"%{search}%"))

    if sort_by and order:
        if sort_by == "name":
            query = query.order_by(BigCategory.name.desc() if order == "desc" else BigCategory.name.asc())
        elif sort_by == "id":
            query = query.order_by(BigCategory.id.desc() if order == "desc" else BigCategory.id.asc())
    else:
        #Сортировака по умолчанию
        query = query.order_by(BigCategory.id.desc() if order == "desc" else BigCategory.id.asc())


    total_count_query = select(func.count()).select_from(query)
    total_count_result = await session.execute(total_count_query)
    total_count = total_count_result.scalar()
    total_pages = ceil(total_count / limit)


    query = query.offset(offset).limit(limit)
    big_category_result = await session.execute(query)
    big_category = big_category_result.scalars().all()

    response_model = BigCategoriesResponseModel(
        total_count=total_count,
        total_pages=total_pages,
        big_categories=big_category
    )

    return response_model

   
@router.post("/big-category")
async def add_big_categories(big_category: BigCategory, session: AsyncSession = Depends(get_session)):
    new_big_category = BigCategory(name=big_category.name, slug=big_category.slug)
    session.add(new_big_category)
    await session.commit()
    await session.refresh(new_big_category)
    return new_big_category

@router.put("/big-category/{big_category_id}")
async def update_big_category(big_category_id: int, updated_big_category: BigCategory, session: AsyncSession = Depends(get_session)):
    existing_big_category = await session.get(BigCategory, big_category_id)
    if existing_big_category is None:
        raise HTTPException(status_code=404, detail="Раздел не найден")
    existing_big_category.name = updated_big_category.name
    existing_big_category.slug = updated_big_category.slug
    await session.commit()
    await session.refresh(existing_big_category)
    return existing_big_category

@router.delete("/big-category/{big_category_id}")
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