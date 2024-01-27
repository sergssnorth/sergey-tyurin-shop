from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Category
from app.db import get_session
from sqlmodel import select


router = APIRouter()


@router.get("/categories", response_model=list[Category])
async def get_categories(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Category))
    categories = result.scalars().all()
    return [Category(id=category.id, name=category.name, slug=category.slug, big_category_id=category.big_category_id) for category in categories]

@router.post("/category")
async def add_category(category: Category, session: AsyncSession = Depends(get_session)):
    new_category = Category(name=category.name, slug=category.slug, big_category_id=category.big_category_id)
    session.add(new_category)
    await session.commit()
    await session.refresh(new_category)
    return new_category