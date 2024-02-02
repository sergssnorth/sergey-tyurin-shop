from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Color
from app.db import get_session
from sqlmodel import select


router = APIRouter()

@router.get("/colors", response_model=list[Color])
async def get_colors(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Color))
    colors = result.scalars().all()
    return [Color(id=color.id, name=color.name, slug=color.slug) for color in colors]

@router.post("/color")
async def add_color(color: Color, session: AsyncSession = Depends(get_session)):
    new_color = Color(name=color.name, slug=color.slug)
    session.add(new_color)
    await session.commit()
    await session.refresh(new_color)
    return new_color

@router.put("/color/{color_id}")
async def update_color(color_id: int, updated_color: Color, session: AsyncSession = Depends(get_session)):
    existing_color = await session.get(Color, color_id)
    if existing_color is None:
        raise HTTPException(status_code=404, detail="Цвет не найден")
    existing_color.name = updated_color.name
    existing_color.slug = updated_color.slug
    await session.commit()
    await session.refresh(existing_color)
    return existing_color

@router.delete("/color/{color_id}")
async def delete_color(color_id: int, session: AsyncSession = Depends(get_session)):
    existing_color = await session.get(Color, color_id)
    if existing_color is None:
        raise HTTPException(status_code=404, detail="Цвет не найден")
    try:
        await session.delete(existing_color)
        await session.commit()
        return {"message": "Цвет успешно удален"}
    except Exception as e:
        print(f"Ошибка при удалении Цвета: {e}")
        await session.rollback()  # Откат изменений в случае ошибки