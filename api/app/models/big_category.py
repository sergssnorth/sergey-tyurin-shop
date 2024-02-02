from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class BigCategory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    name: str
    slug: str
    categories: List["Category"] = Relationship(back_populates="big_category", sa_relationship_kwargs={"cascade": "all,delete,delete-orphan"})
