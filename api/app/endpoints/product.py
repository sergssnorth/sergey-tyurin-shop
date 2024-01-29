from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Product
from app.db import get_session
from sqlmodel import select


router = APIRouter()


@router.get("/products", response_model=list[Product])
async def get_products(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Product))
    products = result.scalars().all()
    return [Product(id=product.id, model_id=product.model_id, color_id=product.color_id, size_id=product.size_id) for product in products]

@router.post("/product")
async def add_product(product: Product, session: AsyncSession = Depends(get_session)):
    new_product = Product(model_id=product.model_id, color_id=product.color_id, size_id=product.size_id)
    session.add(new_product)
    await session.commit()
    await session.refresh(new_product)
    return new_product