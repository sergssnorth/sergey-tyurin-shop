from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Model, Category
from app.db import get_session


from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, and_, join, or_, func
from typing import List
from math import ceil
from pydantic import BaseModel


router = APIRouter()

class ModelResponseModel(BaseModel):
    id: int
    name: str
    slug: str
    category_id: Optional[int] = None
    collection_id: Optional[int] = None
    detail_id: Optional[int] = None
    size_guide_id: Optional[int] = None

class ModelsResponseModel(BaseModel):
    total_count: int
    total_pages: int
    models: List[ModelResponseModel]


@router.get("/models", response_model=ModelsResponseModel)
async def get_models(offset: int = Query(0, ge=0),
                     limit: int = Query(50, gt=0),
                     search: str = Query(None),

                     category_id: Optional[int] = None, 
                     collection_id: Optional[int] = None, 
                     model_id: Optional[int] = None,
                     detail_id: Optional[int] = None,
                     size_guide_id: Optional[int] = None,

                     sort_by: str = Query(None, description="Sort by 'name' or 'id'."),
                     order: str = Query("desc", description="Sort order: 'asc' or 'desc'."),
                     session: AsyncSession = Depends(get_session)):

    query = select(Model)

    if search:
        query = query.filter(or_(
            Model.name.ilike(f"%{search}%")
        ))    

    if category_id is not None:
        query = query.filter(Model.category_id == category_id)

    if collection_id is not None:
        query = query.filter(Model.collection_id == collection_id)

    if model_id is not None:
        query = query.filter(Model.id == model_id)

    if detail_id is not None:
        query = query.filter(Model.detail_id == detail_id)

    if size_guide_id is not None:
        query = query.filter(Model.size_guide_id == size_guide_id)

    if sort_by and order:
        if sort_by == "name":
            query = query.order_by(Model.name.desc() if order == "desc" else Model.name.asc())
        elif sort_by == "id":
            query = query.order_by(Model.id.desc() if order == "desc" else Model.id.asc())
    else:
        #Сортировака по умолчанию
        query = query.order_by(Model.id.desc() if order == "desc" else Model.id.asc())

    total_count_query = select(func.count()).select_from(query)
    total_count_result = await session.execute(total_count_query)
    total_count = total_count_result.scalar()
    total_pages = ceil(total_count / limit)

    query = query.offset(offset).limit(limit)
    models = await session.execute(query)
    models = models.scalars().all()

    models = [ModelResponseModel(
            id=model.id, 
            name=model.name,
            slug=model.slug,
            category_id=model.category_id,
            collection_id=model.collection_id,
            detail_id=model.detail_id,
            size_guide_id=model.size_guide_id
        ) for model in models]
    
    return ModelsResponseModel(
        total_count=total_count,
        total_pages=total_pages,
        models=models
    )
    

@router.post("/model")
async def add_model(model: Model, session: AsyncSession = Depends(get_session)):
    new_model = Model(name=model.name, 
                      slug=model.slug,
                      category_id=model.category_id,
                      collection_id=model.collection_id,  
                      detail_id=model.detail_id,
                      size_guide_id=model.size_guide_id)
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
    existing_model.collection_id = updated_model.collection_id
    existing_model.category_id = updated_model.category_id
    existing_model.detail_id = updated_model.detail_id
    existing_model.size_guide_id = updated_model.size_guide_id
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