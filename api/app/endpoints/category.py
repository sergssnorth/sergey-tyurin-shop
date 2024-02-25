from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Category
from app.db import get_session

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, func, or_
from typing import List,  Optional
from math import ceil
from pydantic import BaseModel

router = APIRouter()

class CategoryResponseModel(BaseModel):
    total_count: int
    total_pages: int
    categories: List[Category]


@router.get("/categories", response_model=CategoryResponseModel)
async def get_categories(offset: int = Query(0, ge=0),
                        limit: int = Query(50, gt=0),
                        search: str = Query(None),
                        big_category_id: int = Query(None), 
                        session: AsyncSession = Depends(get_session)):
    
    query = select(Category)

    if big_category_id:
        query = query.filter(Category.big_category_id == big_category_id)

    if search:
        query = query.filter(or_(
            Category.name.ilike(f"%{search}%")
        ))

    total_count_query = select(func.count()).select_from(query)
    total_count_result = await session.execute(total_count_query)
    total_count = total_count_result.scalar()
    total_pages = ceil(total_count / limit)


    query = query.offset(offset).limit(limit)
    categories_result = await session.execute(query)
    categories = categories_result .scalars().all()

    return CategoryResponseModel(
        total_count=total_count,
        total_pages=total_pages,
        categories=[
            Category(
                id=category.id,
                name=category.name,
                slug=category.slug,
                big_category_id=category.big_category_id
            ) for category in categories
        ]
    )


@router.post("/category")
async def add_category(category: Category, session: AsyncSession = Depends(get_session)):
    new_category = Category(name=category.name, slug=category.slug, big_category_id=category.big_category_id)
    session.add(new_category)
    await session.commit()
    await session.refresh(new_category)
    return new_category


@router.put("/category/{category_id}")
async def update_category(category_id: int, updated_category: Category, session: AsyncSession = Depends(get_session)):
    existing_category = await session.get(Category, category_id)
    if existing_category is None:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    existing_category.name = updated_category.name
    existing_category.slug = updated_category.slug
    existing_category.big_category_id = updated_category.big_category_id
    await session.commit()
    await session.refresh(existing_category)
    return existing_category

@router.delete("/category/{category_id}")
async def delete_category(category_id: int, session: AsyncSession = Depends(get_session)):
    existing_category = await session.get(Category, category_id)
    if existing_category is None:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    try:
        await session.delete(existing_category)
        await session.commit()
        return {"message": "Категория успешно удалена"}
    except Exception as e:
        print(f"Ошибка при удалении категории: {e}")
        await session.rollback()  # Откат изменений в случае ошибки
