from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from .client import Client
from .order_status import OrderStatus


class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    name: str
    slug: str
    client_id: Optional[int] = Field(default=None, foreign_key="client.id")
    order_status_id: Optional[int] = Field(default=None, foreign_key="orderstatus.id")

    client: Optional[Client] = Relationship(back_populates="orders")
    order_status: Optional[OrderStatus] = Relationship(back_populates="orders")