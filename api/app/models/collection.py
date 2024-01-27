from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from .big_category import BigCategory
from datetime import datetime

class Collection(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    name: str
    slug: str
    description: str
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)
    products: List["Product"] = Relationship(back_populates="collection")
