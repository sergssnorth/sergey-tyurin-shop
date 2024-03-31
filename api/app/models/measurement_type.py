from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from .size_guide import SizeGuide

class MeasurementType(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    size_guide_id: int = Field(foreign_key="sizeguide.id")
    name: str  # Название типа измерения, например "chest", "length", "sleeve"
    
    size_guide: Optional[SizeGuide] = Relationship(back_populates="measurement_types")
    measurement_values: List["MeasurementValue"] = Relationship(back_populates="measurement_type")
