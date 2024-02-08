from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from .model import Model
from .color import Color

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    model_id: Optional[int] = Field(default=None, foreign_key="model.id")
    color_id: Optional[int] = Field(default=None, foreign_key="color.id")

    model: Optional[Model] = Relationship(back_populates="products")
    color: Optional[Color] = Relationship(back_populates="products")

    product_sizes: List["ProductSize"] = Relationship(back_populates="product")