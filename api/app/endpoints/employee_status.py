from sqlalchemy.ext.asyncio import AsyncSession
from app.models import EmployeeStatus
from app.db import get_session


from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, func, or_
from typing import List
from math import ceil
from pydantic import BaseModel


router = APIRouter()

class EmployeeStatusResponseModel(BaseModel):
    total_count: int
    total_pages: int
    employee_statuses: List[EmployeeStatus]

@router.get("/employee-statuses", response_model=EmployeeStatusResponseModel)
async def get_employee_statuses(offset: int = Query(0, ge=0),
                     limit: int = Query(50, gt=0),
                     search: str = Query(None),

                     sort_by: str = Query(None, description="Sort by 'name' or 'id'."),
                     order: str = Query("desc", description="Sort order: 'asc' or 'desc'."),

                     session: AsyncSession = Depends(get_session)):
    
    query = select(EmployeeStatus)

    if search:
        query = query.where(EmployeeStatus.name.ilike(f"%{search}%"))

    if sort_by and order:
        if sort_by == "name":
            query = query.order_by(EmployeeStatus.name.desc() if order == "desc" else EmployeeStatus.name.asc())
        elif sort_by == "id":
            query = query.order_by(EmployeeStatus.id.desc() if order == "desc" else EmployeeStatus.id.asc())
    else:
        #Сортировака по умолчанию
        query = query.order_by(EmployeeStatus.id.desc() if order == "desc" else EmployeeStatus.id.asc())

    total_count_query = select(func.count()).select_from(query)
    total_count_result = await session.execute(total_count_query)
    total_count = total_count_result.scalar()
    total_pages = ceil(total_count / limit)

    query = query.offset(offset).limit(limit)
    employee_statuses_result = await session.execute(query)
    employee_statuses = employee_statuses_result.scalars().all()

    return EmployeeStatusResponseModel(
        total_count=total_count,
        total_pages=total_pages,
        employee_statuses=[
            EmployeeStatus(
                id=employee_status.id,
                name=employee_status.name
            ) for employee_status in employee_statuses]
    )


@router.post("/employee-status")
async def add_employee_status(employee_status: EmployeeStatus, session: AsyncSession = Depends(get_session)):
    new_employee_status = EmployeeStatus(name=employee_status.name)
    session.add(new_employee_status)
    await session.commit()
    await session.refresh(new_employee_status)
    return new_employee_status

@router.put("/employee-status/{employee_status_id}")
async def update_EmployeeStatus(employee_status_id: int, updated_employee_status: EmployeeStatus, session: AsyncSession = Depends(get_session)):
    existing_employee_status = await session.get(EmployeeStatus, employee_status_id)
    if existing_employee_status is None:
        raise HTTPException(status_code=404, employee_status="Статус сотрудника не найден")
    existing_employee_status.name = updated_employee_status.name
    await session.commit()
    await session.refresh(existing_employee_status)
    return existing_employee_status

@router.delete("/employee0status/{employee_status_id}")
async def delete_EmployeeStatus(employee_status_id: int, session: AsyncSession = Depends(get_session)):
    existing_employee_status = await session.get(EmployeeStatus, employee_status_id)
    if existing_employee_status is None:
        raise HTTPException(status_code=404, employee_status="Статус сотрудника не найден")
    try:
        await session.delete(existing_employee_status)
        await session.commit()
        return {"message": "Статус сотрудника успешно удален"}
    except Exception as e:
        print(f"Ошибка при удалении Статуса сотрудника: {e}")
        await session.rollback()  # Откат изменений в случае ошибки