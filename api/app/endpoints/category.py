from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Category
from app.db import get_session
from sqlmodel import select
from typing import List, Optional

router = APIRouter()


@router.get("/categories", response_model=List[Category])
async def get_categories(big_category_id: Optional[int] = None, session: AsyncSession = Depends(get_session)):
    query = select(Category)

    # Если задан big_category_id, добавляем условие фильтрации
    if big_category_id is not None:
        query = query.filter(Category.big_category_id == big_category_id)

    result = await session.execute(query)
    categories = result.scalars().all()

    return [
        Category(
            id=category.id,
            name=category.name,
            slug=category.slug,
            big_category_id=category.big_category_id
        ) for category in categories
    ]

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
