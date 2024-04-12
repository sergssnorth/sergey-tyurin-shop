from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from .client import Client
from .employee import Employee
from .order_status import OrderStatus
from .delivery_information import DeliveryInformation


class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    client_id: Optional[int] = Field(default=None, foreign_key="client.id")
    employee_id: Optional[int] = Field(default=None, foreign_key="employee.id")
    order_status_id: Optional[int] = Field(default=None, foreign_key="orderstatus.id")
    delivery_information_id: Optional[int] = Field(default=None, foreign_key="deliveryinformation.id")
    created_at: datetime
    updated_at: datetime

    order_elements: List["OrderElement"] = Relationship(back_populates="order")

    client: Optional[Client] = Relationship(back_populates="orders")
    employee: Optional[Employee] = Relationship(back_populates="orders")
    order_status: Optional[OrderStatus] = Relationship(back_populates="orders")
    delivery_information: Optional[DeliveryInformation] = Relationship(back_populates="orders")