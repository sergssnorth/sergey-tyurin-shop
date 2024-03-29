from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from pydantic import EmailStr, validator 
from datetime import datetime

class Client(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    name: str
    phone: str
    email: str 
    created_at: datetime

    orders: List["Order"] = Relationship(back_populates="client")

    # Валидатор для проверки формата телефонного номера
    @validator('phone')
    def validate_phone(cls, value):
        import re
        if not re.match(r'^\+?7?\d{9,15}$', value):
            raise ValueError("Неверный формат телефонного номера")
        return value

    # Валидатор для проверки email
    @validator('email')
    def validate_email(cls, value):
        return EmailStr.validate(value)
    