from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


class Department(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    name: str

    employees: List["Employee"] = Relationship(back_populates="department")
