from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Collection
from app.db import get_session
from sqlmodel import select


router = APIRouter()


@router.get("/collections", response_model=list[Collection])
async def get_collections(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Collection))
    collections = result.scalars().all()
    return [Collection(id=collection.id, name=collection.name, slug=collection.slug, description=collection.description) for collection in collections]

@router.post("/collection")
async def add_collection(collection: Collection, session: AsyncSession = Depends(get_session)):
    new_collection = Collection(name=collection.name, slug=collection.slug, description=collection.description)
    session.add(new_collection)
    await session.commit()
    await session.refresh(new_collection)
    return new_collection