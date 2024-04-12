from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from .user import User
from .employee_status import EmployeeStatus
from .department import Department


class Employee(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    employee_status_id: Optional[int] = Field(default=None, foreign_key="employeestatus.id")
    department_id: Optional[int] = Field(default=None, foreign_key="department.id")
    employment_at: datetime
    employment_end: datetime

    user: Optional[User] = Relationship(back_populates="employee")
    employee_status: Optional[EmployeeStatus] = Relationship(back_populates="employees")
    department: Optional[Department] = Relationship(back_populates="employees")

    orders: List["Order"] = Relationship(back_populates="employee")
