from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import WarehouseElement, ProductInstance, Size , Product, Model
from app.db import get_session


from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, and_, join, or_, func
from typing import List
from math import ceil
from pydantic import BaseModel


router = APIRouter()

class WarehouseElementResponseModel(BaseModel):
    id: int
    warehouse_id: Optional[int] = None
    product_instance_id: Optional[int] = None
    model_name: str
    size_name: str
    count: int

class WarehouseElementsResponseModel(BaseModel):
    total_count: int
    total_pages: int
    warehouse_elements: List[WarehouseElementResponseModel]

@router.get("/warehouse-elements", response_model=WarehouseElementsResponseModel)
async def get_warehouse_elements(
    offset: int = Query(0, ge=0),
    limit: int = Query(50, gt=0),
    warehouse_id: Optional[int] = None,
    product_instance_id: Optional[int] = None,
    sort_by: str = Query(None, description="Sort by 'name' or 'id'."),
    order: str = Query("desc", description="Sort order: 'asc' or 'desc'."),
    session: AsyncSession = Depends(get_session)
):

    query = (
        select(WarehouseElement, ProductInstance, Product, Size, Model)
        .join(WarehouseElement.product_instances)
        .join(ProductInstance.size)
        .join(ProductInstance.product)
        .join(Model)
    )

    if warehouse_id is not None:
        query = query.filter(WarehouseElement.warehouse_id == warehouse_id)

    if product_instance_id is not None:
        query = query.filter(WarehouseElement.product_instance_id == product_instance_id)

    if sort_by and order:
        if sort_by == "id":
            query = query.order_by(
                WarehouseElement.id.desc() if order == "desc" else WarehouseElement.id.asc()
            )
    else:
        query = query.order_by(
            WarehouseElement.id.desc() if order == "desc" else WarehouseElement.id.asc()
        )

    total_count_query = select(func.count()).select_from(WarehouseElement)
    total_count_result = await session.execute(total_count_query)
    total_count = total_count_result.scalar()
    total_pages = ceil(total_count / limit)

    query = query.offset(offset).limit(limit)
    warehouse_elements = await session.execute(query)

    response_data = []
    for warehouse_element, product_instance, product, size, model in warehouse_elements:
        response_data.append(
            WarehouseElementResponseModel(
                id=warehouse_element.id,
                warehouse_id=warehouse_element.warehouse_id,
                product_instance_id=warehouse_element.product_instance_id,
                model_name=model.name,
                size_name=size.name,
                count=warehouse_element.count,
            )
        )

    return WarehouseElementsResponseModel(
        total_count=total_count,
        total_pages=total_pages,
        warehouse_elements=response_data
    ) 

@router.post("/warehouse-element")
async def add_warehouse_element(warehouse_element: WarehouseElement, session: AsyncSession = Depends(get_session)):
    new_warehouse_element = WarehouseElement(id=warehouse_element.id, 
                        warehouse_id=warehouse_element.warehouse_id,
                        product_instance_id=warehouse_element.product_instance_id,
                        count=warehouse_element.count)
    session.add(new_warehouse_element)
    await session.commit()
    await session.refresh(new_warehouse_element)
    return new_warehouse_element

@router.put("/warehouse-element/{warehouse_element_id}")
async def update_warehouse_element(warehouse_element_id: int, updated_warehouse_element: WarehouseElement, session: AsyncSession = Depends(get_session)):
    existing_warehouse_element = await session.get(WarehouseElement, warehouse_element_id)
    if existing_warehouse_element is None:
        raise HTTPException(status_code=404, detail="Модель не найдена")
    existing_warehouse_element.warehouse_id = updated_warehouse_element.warehouse_id
    existing_warehouse_element.product_instance_id = updated_warehouse_element.product_instance_id
    existing_warehouse_element.count = updated_warehouse_element.count
    await session.commit()
    await session.refresh(existing_warehouse_element)
    return existing_warehouse_element

@router.delete("/warehouse-element/{warehouse_element_id}")
async def delete_warehouse_element(warehouse_element_id: int, session: AsyncSession = Depends(get_session)):
    existing_warehouse_element = await session.get(WarehouseElement, warehouse_element_id)
    if existing_warehouse_element is None:
        raise HTTPException(status_code=404, detail="Модель не найдена")
    try:
        await session.delete(existing_warehouse_element)
        await session.commit()
        return {"message": "Модель успешно удалена"}
    except Exception as e:
        print(f"Ошибка при удалении Модели: {e}")
        await session.rollback()  # Откат изменений в случае ошибки