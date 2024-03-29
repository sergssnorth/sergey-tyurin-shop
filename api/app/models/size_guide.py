from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

class SizeGuide(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    name: str
    image: str
    
    models: List["Model"] = Relationship(back_populates="size_guide")
