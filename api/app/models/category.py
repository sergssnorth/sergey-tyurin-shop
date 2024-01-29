from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from .big_category import BigCategory

class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    name: str
    slug: str
    models: List["Model"] = Relationship(back_populates="category")

    big_category_id: Optional[int] = Field(default=None, foreign_key="bigcategory.id")
    big_category: Optional[BigCategory] = Relationship(back_populates="categories")
    