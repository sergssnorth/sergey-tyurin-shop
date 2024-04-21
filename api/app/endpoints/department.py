from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Department
from app.db import get_session


from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, func, or_
from typing import List
from math import ceil
from pydantic import BaseModel


router = APIRouter()

class DepartmentResponseModel(BaseModel):
    total_count: int
    total_pages: int
    departments: List[Department]

@router.get("/departments", response_model=DepartmentResponseModel)
async def get_departments(offset: int = Query(0, ge=0),
                     limit: int = Query(50, gt=0),
                     search: str = Query(None),

                     sort_by: str = Query(None, description="Sort by 'name' or 'id'."),
                     order: str = Query("desc", description="Sort order: 'asc' or 'desc'."),

                     session: AsyncSession = Depends(get_session)):
    
    query = select(Department)

    if search:
        query = query.where(Department.name.ilike(f"%{search}%"))

    if sort_by and order:
        if sort_by == "name":
            query = query.order_by(Department.name.desc() if order == "desc" else Department.name.asc())
        elif sort_by == "id":
            query = query.order_by(Department.id.desc() if order == "desc" else Department.id.asc())
    else:
        #Сортировака по умолчанию
        query = query.order_by(Department.id.desc() if order == "desc" else Department.id.asc())

    total_count_query = select(func.count()).select_from(query)
    total_count_result = await session.execute(total_count_query)
    total_count = total_count_result.scalar()
    total_pages = ceil(total_count / limit)

    query = query.offset(offset).limit(limit)
    departments_result = await session.execute(query)
    departments = departments_result.scalars().all()

    return DepartmentResponseModel(
        total_count=total_count,
        total_pages=total_pages,
        departments=[
            Department(
                id=department.id,
                name=department.name
            ) for department in departments]
    )


@router.post("/department")
async def add_department(department: Department, session: AsyncSession = Depends(get_session)):
    new_department = Department(name=department.name)
    session.add(new_department)
    await session.commit()
    await session.refresh(new_department)
    return new_department

@router.put("/department/{department_id}")
async def update_Department(department_id: int, updated_department: Department, session: AsyncSession = Depends(get_session)):
    existing_department = await session.get(Department, department_id)
    if existing_department is None:
        raise HTTPException(status_code=404, department="Отдел не найден")
    existing_department.name = updated_department.name
    await session.commit()
    await session.refresh(existing_department)
    return existing_department

@router.delete("/department/{department_id}")
async def delete_Department(department_id: int, session: AsyncSession = Depends(get_session)):
    existing_department = await session.get(Department, department_id)
    if existing_department is None:
        raise HTTPException(status_code=404, department="Отдел не найден")
    try:
        await session.delete(existing_department)
        await session.commit()
        return {"message": "Отдел успешно удален"}
    except Exception as e:
        print(f"Ошибка при удалении Отдела: {e}")
        await session.rollback()  # Откат изменений в случае ошибки