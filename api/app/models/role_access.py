from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from .access import Access
from .role import Role

class RoleAccess(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    access_id: Optional[int] = Field(default=None, foreign_key="access.id")
    role_id: Optional[int] = Field(default=None, foreign_key="role.id")
    

    access: Optional[Access] = Relationship(back_populates="role_accesses")
    role: Optional[Role] = Relationship(back_populates="role_accesses")