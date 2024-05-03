from datetime import datetime
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import PriceListElement, ProductInstance, Size ,Product, Model
from app.db import get_session


from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, and_, join, or_, func
from typing import List
from math import ceil
from pydantic import BaseModel


router = APIRouter()

class PriceListElementResponseModel(BaseModel):
    id: int
    price_list_id: Optional[int] = None
    product_id: int
    product_instance_id: Optional[int] = None
    model_name: str
    size_name: str
    price: float

class PriceListElementsResponseModel(BaseModel):
    total_count: int
    total_pages: int
    price_list_elements: List[PriceListElementResponseModel]

@router.get("/price-list-elements", response_model=PriceListElementsResponseModel)
async def get_price_list_elements(
    offset: int = Query(0, ge=0),
    limit: int = Query(50, gt=0),

    price_list_id: Optional[int] = None,
    product_id: Optional[int] = None,
    product_instance_id: Optional[int] = None,

    sort_by: str = Query(None, description="Sort by 'name' or 'id'."),
    order: str = Query("desc", description="Sort order: 'asc' or 'desc'."),
    session: AsyncSession = Depends(get_session)
):

    query = (
        select(PriceListElement, ProductInstance, Product, Size, Model)
        .join(PriceListElement.product_instances)
        .join(ProductInstance.size)
        .join(ProductInstance.product)
        .join(Model)
    )

    if price_list_id is not None:
        query = query.filter(PriceListElement.price_list_id == price_list_id)

    if product_id is not None:
        query = query.filter(Product.id == product_id)

    if product_instance_id is not None:
        query = query.filter(PriceListElement.product_instance_id == product_instance_id)

    if sort_by and order:
        if sort_by == "id":
            query = query.order_by(
                PriceListElement.id.desc() if order == "desc" else PriceListElement.id.asc()
            )
    else:
        query = query.order_by(
            PriceListElement.id.desc() if order == "desc" else PriceListElement.id.asc()
        )

    total_count_query = select(func.count()).select_from(PriceListElement)
    total_count_result = await session.execute(total_count_query)
    total_count = total_count_result.scalar()
    total_pages = ceil(total_count / limit)

    query = query.offset(offset).limit(limit)
    price_list_elements = await session.execute(query)

    response_data = []
    for price_list_element, product_instance, product, size, model in price_list_elements:
        response_data.append(
            PriceListElementResponseModel(
                id=price_list_element.id,
                price_list_id=price_list_element.price_list_id,
                product_id=product.id,
                product_instance_id=price_list_element.product_instance_id,
                model_name=model.name,
                size_name=size.name,
                price=price_list_element.price
            )
        )

    return PriceListElementsResponseModel(
        total_count=total_count,
        total_pages=total_pages,
        price_list_elements=response_data
    ) 

@router.post("/price-list-element")
async def add_price_list_element(price_list_element: PriceListElement, session: AsyncSession = Depends(get_session)):
    new_price_list_element = PriceListElement(id=price_list_element.id, 
                        price_list_id=price_list_element.price_list_id,
                        product_instance_id=price_list_element.product_instance_id,
                        price=price_list_element.price)
    session.add(new_price_list_element)
    await session.commit()
    await session.refresh(new_price_list_element)
    return new_price_list_element

@router.put("/price-list-element/{price_list_element_id}")
async def update_price_list_element(price_list_element_id: int, updated_price_list_element: PriceListElement, session: AsyncSession = Depends(get_session)):
    existing_price_list_element = await session.get(PriceListElement, price_list_element_id)
    if existing_price_list_element is None:
        raise HTTPException(status_code=404, detail="Модель не найдена")
    existing_price_list_element.price_list_id = updated_price_list_element.price_list_id
    existing_price_list_element.product_instance_id = updated_price_list_element.product_instance_id
    existing_price_list_element.price = updated_price_list_element.price
    await session.commit()
    await session.refresh(existing_price_list_element)
    return existing_price_list_element

@router.delete("/price-list-element/{price_list_element_id}")
async def delete_price_list_element(price_list_element_id: int, session: AsyncSession = Depends(get_session)):
    existing_price_list_element = await session.get(PriceListElement, price_list_element_id)
    if existing_price_list_element is None:
        raise HTTPException(status_code=404, detail="Модель не найдена")
    try:
        await session.delete(existing_price_list_element)
        await session.commit()
        return {"message": "Модель успешно удалена"}
    except Exception as e:
        print(f"Ошибка при удалении Модели: {e}")
        await session.rollback()  # Откат изменений в случае ошибки