from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

class Detail(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    name: str
    description: str
    
    models: List["Model"] = Relationship(back_populates="detail")
