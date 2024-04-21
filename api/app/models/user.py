from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    login: str
    password: str
    email: str
    registration_at: datetime

    employee: Optional["Employee"] = Relationship(back_populates="user")

    orders: List["Order"] = Relationship(back_populates="user")