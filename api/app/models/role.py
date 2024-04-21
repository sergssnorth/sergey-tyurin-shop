from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

class Role(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    name: str
    
    role_accesses: List["RoleAccess"] = Relationship(back_populates="role")
    empolyee_roles: List["EmployeeRole"] = Relationship(back_populates="role")