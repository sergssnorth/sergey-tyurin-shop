from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class DeliveryInformation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    region: str
    city: str
    postal_code: str
    
    orders: List["Order"] = Relationship(back_populates="delivery_information")