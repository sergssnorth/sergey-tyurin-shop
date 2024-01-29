from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Model
from app.db import get_session
from sqlmodel import select


router = APIRouter()


@router.get("/models", response_model=list[Model])
async def get_models(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Model))
    models = result.scalars().all()
    return [Model(id=model.id, name=model.name, slug=model.slug, description=model.description, collection_id=model.collection_id, category_id=model.category_id) for model in models]

@router.post("/model")
async def add_model(model: Model, session: AsyncSession = Depends(get_session)):
    new_model = Model(name=model.name, slug=model.slug, description=model.description, collection_id=model.collection_id, category_id=model.category_id)
    session.add(new_model)
    await session.commit()
    await session.refresh(new_model)
    return new_model