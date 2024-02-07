from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Product
from app.db import get_session
from sqlmodel import select
from pydantic import BaseModel 

router = APIRouter()

class ModelResponse(BaseModel):
    id: int
    model_id: int
    color_id: str
    size_id: int



@router.get("/products", response_model=list[Product])
async def get_products(
    model_id: Optional[int] = None, 
    session: AsyncSession = Depends(get_session)):

    query = select(Product)
    if model_id is not None:
        query = query.filter(Product.model_id == model_id)
                   
    products = await session.execute(query)
    product_list = list(products)

    print(product_list)
    result_list = []
    for product in product_list:
        product = product[0] 
        result_list.append(
            ModelResponse(
                id = product.id, 
                model_id = product.model_id,
                color_id = product.color_id,
                size_id = product.size_id,
            )
        )
    return result_list


@router.post("/product")
async def add_product(product: Product, session: AsyncSession = Depends(get_session)):
    new_product = Product(model_id=product.model_id, color_id=product.color_id, size_id=product.size_id)
    session.add(new_product)
    await session.commit()
    await session.refresh(new_product)
    return new_product