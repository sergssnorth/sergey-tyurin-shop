from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from .order import Order
from .price_list_element import PriceListElement

class OrderElement(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    order_id: Optional[int] = Field(default=None, foreign_key="order.id")
    price_list_element_id: Optional[int] = Field(default=None, foreign_key="pricelistelement.id")

    order: Optional[Order] = Relationship(back_populates="order_elements")
    price_list_element: Optional[PriceListElement] = Relationship(back_populates="order_elements")
