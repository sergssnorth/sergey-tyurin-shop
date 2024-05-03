from datetime import datetime
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import OrderElement, PriceListElement, ProductInstance, Size ,Product, Model
from app.db import get_session


from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, and_, join, or_, func
from typing import List
from math import ceil
from pydantic import BaseModel


router = APIRouter()

class OrderElementResponseModel(BaseModel):
    id: int
    order_id: int
    price_list_element_id: int
    count: int
    price: float
    product_instance_id: Optional[int] = None
    model_name: str
    size_name: str

class OrderElementsResponseModel(BaseModel):
    total_count: int
    total_pages: int
    order_elements: List[OrderElementResponseModel]

@router.get("/order-elements", response_model=OrderElementsResponseModel)
async def get_order_elements(
    offset: int = Query(0, ge=0),
    limit: int = Query(50, gt=0),

    order_id: Optional[int] = None,

    sort_by: str = Query(None, description="Sort by 'name' or 'id'."),
    order: str = Query("desc", description="Sort order: 'asc' or 'desc'."),
    session: AsyncSession = Depends(get_session)
):

    query = (
        select(OrderElement, PriceListElement, ProductInstance, Product, Size, Model)
        .join(OrderElement.price_list_element)
        .join(PriceListElement.product_instances)
        .join(ProductInstance.size)
        .join(ProductInstance.product)
        .join(Model)
    )

    if order_id is not None:
        query = query.filter(OrderElement.order_id == order_id)

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
    order_elements = await session.execute(query)

    response_data = []
    for order_element, price_list_element, product_instance, product, size, model in order_elements:
        response_data.append(
            OrderElementResponseModel(
                id=order_element.id,
                order_id=order_element.order_id,
                count=order_element.count,
                price_list_element_id=price_list_element.id,
                price_list_id=price_list_element.price_list_id,
                product_instance_id=price_list_element.product_instance_id,
                model_name=model.name,
                size_name=size.name,
                price=price_list_element.price
            )
        )

    return OrderElementsResponseModel(
        total_count=total_count,
        total_pages=total_pages,
        order_elements=response_data
    ) 

@router.post("/order-element")
async def add_order_element(order_element: OrderElement, session: AsyncSession = Depends(get_session)):
    new_order_element = OrderElement(order_id=order_element.order_id,
                        price_list_element_id=order_element.price_list_element_id,
                        count=order_element.count)
    session.add(new_order_element)
    await session.commit()
    await session.refresh(new_order_element)
    return new_order_element

@router.put("/order-element/{order_element_id}")
async def update_order_element(order_element_id: int, updated_order_element: OrderElement, session: AsyncSession = Depends(get_session)):
    existing_order_element = await session.get(OrderElement, order_element_id)
    if existing_order_element is None:
        raise HTTPException(status_code=404, detail="Элемент заказа не найден")
    existing_order_element.order_id = updated_order_element.order_id
    existing_order_element.price_list_element_id = updated_order_element.price_list_element_id
    existing_order_element.count = updated_order_element.count
    await session.commit()
    await session.refresh(existing_order_element)
    return existing_order_element

@router.delete("/order-element/{order_element_id}")
async def delete_price_list_element(order_element_id: int, session: AsyncSession = Depends(get_session)):
    existing_order_element = await session.get(OrderElement, order_element_id)
    if existing_order_element is None:
        raise HTTPException(status_code=404, detail="Элемент заказа не найден")
    try:
        await session.delete(existing_order_element)
        await session.commit()
        return {"message": "Элемент заказа успешно удален"}
    except Exception as e:
        print(f"Ошибка при удалении Элемента заказа: {e}")
        await session.rollback()  # Откат изменений в случае ошибки