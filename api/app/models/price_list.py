from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

class PriceList(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    name: str
    created_at: datetime
    beginning_at: datetime
    completion_at: datetime

    price_list_elements: List["PriceListElement"] = Relationship(back_populates="price_list")
