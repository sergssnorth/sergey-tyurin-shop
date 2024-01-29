from fastapi import APIRouter, Depends
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