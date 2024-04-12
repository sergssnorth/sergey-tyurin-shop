from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from .user import User

class Client(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    email: str
    name: str
    sname: Optional[str] = Field(nullable=True)
    phone: str

    user: Optional[User] = Relationship(back_populates="client")

    orders: List["Order"] = Relationship(back_populates="client")
