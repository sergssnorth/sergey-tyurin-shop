from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from app.models import ProductSize, Size
from app.db import get_session



from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, func, or_
from typing import List
from math import ceil
from pydantic import BaseModel


router = APIRouter()
class ProductSizeResponseModel(BaseModel):
    product_size_id: int
    product_id: int
    size_id: int
    size_name: str

class ProductSizesResponseModel(BaseModel):
    total_count: int
    total_pages: int
    product_sizes: List[ProductSizeResponseModel]

@router.get("/product-sizes", response_model = ProductSizesResponseModel)
async def get_products_sizes(offset: int = Query(0, ge=0),
                             limit: int = Query(50, gt=0),
                             search: str = Query(None),
                             product_id: Optional[int] = None, 
                             session: AsyncSession = Depends(get_session)):

    query = select(ProductSize, Size).join(Size)

    if search:
        query = query.where(Size.name.ilike(f"%{search}%"))

    if product_id is not None:
        query = query.filter(ProductSize.product_id == product_id)

    total_count_query = select(func.count()).select_from(query)
    total_count_result = await session.execute(total_count_query)
    total_count = total_count_result.scalar()
    total_pages = ceil(total_count / limit)

    query = query.offset(offset).limit(limit)
    product_sizes = await session.execute(query)

    product_sizes = [ProductSizeResponseModel(
            product_size_id = product_size.id,
            product_id = product_size.product_id,
            size_id = product_size.size_id,
            size_name = size.name,
        ) for product_size,size in product_sizes]
    
    return ProductSizesResponseModel(
        total_count=total_count,
        total_pages=total_pages,
        product_sizes=product_sizes
    )

@router.post("/product-size")
async def add_product_size(product_size: ProductSize, session: AsyncSession = Depends(get_session)):
    new_product_size = ProductSize(product_id=product_size.product_id, size_id = product_size.size_id)
    session.add(new_product_size)
    await session.commit()
    await session.refresh(new_product_size)
    return new_product_size


@router.put("/product-size/{product_size_id}")
async def update_product_size(product_size_id: int, updated_product_size: ProductSize, session: AsyncSession = Depends(get_session)):
    existing_product_size = await session.get(ProductSize, product_size_id)
    if existing_product_size is None:
        raise HTTPException(status_code=404, detail="Размер продукта не найден")
    existing_product_size.product_id = updated_product_size.product_id
    existing_product_size.size_id = updated_product_size.size_id
    await session.commit()
    await session.refresh(existing_product_size)
    return existing_product_size

@router.delete("/product-size/{product_size_id}")
async def delete_product_size(product_size_id: int, session: AsyncSession = Depends(get_session)):
    product_size = await session.get(ProductSize, product_size_id)
    if product_size is None:
        raise HTTPException(status_code=404, detail="Размер продукта не найден")
    try:
        await session.delete(product_size)
        await session.commit()
        return {"message": "Размер продукта успешно удален"}
    except Exception as e:
        print(f"Ошибка при удалении Размера продукта: {e}")
        await session.rollback()  # Откат изменений в случае ошибки