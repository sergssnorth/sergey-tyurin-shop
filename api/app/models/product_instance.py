from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from .product import Product
from .size import Size


class ProductInstance(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    product_id: int = Field(default=None, foreign_key="product.id")
    size_id: int = Field(default=None, foreign_key="size.id")

    price_list_elements: List["PriceListElement"] = Relationship(back_populates="product_instances")
    warehouse_element: Optional["WarehouseElement"] = Relationship(back_populates="product_instances")

    product: Optional[Product] = Relationship(back_populates="product_instances")
    size: Optional[Size] = Relationship(back_populates="product_instances")