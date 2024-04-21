from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from .employee import Employee
from .role import Role

class EmployeeRole(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    role_id: Optional[int] = Field(default=None, foreign_key="role.id")
    employee_id: Optional[int] = Field(default=None, foreign_key="employee.id")
    
    role: Optional[Role] = Relationship(back_populates="empolyee_roles")
    employee: Optional[Employee] = Relationship(back_populates="empolyee_roles")
    