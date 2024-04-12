from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from .price_list import PriceList
from .product_instance import ProductInstance

class PriceListElement(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    price_list_id: Optional[int] = Field(default=None, foreign_key="pricelist.id")
    product_instance_id: Optional[int] = Field(default=None, foreign_key="productinstance.id")

    order_elements: List["OrderElement"] = Relationship(back_populates="price_list_element")

    price_list: Optional[PriceList] = Relationship(back_populates="price_list_elements")
    product_instances: Optional[ProductInstance] = Relationship(back_populates="price_list_elements")
