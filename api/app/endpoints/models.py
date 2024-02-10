from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Model, Category, BigCategory
from app.db import get_session
from sqlmodel import select, and_, join
from pydantic import BaseModel 

router = APIRouter()

class ModelResponse(BaseModel):
    id: int
    name: str
    slug: str
    description: str
    collection_id: int
    big_category_id: int
    category_id: int


@router.get("/models")
async def get_models(
    big_category_id: Optional[int] = None, 
    category_id: Optional[int] = None, 
    collection_id: Optional[int] = None, 
    model_id: Optional[int] = None, 
    session: AsyncSession = Depends(get_session)):

    query = select(Model, Category).join(Category)

    if big_category_id is not None:
        query = query.filter(Category.big_category_id == big_category_id)

    if category_id is not None:
        query = query.filter(Model.category_id == category_id)

    if collection_id is not None:
        query = query.filter(Model.collection_id == collection_id)

    if model_id is not None:
        query = query.filter(Model.id == model_id)

    models_and_categories = await session.execute(query)
    models_and_categories_list = list(models_and_categories)
    

    result_list = []

    for model, category in models_and_categories_list:
        result_list.append(
            ModelResponse(
                id=model.id, 
                name=model.name,
                slug= model.slug,
                description=model.description,
                collection_id = model.collection_id,
                big_category_id = category.big_category_id,
                category_id = model.category_id,
            )
        )

    return result_list
    

@router.post("/model")
async def add_model(model: Model, session: AsyncSession = Depends(get_session)):
    new_model = Model(name=model.name, slug=model.slug, description=model.description, collection_id=model.collection_id, category_id=model.category_id)
    session.add(new_model)
    await session.commit()
    await session.refresh(new_model)
    return new_model

@router.put("/model/{model_id}")
async def update_collection(model_id: int, updated_model: Model, session: AsyncSession = Depends(get_session)):
    existing_model = await session.get(Model, model_id)
    if existing_model is None:
        raise HTTPException(status_code=404, detail="Модель не найдена")
    existing_model.name = updated_model.name
    existing_model.slug = updated_model.slug
    existing_model.description = updated_model.description
    existing_model.collection_id = updated_model.collection_id
    existing_model.category_id = updated_model.category_id
    await session.commit()
    await session.refresh(existing_model)
    return existing_model

@router.delete("/model/{model_id}")
async def delete_collection(model_id: int, session: AsyncSession = Depends(get_session)):
    existing_model = await session.get(Model, model_id)
    if existing_model is None:
        raise HTTPException(status_code=404, detail="Модель не найдена")
    try:
        await session.delete(existing_model)
        await session.commit()
        return {"message": "Модель успешно удалена"}
    except Exception as e:
        print(f"Ошибка при удалении Модели: {e}")
        await session.rollback()  # Откат изменений в случае ошибки