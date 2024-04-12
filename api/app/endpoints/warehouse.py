from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Warehouse
from app.db import get_session


from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, and_, join, or_, func
from typing import List
from math import ceil
from pydantic import BaseModel


router = APIRouter()

class WarehouseResponseModel(BaseModel):
    id: int
    name: str

class WarehousesResponseModel(BaseModel):
    total_count: int
    total_pages: int
    warehouses: List[WarehouseResponseModel]


@router.get("/warehouses", response_model=WarehousesResponseModel)
async def get_models(offset: int = Query(0, ge=0),
                     limit: int = Query(50, gt=0),
                     search: str = Query(None),

                     sort_by: str = Query(None, description="Sort by 'name' or 'id'."),
                     order: str = Query("desc", description="Sort order: 'asc' or 'desc'."),
                     session: AsyncSession = Depends(get_session)):

    query = select(Warehouse)

    if search:
        query = query.filter(or_(
            Warehouse.name.ilike(f"%{search}%")
        ))    

    if sort_by and order:
        if sort_by == "name":
            query = query.order_by(Warehouse.name.desc() if order == "desc" else Warehouse.name.asc())
        elif sort_by == "id":
            query = query.order_by(Warehouse.id.desc() if order == "desc" else Warehouse.id.asc())
    else:
        #Сортировака по умолчанию
        query = query.order_by(Warehouse.id.desc() if order == "desc" else Warehouse.id.asc())

    total_count_query = select(func.count()).select_from(query)
    total_count_result = await session.execute(total_count_query)
    total_count = total_count_result.scalar()
    total_pages = ceil(total_count / limit)

    query = query.offset(offset).limit(limit)
    warehouses = await session.execute(query)
    warehouses = warehouses.scalars().all()

    warehouses = [WarehouseResponseModel(
            id=warehouse.id, 
            name=warehouse.name,
        ) for warehouse in warehouses]
    
    return WarehousesResponseModel(
        total_count=total_count,
        total_pages=total_pages,
        warehouses=warehouses
    )
    

@router.post("/warehouse")
async def add_warehouse(warehouse: Warehouse, session: AsyncSession = Depends(get_session)):
    new_warehouse = Warehouse(name=warehouse.name)
    session.add(new_warehouse)
    await session.commit()
    await session.refresh(new_warehouse)
    return new_warehouse

@router.put("/warehouse/{warehouse_id}")
async def update_warehouse(warehouse_id: int, updated_warehouse: Warehouse, session: AsyncSession = Depends(get_session)):
    existing_warehouse = await session.get(Warehouse, warehouse_id)
    if existing_warehouse is None:
        raise HTTPException(status_code=404, detail="Модель не найдена")
    existing_warehouse.name = updated_warehouse.name
    await session.commit()
    await session.refresh(existing_warehouse)
    return existing_warehouse

@router.delete("/warehouse/{warehouse_id}")
async def delete_warehouse(warehouse_id: int, session: AsyncSession = Depends(get_session)):
    existing_warehouse = await session.get(Warehouse, warehouse_id)
    if existing_warehouse is None:
        raise HTTPException(status_code=404, detail="Модель не найдена")
    try:
        await session.delete(existing_warehouse)
        await session.commit()
        return {"message": "Модель успешно удалена"}
    except Exception as e:
        print(f"Ошибка при удалении Модели: {e}")
        await session.rollback()  # Откат изменений в случае ошибки