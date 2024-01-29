from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from .product import Product


class Warehouse(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    name: str
    description: str
