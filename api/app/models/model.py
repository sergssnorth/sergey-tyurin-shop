from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from .category import Category
from .collection import Collection

class Model(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    name: str
    slug: str
    description: str
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")
    collection_id: Optional[int] = Field(default=None, foreign_key="collection.id")
    products: List["Product"] = Relationship(back_populates="model")

    category: Optional[Category] = Relationship(back_populates="models")
    collection: Optional[Collection] = Relationship(back_populates="models")