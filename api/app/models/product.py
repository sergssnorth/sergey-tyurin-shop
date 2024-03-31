from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from .model import Model
from .color import Color

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    model_id: Optional[int] = Field(default=None, foreign_key="model.id")
    color_id: Optional[int] = Field(default=None, foreign_key="color.id")
    image1: Optional[str]  # Путь к изображению размерной сетки
    image2: Optional[str]  # Путь к изображению размерной сетки
    image3: Optional[str]  # Путь к изображению размерной сетки
    image4: Optional[str]  # Путь к изображению размерной сетки
    image5: Optional[str]  # Путь к изображению размерной сетки
    image6: Optional[str]  # Путь к изображению размерной сетки
    image7: Optional[str]  # Путь к изображению размерной сетки
    image8: Optional[str]  # Путь к изображению размерной сетки
    image9: Optional[str]  # Путь к изображению размерной сетки
    image10: Optional[str]  # Путь к изображению размерной сетки


    model: Optional[Model] = Relationship(back_populates="products")
    color: Optional[Color] = Relationship(back_populates="products")

    product_sizes: List["ProductSize"] = Relationship(back_populates="product")