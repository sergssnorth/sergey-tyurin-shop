from fastapi import APIRouter, Depends, HTTPException
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

@router.put("/big_category/{big_category_id}")
async def update_big_category(
    big_category_id: int, updated_big_category: BigCategory, session: AsyncSession = Depends(get_session)
):
    # Поиск категории по идентификатору
    existing_big_category = await session.get(BigCategory, big_category_id)

    # Если категория не найдена, вернуть 404 Not Found
    if existing_big_category is None:
        raise HTTPException(status_code=404, detail="Категория не найдена")

    # Обновление данных
    existing_big_category.name = updated_big_category.name
    existing_big_category.slug = updated_big_category.slug

    # Сохранение изменений
    await session.commit()
    await session.refresh(existing_big_category)

    return existing_big_category

@router.delete("/big_category/{big_category_id}")
async def delete_big_category(big_category_id: int, session: AsyncSession = Depends(get_session)):
    # Поиск категории по идентификатору
    big_category = await session.get(BigCategory, big_category_id)

    # Если категория не найдена, вернуть 404 Not Found
    if big_category is None:
        raise HTTPException(status_code=404, detail="Категория не найдена")

    # Удаление категории
    session.delete(big_category)
    await session.commit()

    return {"message": "Категория успешно удалена"}