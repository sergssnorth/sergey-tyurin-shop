from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Client(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    name: str
    slug: str

    orders: List["Order"] = Relationship(back_populates="client")