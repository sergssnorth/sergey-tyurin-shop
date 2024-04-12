from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from .warehouse import Warehouse
from .product_instance import ProductInstance

class WarehouseElement(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    warehouse_id: Optional[int] = Field(default=None, foreign_key="warehouse.id")
    product_instance_id: Optional[int] = Field(default=None, foreign_key="productinstance.id")
    count: Optional[int]

    warehouse: Optional[Warehouse] = Relationship(back_populates="warehouse_elements")
    product_instances: Optional[ProductInstance] = Relationship(back_populates="warehouse_element")