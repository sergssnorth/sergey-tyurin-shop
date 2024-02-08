from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from .product import Product
from .size import Size

class ProductSize(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    product_id: Optional[int] = Field(default=None, foreign_key="product.id")
    size_id: Optional[int] = Field(default=None, foreign_key="size.id")

    product: Optional[Product] = Relationship(back_populates = "product_sizes")
    size: Optional[Size] = Relationship(back_populates="product_sizes")