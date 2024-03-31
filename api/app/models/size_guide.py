from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

class SizeGuide(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    name: str  # Например, "Мужские футболки"
    image: str  # Путь к изображению размерной сетки
    
    models: List["Model"] = Relationship(back_populates="size_guide")
    measurement_types: List["MeasurementType"] = Relationship(back_populates="size_guide")