from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import BigCategory
from app.db import get_session
from sqlmodel import select


router = APIRouter()


@router.get("/big_categories", response_model=list[BigCategory])
async def get_big_categories(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(BigCategory))
    big_categories = result.scalars().all()
    return [BigCategory(id=big_category.id, name=big_category.name, slug=big_category.slug) for big_category in big_categories]

@router.post("/big_category")
async def add_big_categories(big_category: BigCategory, session: AsyncSession = Depends(get_session)):
    new_big_category = BigCategory(name=big_category.name, slug=big_category.slug)
    session.add(new_big_category)
    await session.commit()
    await session.refresh(new_big_category)
    return new_big_category