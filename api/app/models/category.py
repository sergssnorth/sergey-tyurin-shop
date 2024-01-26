from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class BigCategory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    name: str
    slug: str
    categories: List["Category"] = Relationship(back_populates="big_category")

class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    name: str
    slug: str
    big_category_id: Optional[int] = Field(default=None, foreign_key="bigcategory.id")
    big_category: Optional[BigCategory] = Relationship(back_populates="categories")