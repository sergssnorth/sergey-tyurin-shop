from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Product, Color
from app.db import get_session
from sqlmodel import select, join
from pydantic import BaseModel 

router = APIRouter()

class ModelResponse(BaseModel):
    id: int
    model_id: int
    color_id: int
    color_name: str




@router.get("/products", response_model=list[ModelResponse])
async def get_products(
    model_id: Optional[int] = None, 
    session: AsyncSession = Depends(get_session)):

    query = select(Product, Color).join(Color)
    if model_id is not None:
        query = query.filter(Product.model_id == model_id)
                   
    products = await session.execute(query)
    product_list = list(products)

    print(product_list)
    result_list = []
    for product,color in product_list:
        result_list.append(
            ModelResponse(
                id = product.id, 
                model_id = product.model_id,
                color_id = product.color_id,
                color_name= color.name,
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


@router.put("/product/{product_id}")
async def update_product(product_id: int, updated_product: Product, session: AsyncSession = Depends(get_session)):
    existing_product = await session.get(Product, product_id)
    if existing_product is None:
        raise HTTPException(status_code=404, detail="Продукт не найден")
    existing_product.model_id = updated_product.model_id
    existing_product.color_id = updated_product.color_id
    await session.commit()
    await session.refresh(existing_product)
    return existing_product

@router.delete("/product/{product_id}")
async def delete_product(product_id: int, session: AsyncSession = Depends(get_session)):
    product = await session.get(Product, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Продукт не найден")
    try:
        await session.delete(product)
        await session.commit()
        return {"message": "Продукт успешно удален"}
    except Exception as e:
        print(f"Ошибка при удалении Продукта: {e}")
        await session.rollback()  # Откат изменений в случае ошибки