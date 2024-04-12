from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    login: str
    password: str
    registration_at: datetime

    client: Optional["Client"] = Relationship(back_populates="user")
    employee: Optional["Employee"] = Relationship(back_populates="user")