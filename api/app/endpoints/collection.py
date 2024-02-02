from fastapi import APIRouter, Depends, HTTPException
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

@router.put("/collection/{collection_id}")
async def update_collection(collection_id: int, updated_collection: Collection, session: AsyncSession = Depends(get_session)):
    existing_collection = await session.get(Collection, collection_id)
    if existing_collection is None:
        raise HTTPException(status_code=404, detail="Коллекция не найдена")
    existing_collection.name = updated_collection.name
    existing_collection.slug = updated_collection.slug
    existing_collection.description = updated_collection.description
    await session.commit()
    await session.refresh(existing_collection)
    return existing_collection

@router.delete("/collection/{collection_id}")
async def delete_collection(collection_id: int, session: AsyncSession = Depends(get_session)):
    existing_collection = await session.get(Collection, collection_id)
    if existing_collection is None:
        raise HTTPException(status_code=404, detail="Коллекция не найдена")
    try:
        await session.delete(existing_collection)
        await session.commit()
        return {"message": "Коллекция успешно удалена"}
    except Exception as e:
        print(f"Ошибка при удалении Коллекции: {e}")
        await session.rollback()  # Откат изменений в случае ошибки