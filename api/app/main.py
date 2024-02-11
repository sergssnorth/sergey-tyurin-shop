from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from app.db import get_session
from app.endpoints import big_category
from app.endpoints import category
from app.endpoints import collection
from app.endpoints import models
from app.endpoints import color
from app.endpoints import size
from app.endpoints import warehouse
from app.endpoints import product
from app.endpoints import product_size
from app.endpoints import order_status
from app.endpoints import client
from app.endpoints import order

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(big_category.router)
app.include_router(category.router)
app.include_router(collection.router)
app.include_router(models.router)
app.include_router(color.router)
app.include_router(size.router)
app.include_router(warehouse.router)
app.include_router(product.router)
app.include_router(product_size.router)
app.include_router(order_status.router)
app.include_router(client.router)
app.include_router(order.router)

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
