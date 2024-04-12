import os
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Product, Color
from app.db import get_session
from fastapi.responses import JSONResponse

from fastapi import APIRouter, Depends,Form, HTTPException, Query, UploadFile, File, Request
from sqlmodel import select, and_, join, or_, func
from typing import List
from math import ceil
from pydantic import BaseModel, HttpUrl
router = APIRouter()

class ProductResponseModel(BaseModel):
    id: int
    model_id: int
    color_id: int
    color_name: str
    image1: Optional[str] = None
    image2: Optional[str] = None
    image3: Optional[str] = None
    image4: Optional[str] = None
    image5: Optional[str] = None
    image6: Optional[str] = None
    image7: Optional[str] = None
    image8: Optional[str] = None
    image9: Optional[str] = None
    image10: Optional[str] = None

class ProductCreateResponseModel(BaseModel):
    id: int
    model_id: int
    color_id: int
    image1: Optional[str]
    image2: Optional[str]
    image3: Optional[str]
    image4: Optional[str]
    image5: Optional[str]
    image6: Optional[str]
    image7: Optional[str]
    image8: Optional[str]
    image9: Optional[str]
    image10: Optional[str]

class ProductListResponseModel(BaseModel):
    total_count: int
    total_pages: int
    products: List[ProductResponseModel]

static_path = os.path.join('static', 'products')
os.makedirs(static_path, exist_ok=True)  # Создаем папку, если она не существует

# Предположим, у нас есть функция для сохранения файлов, которая возвращает путь к файлу
async def save_image(image: UploadFile) -> str:
    file_location = os.path.join(static_path, image.filename)
    with open(file_location, "wb+") as file_object:
        file_object.write(await image.read())  # Используйте 'await' с 'image.read()'
    return file_location


@router.get("/products", response_model=ProductListResponseModel)
async def get_products(request: Request,
                       
                       offset: int = Query(0, ge=0),
                       limit: int = Query(50, gt=0),
                       search: str = Query(None),
                       model_id: Optional[int] = None, 
                       session: AsyncSession = Depends(get_session)):
    
    query = select(Product, Color).join(Color)

    if search:
        query = query.filter(or_(
            Color.name.ilike(f"%{search}%")
        ))    

    if model_id is not None:
        query = query.filter(Product.model_id == model_id)
                   
    total_count_query = select(func.count()).select_from(query)
    total_count_result = await session.execute(total_count_query)
    total_count = total_count_result.scalar()
    total_pages = ceil(total_count / limit)

    query = query.offset(offset).limit(limit)
    products_and_colors = await session.execute(query)

    products = []
    for product, color in products_and_colors:
        product_dict = {
            'id': product.id,
            'model_id': product.model_id,
            'color_id': product.color_id,
            'color_name': color.name
        }
        # Добавляем только существующие изображения
        for i in range(1, 11):
            image_attr = getattr(product, f"image{i}", None)
            if image_attr:
                product_dict[f"image{i}"] = str(request.url_for('static', path=f"products/{os.path.basename(image_attr)}"))
        products.append(ProductResponseModel(**product_dict))

    return ProductListResponseModel(
        total_count=total_count,
        total_pages=total_pages,
        products=products
    )


@router.post("/product", response_model=ProductCreateResponseModel)
async def add_product(
    request: Request,
    model_id: int = Form(...),
    color_id: int = Form(...),
    image1: Optional[UploadFile] = File(None),
    image2: Optional[UploadFile] = File(None),
    image3: Optional[UploadFile] = File(None),
    image4: Optional[UploadFile] = File(None),
    image5: Optional[UploadFile] = File(None),
    image6: Optional[UploadFile] = File(None),
    image7: Optional[UploadFile] = File(None),
    image8: Optional[UploadFile] = File(None),
    image9: Optional[UploadFile] = File(None),
    image10: Optional[UploadFile] = File(None),
    session: AsyncSession = Depends(get_session)):

    # Сохранение всех изображений и получение их URL-адресов
    image_urls = {}
    for image_name, image_file in [
        ("image1", image1),
        ("image2", image2),
        ("image3", image3),
        ("image4", image4),
        ("image5", image5),
        ("image6", image6),
        ("image7", image7),
        ("image8", image8),
        ("image9", image9),
        ("image10", image10)
    ]:
        if image_file:
            # Сохранение изображения
            image_path = await save_image(image_file)
            # Формирование URL-адреса
            image_url = str(request.url_for('static', path=f"products/{os.path.basename(image_path)}"))
            # Добавление URL-адреса в словарь
            image_urls[image_name] = image_url
        else:
            # Если изображение не предоставлено, устанавливаем значение по умолчанию None
            image_urls[image_name] = None

    # Создание нового продукта с указанием всех URL-адресов изображений
    new_product = Product(
        model_id=model_id, 
        color_id=color_id, 
        **{f"image{i}": getattr(image_file, "filename", None) for i, image_file in enumerate([image1, image2, image3, image4, image5, image6, image7, image8, image9, image10], start=1)}
    )
    session.add(new_product)
    await session.commit()
    await session.refresh(new_product)

    # Возвращение созданного продукта вместе с URL-адресами изображений
    return ProductCreateResponseModel(
        id=new_product.id,
        model_id=new_product.model_id,
        color_id=new_product.color_id,
        **image_urls
    )


@router.put("/product/{product_id}")
async def update_product(product_id: int, updated_product: Product, session: AsyncSession = Depends(get_session)):
    existing_product = await session.get(Product, product_id)
    if existing_product is None:
        raise HTTPException(status_code=404, detail="Продукт не найден")
    existing_product.model_id = updated_product.model_id
    existing_product.color_id = updated_product.color_id
    await session.commit()
    await session.refresh(existing_product)
    return existing_product

@router.delete("/product/{product_id}")
async def delete_product(product_id: int, session: AsyncSession = Depends(get_session)):
    product = await session.get(Product, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Продукт не найден")
    try:
        await session.delete(product)
        await session.commit()
        return {"message": "Продукт успешно удален"}
    except Exception as e:
        print(f"Ошибка при удалении Продукта: {e}")
        await session.rollback()  # Откат изменений в случае ошибки