from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Size
from app.db import get_session
from sqlmodel import select

router = APIRouter()

@router.get("/sizes", response_model=list[Size])
async def get_sizes(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Size))
    sizes = result.scalars().all()
    return [Size(id=size.id, name=size.name, slug=size.slug) for size in sizes]

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