from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


class Warehouse(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    name: str

    warehouse_elements: List["WarehouseElement"] = Relationship(back_populates="warehouse")
