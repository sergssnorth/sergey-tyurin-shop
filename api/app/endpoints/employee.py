from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Employee
from app.db import get_session
from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, func, or_
from typing import List
from math import ceil
from pydantic import BaseModel


router = APIRouter()

class EmployeeResponseModel(BaseModel):
    total_count: int
    total_pages: int
    employees: List[Employee]

@router.get("/employees", response_model=EmployeeResponseModel)
async def get_employees(offset: int = Query(0, ge=0),
                     limit: int = Query(50, gt=0),
                     search: str = Query(None),

                     employee_status_id: Optional[int] = None,
                     department_id: Optional[int] = None,

                     sort_by: str = Query(None, description="Sort by 'name' or 'id'."),
                     order: str = Query("desc", description="Sort order: 'asc' or 'desc'."),

                     session: AsyncSession = Depends(get_session)):
    
    query = select(Employee)

    if search:
        query = query.where(Employee.name.ilike(f"%{search}%"))

    if employee_status_id is not None:
        query = query.filter(Employee.employee_status_id == employee_status_id)

    if department_id is not None:
        query = query.filter(Employee.department_id == department_id)

    if sort_by and order:
        if sort_by == "name":
            query = query.order_by(Employee.name.desc() if order == "desc" else Employee.name.asc())
        elif sort_by == "id":
            query = query.order_by(Employee.id.desc() if order == "desc" else Employee.id.asc())
    else:
        #Сортировака по умолчанию
        query = query.order_by(Employee.id.desc() if order == "desc" else Employee.id.asc())

    total_count_query = select(func.count()).select_from(query)
    total_count_result = await session.execute(total_count_query)
    total_count = total_count_result.scalar()
    total_pages = ceil(total_count / limit)

    query = query.offset(offset).limit(limit)
    employees_result = await session.execute(query)
    employees = employees_result.scalars().all()

    return EmployeeResponseModel(
        total_count=total_count,
        total_pages=total_pages,
        employees=[
            Employee(
                id=employee.id,
                user_id=employee.user_id,
                name=employee.name,
                sname=employee.sname,
                employee_status_id=employee.employee_status_id,
                department_id=employee.department_id,
                employment_at=employee.employment_at,
                employment_end=employee.employment_end,
            ) for employee in employees]
    )


@router.post("/employee")
async def add_employee(employee: Employee, session: AsyncSession = Depends(get_session)):
    new_employee = Employee(user_id=employee.user_id,
                            name=employee.name,
                            sname=employee.sname,
                            employee_status_id=employee.employee_status_id,
                            department_id=employee.department_id,
                            employment_at = datetime.now())
    session.add(new_employee)
    await session.commit()
    await session.refresh(new_employee)
    return new_employee

@router.put("/employee/{employee_id}")
async def update_Employee(employee_id: int, updated_employee: Employee, session: AsyncSession = Depends(get_session)):
    existing_employee = await session.get(Employee, employee_id)
    if existing_employee is None:
        raise HTTPException(status_code=404, employee="Сотрудник не найден")
    existing_employee.user_id = updated_employee.user_id
    existing_employee.name = updated_employee.name
    existing_employee.sname = updated_employee.sname
    existing_employee.employee_status_id = updated_employee.employee_status_id
    existing_employee.department_id = updated_employee.department_id
    existing_employee.employment_end = updated_employee.employment_end
    await session.commit()
    await session.refresh(existing_employee)
    return existing_employee

@router.delete("/employee/{employee_id}")
async def delete_Employee(employee_id: int, session: AsyncSession = Depends(get_session)):
    existing_employee = await session.get(Employee, employee_id)
    if existing_employee is None:
        raise HTTPException(status_code=404, employee="Сотрудник не найден")
    try:
        await session.delete(existing_employee)
        await session.commit()
        return {"message": "Сотрудник успешно удален"}
    except Exception as e:
        print(f"Ошибка при удалении Сотрудника: {e}")
        await session.rollback()  # Откат изменений в случае ошибки