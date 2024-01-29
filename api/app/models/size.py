from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Size(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    name: str
    slug: str

    products: List["Product"] = Relationship(back_populates="size")
