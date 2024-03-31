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
    image1: HttpUrl
    image2: HttpUrl
    image3: HttpUrl
    image4: HttpUrl
    image5: HttpUrl
    image6: HttpUrl
    image7: HttpUrl
    image8: HttpUrl
    image9: HttpUrl
    image10: HttpUrl

class ProductCreateResponseModel(BaseModel):
    id: int
    model_id: int
    color_id: int
    image1: HttpUrl
    image2: HttpUrl
    image3: HttpUrl
    image4: HttpUrl
    image5: HttpUrl
    image6: HttpUrl
    image7: HttpUrl
    image8: HttpUrl
    image9: HttpUrl
    image10: HttpUrl

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



    products = [ProductResponseModel(
            id = product.id, 
            model_id = product.model_id,
            color_id = product.color_id,
            color_name= color.name,
            image1 = str(request.url_for('static', path=f"products/{os.path.basename(product.image1)}")),
            image2 = str(request.url_for('static', path=f"products/{os.path.basename(product.image2)}")),
            image3 = str(request.url_for('static', path=f"products/{os.path.basename(product.image3)}")),
            image4 = str(request.url_for('static', path=f"products/{os.path.basename(product.image4)}")),
            image5 = str(request.url_for('static', path=f"products/{os.path.basename(product.image5)}")),
            image6 = str(request.url_for('static', path=f"products/{os.path.basename(product.image6)}")),
            image7 = str(request.url_for('static', path=f"products/{os.path.basename(product.image7)}")),
            image8 = str(request.url_for('static', path=f"products/{os.path.basename(product.image8)}")),
            image9 = str(request.url_for('static', path=f"products/{os.path.basename(product.image9)}")),
            image10 = str(request.url_for('static', path=f"products/{os.path.basename(product.image10)}"))
        ) for product, color in products_and_colors]

    return JSONResponse(content=ProductListResponseModel(
        total_count=total_count,
        total_pages=total_pages,
        products=products
    ))


@router.post("/product", response_model=ProductCreateResponseModel)
async def add_product(
    request: Request,
    model_id: int = Form(...),
    color_id: int = Form(...),
    image1: UploadFile = File(...),
    image2: UploadFile = File(...),
    image3: UploadFile = File(...),
    image4: UploadFile = File(...),
    image5: UploadFile = File(...),
    image6: UploadFile = File(...),
    image7: UploadFile = File(...),
    image8: UploadFile = File(...),
    image9: UploadFile = File(...),
    image10: UploadFile = File(...),
    session: AsyncSession = Depends(get_session)):

    image_path = await save_image(image1)
    image_path = await save_image(image2)
    image_path = await save_image(image3)
    image_path = await save_image(image4)
    image_path = await save_image(image5)
    image_path = await save_image(image6)
    image_path = await save_image(image7)
    image_path = await save_image(image8)
    image_path = await save_image(image9)
    image_path = await save_image(image10)

    new_product = Product(model_id=model_id, 
                          color_id=color_id, 
                          image1=image1,
                          image2=image2,
                          image3=image3,
                          image4=image4,
                          image5=image5,
                          image6=image6,
                          image7=image7,
                          image8=image8,
                          image9=image9,
                          image10=image10,)
    session.add(new_product)
    await session.commit()
    await session.refresh(new_product)
    
    image_url1 = str(request.url_for('static', path=f"products/{image1.filename}"))
    image_url2 = str(request.url_for('static', path=f"products/{image2.filename}"))
    image_url3 = str(request.url_for('static', path=f"products/{image3.filename}"))
    image_url4 = str(request.url_for('static', path=f"products/{image4.filename}"))
    image_url5 = str(request.url_for('static', path=f"products/{image5.filename}"))
    image_url6 = str(request.url_for('static', path=f"products/{image6.filename}"))
    image_url7 = str(request.url_for('static', path=f"products/{image7.filename}"))
    image_url8 = str(request.url_for('static', path=f"products/{image8.filename}"))
    image_url9 = str(request.url_for('static', path=f"products/{image9.filename}"))
    image_url10 = str(request.url_for('static', path=f"products/{image10.filename}"))  # Настройте путь по мере необходимости

    return ProductCreateResponseModel(
        id=new_product.id,
        model_id=new_product.model_id,
        color_id=new_product.color_id,
        image1=image_url1,
        image2=image_url2,
        image3=image_url3,
        image4=image_url4,
        image5=image_url5,
        image6=image_url6,
        image7=image_url7,
        image8=image_url8,
        image9=image_url9,
        image10=image_url10,

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