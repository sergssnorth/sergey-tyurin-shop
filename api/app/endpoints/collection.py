from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Collection
from app.db import get_session


from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, func, or_
from typing import List
from math import ceil
from pydantic import BaseModel


router = APIRouter()

class CollectionResponseModel(BaseModel):
    total_count: int
    total_pages: int
    collections: List[Collection]


@router.get("/collections", response_model=CollectionResponseModel)
async def get_collections(offset: int = Query(0, ge=0),
                          limit: int = Query(50, gt=0),
                          search: str = Query(None),
                          session: AsyncSession = Depends(get_session)):
    
    query = select(Collection).offset(offset).limit(limit)
    
    if search:
        query = query.filter(or_(
            Collection.name.ilike(f"%{search}%")
        ))

    total_count = await session.scalar(select(func.count()).select_from(query.alias()))
    total_pages = ceil(total_count / limit)
    collections_result = await session.execute(query)
    collections = collections_result.scalars().all()

    return CollectionResponseModel(
        total_count=total_count,
        total_pages=total_pages,
        collections=[
            Collection(
                id=collection.id,
                name=collection.name,
                slug=collection.slug,
                description=collection.description
            ) for collection in collections
        ]
    )


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