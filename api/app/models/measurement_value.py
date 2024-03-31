from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from .size import Size
from .measurement_type import MeasurementType

class MeasurementValue(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    size_id: int = Field(foreign_key="size.id")
    measurement_type_id: int = Field(foreign_key="measurementtype.id")
    value: float  # Значение измерения

    size: Size = Relationship(back_populates="measurement_values")
    measurement_type: Optional[MeasurementType] = Relationship(back_populates="measurement_values")
