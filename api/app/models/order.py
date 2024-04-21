from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from .user import User
from .employee import Employee
from .order_status import OrderStatus



class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    name: str
    sname: str
    lname: str
    phone: str
    email: str
    region: str
    city: str
    postal_code: str
    employee_id: Optional[int] = Field(default=None, foreign_key="employee.id")
    order_status_id: int = Field(default=None, foreign_key="orderstatus.id")

    created_at: datetime
    updated_at: Optional[datetime]

    order_elements: List["OrderElement"] = Relationship(back_populates="order")

    user: Optional[User] = Relationship(back_populates="orders")
    employee: Optional[Employee] = Relationship(back_populates="orders")
    order_status: Optional[OrderStatus] = Relationship(back_populates="orders")