from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Size
from app.db import get_session

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, func, or_
from typing import List
from math import ceil
from pydantic import BaseModel


router = APIRouter()

class SizesResponseModel(BaseModel):
    total_count: int
    total_pages: int
    sizrs: List[Size]


@router.get("/sizes", response_model=SizesResponseModel)
async def get_sizes(offset: int = Query(0, ge=0),
                    limit: int = Query(50, gt=0),
                    search: str = Query(None),
                    session: AsyncSession = Depends(get_session)):
    query = select(Size)

    if search:
        query = query.where(Size.name.ilike(f"%{search}%"))

    total_count_query = select(func.count()).select_from(query)
    total_count_result = await session.execute(total_count_query)
    total_count = total_count_result.scalar()
    total_pages = ceil(total_count / limit)

    query = query.offset(offset).limit(limit)
    sizes_result = await session.execute(query)
    sizes = sizes_result.scalars().all()

    return SizesResponseModel(
        total_count=total_count,
        total_pages=total_pages,
        sizes=[
            Size(
                id=size.id,
                name=size.name,
                slug=size.slug,
            ) for size in sizes]
    )

@router.post("/size")
async def add_color(size: Size, session: AsyncSession = Depends(get_session)):
    new_size = Size(name=size.name, slug=size.slug)
    session.add(new_size)
    await session.commit()
    await session.refresh(new_size)
    return new_size

@router.put("/size/{size_id}")
async def update_size(size_id: int, updated_size: Size, session: AsyncSession = Depends(get_session)):
    existing_size = await session.get(Size, size_id)
    if existing_size is None:
        raise HTTPException(status_code=404, detail="Размер не найден")
    existing_size.name = updated_size.name
    existing_size.slug = updated_size.slug
    await session.commit()
    await session.refresh(existing_size)
    return existing_size

@router.delete("/size/{size_id}")
async def delete_size(size_id: int, session: AsyncSession = Depends(get_session)):
    existing_size = await session.get(Size, size_id)
    if existing_size is None:
        raise HTTPException(status_code=404, detail="Размер не найден")
    try:
        await session.delete(existing_size)
        await session.commit()
        return {"message": "Размер успешно добавлен"}
    except Exception as e:
        print(f"Ошибка при удалении размера: {e}")
        await session.rollback()  # Откат изменений в случае ошибки