from fastapi import Depends, FastAPI
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from app.db import get_session
from app.endpoints import big_category

app = FastAPI()

app.include_router(big_category.router)

# @app.get("/big_categories", response_model=list[BigCategory])
# async def get_big_categories(session: AsyncSession = Depends(get_session)):
#     result = await session.execute(select(BigCategory))
#     big_categories = result.scalars().all()
#     return [BigCategory(id=big_category.id, name=big_category.name, slug=big_category.slug) for big_category in big_categories]

# @app.post("/big_categories")
# async def add_big_categories(big_category: BigCategory, session: AsyncSession = Depends(get_session)):
#     new_big_category = BigCategory(name = big_category.name, slug=big_category.slug)
#     session.add(new_big_category)
#     await session.commit()
#     await session.refresh(new_big_category)
#     return new_big_category
