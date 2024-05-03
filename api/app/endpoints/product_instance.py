from sqlalchemy.ext.asyncio import AsyncSession
from app.models import ProductInstance, Size, Product, Model, Color
from app.db import get_session

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, and_, join, or_, func
from typing import List
from math import ceil
from pydantic import BaseModel


router = APIRouter()

class ProductInstanceResponseModel(BaseModel):
    id: int
    product_id: int
    size_id: int
    model_name: str
    color_name: str
    size_name: str

class ProductInstancesResponseModel(BaseModel):
    total_count: int
    total_pages: int
    product_instances: List[ProductInstanceResponseModel]


@router.get("/product-instances", response_model=ProductInstancesResponseModel)
async def get_product_instances(offset: int = Query(0, ge=0),
                     limit: int = Query(50, gt=0),
                     search: str = Query(None),

                     product_id: int = Query(None),
                     size_id: int = Query(None),

                     sort_by: str = Query(None, description="Sort by 'id'."),
                     order: str = Query("desc", description="Sort product_instance: 'asc' or 'desc'."),

                     session: AsyncSession = Depends(get_session)):

    query = select(ProductInstance, Product, Color, Model, Size).join(ProductInstance.product).join(Product.color).join(Product.model).join(ProductInstance.size)

    if search:
        query = query.filter(or_(
            ProductInstance.id.ilike(f"%{search}%")
        ))    

    if product_id:
        query = query.filter(ProductInstance.product_id == product_id)

    if size_id:
        query = query.filter(ProductInstance.size_id == size_id)

    if sort_by and order:
        if sort_by == "id":
            query = query.order_by(ProductInstance.id.desc() if order == "desc" else ProductInstance.id.asc())
    else:
        #Сортировака по умолчанию
        query = query.order_by(ProductInstance.id.desc() if order == "desc" else ProductInstance.id.asc())


    total_count_query = select(func.count()).select_from(query)
    total_count_result = await session.execute(total_count_query)
    total_count = total_count_result.scalar()
    total_pages = ceil(total_count / limit)

    query = query.offset(offset).limit(limit)
    product_instances_and_sizes = await session.execute(query)

    product_instances = [ProductInstanceResponseModel(
            id=product_instance.id,
            product_id=product_instance.product_id,
            size_id=product_instance.size_id,
            model_name= model.name,
            color_name = color.name,
            size_name=size.name,
        ) for product_instance, product, color, model, size in product_instances_and_sizes]

    return ProductInstancesResponseModel(
        total_count=total_count,
        total_pages=total_pages,
        product_instances=product_instances
    )


@router.post("/product-instance")
async def add_product_instance(product_instance: ProductInstance, session: AsyncSession = Depends(get_session)):
    new_product_instance = ProductInstance(product_id=product_instance.product_id, size_id=product_instance.size_id)
    session.add(new_product_instance)
    await session.commit()
    await session.refresh(new_product_instance)
    return new_product_instance

@router.put("/product-instance/{product_instance_id}")
async def update_product_instance(product_instance_id: int, updated_product_instance: ProductInstance, session: AsyncSession = Depends(get_session)):
    existing_product_instance = await session.get(ProductInstance, product_instance_id)
    if existing_product_instance is None:
        raise HTTPException(status_code=404, detail="Заказ не найден")
    existing_product_instance.id = updated_product_instance.id
    existing_product_instance.product_id = updated_product_instance.product_id
    existing_product_instance.size_id = updated_product_instance.size_id
    await session.commit()
    await session.refresh(existing_product_instance)
    return existing_product_instance

@router.delete("/product-instance/{product_instance_id}")
async def delete_product_instance(product_instance_id: int, session: AsyncSession = Depends(get_session)):
    product_instance = await session.get(ProductInstance, product_instance_id)
    if product_instance is None:
        raise HTTPException(status_code=404, detail="Заказа не найден")
    try:
        await session.delete(product_instance)
        await session.commit()
        return {"message": "Заказ успешно удален"}
    except Exception as e:
        print(f"Ошибка при удалении Заказа: {e}")
        await session.rollback()  # Откат изменений в случае ошибки