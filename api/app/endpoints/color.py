from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Color
from app.db import get_session


from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, func, or_
from typing import List
from math import ceil
from pydantic import BaseModel


router = APIRouter()

class ColorsResponseModel(BaseModel):
    total_count: int
    total_pages: int
    colors: List[Color]

@router.get("/colors", response_model=ColorsResponseModel)
async def get_colors(offset: int = Query(0, ge=0),
                     limit: int = Query(50, gt=0),
                     search: str = Query(None),

                     sort_by: str = Query(None, description="Sort by 'name' or 'id'."),
                     order: str = Query("desc", description="Sort order: 'asc' or 'desc'."),

                     session: AsyncSession = Depends(get_session)):
    
    query = select(Color)

    if search:
        query = query.where(Color.name.ilike(f"%{search}%"))

    if sort_by and order:
        if sort_by == "name":
            query = query.order_by(Color.name.desc() if order == "desc" else Color.name.asc())
        elif sort_by == "id":
            query = query.order_by(Color.id.desc() if order == "desc" else Color.id.asc())
    else:
        #Сортировака по умолчанию
        query = query.order_by(Color.id.desc() if order == "desc" else Color.id.asc())

    total_count_query = select(func.count()).select_from(query)
    total_count_result = await session.execute(total_count_query)
    total_count = total_count_result.scalar()
    total_pages = ceil(total_count / limit)

    query = query.offset(offset).limit(limit)
    colors_result = await session.execute(query)
    colors = colors_result.scalars().all()

    return ColorsResponseModel(
        total_count=total_count,
        total_pages=total_pages,
        colors=[
            Color(
                id=color.id,
                name=color.name,
                slug=color.slug,
            ) for color in colors]
    )


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