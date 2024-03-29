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
from app.endpoints import detail


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
app.include_router(detail.router)
