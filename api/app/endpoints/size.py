from fastapi import APIRouter, Depends
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

@router.post("/color")
async def add_color(size: Size, session: AsyncSession = Depends(get_session)):
    new_size = Size(name=size.name, slug=size.slug)
    session.add(new_size)
    await session.commit()
    await session.refresh(new_size)
    return new_size