from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Warehouse
from app.db import get_session
from sqlmodel import select


router = APIRouter()


@router.get("/warehouses", response_model=list[Warehouse])
async def get_warehouses(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Warehouse))
    warehouses = result.scalars().all()
    return [Warehouse(id=warehouse.id, name=warehouse.name, description=warehouse.description) for warehouse in warehouses]

@router.post("/warehouse")
async def add_warehouse(warehouse: Warehouse, session: AsyncSession = Depends(get_session)):
    new_warehouse = Warehouse(name=warehouse.name, description=warehouse.description)
    session.add(new_warehouse)
    await session.commit()
    await session.refresh(new_warehouse)
    return new_warehouse