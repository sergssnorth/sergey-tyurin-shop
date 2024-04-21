from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

class Access(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    name: str
    
    role_accesses: List["RoleAccess"] = Relationship(back_populates="access")