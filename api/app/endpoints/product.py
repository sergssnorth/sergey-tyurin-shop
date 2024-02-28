from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Product, Color
from app.db import get_session


from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, and_, join, or_, func
from typing import List
from math import ceil
from pydantic import BaseModel
router = APIRouter()

class ProductResponseModel(BaseModel):
    id: int
    model_id: int
    color_id: int
    color_name: str

class ProductsResponseModel(BaseModel):
    total_count: int
    total_pages: int
    products: List[ProductResponseModel]


@router.get("/products", response_model=ProductsResponseModel)
async def get_products(offset: int = Query(0, ge=0),
                       limit: int = Query(50, gt=0),
                       search: str = Query(None),
                       model_id: Optional[int] = None, 
                       session: AsyncSession = Depends(get_session)):

    query = select(Product, Color).join(Color)

    if search:
        query = query.filter(or_(
            Color.name.ilike(f"%{search}%")
        ))    

    if model_id is not None:
        query = query.filter(Product.model_id == model_id)
                   
    total_count_query = select(func.count()).select_from(query)
    total_count_result = await session.execute(total_count_query)
    total_count = total_count_result.scalar()
    total_pages = ceil(total_count / limit)

    query = query.offset(offset).limit(limit)
    products_and_colors = await session.execute(query)

    products = [ProductResponseModel(
            id = product.id, 
            model_id = product.model_id,
            color_id = product.color_id,
            color_name= color.name,
        ) for product, color in products_and_colors]

    return ProductsResponseModel(
        total_count=total_count,
        total_pages=total_pages,
        products=products
    )


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