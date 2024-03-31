import os
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_session

from fastapi.staticfiles import StaticFiles
from fastapi import APIRouter, Depends, Form, HTTPException, Query, UploadFile, File, Request
from fastapi.responses import JSONResponse
from sqlmodel import select, and_, join, or_, func
from typing import List
from math import ceil
from pydantic import BaseModel, HttpUrl
from app.models import SizeGuide

router = APIRouter()

class SizeGuideCreate(BaseModel):
    name: str


# Это модель, которую вы использовали бы для ответа клиенту,
# включая URL изображения, которое было загружено
class SizeGuideResponse(BaseModel):
    id: int
    name: str
    image: HttpUrl

class SizeGuideListResponse(BaseModel):
    total_count: int
    total_pages: int
    size_guides: List[SizeGuideResponse]

# Папка для изображений
static_path = os.path.join('static', 'images')
os.makedirs(static_path, exist_ok=True)  # Создаем папку, если она не существует

# Предположим, у нас есть функция для сохранения файлов, которая возвращает путь к файлу
async def save_image(image: UploadFile) -> str:
    file_location = os.path.join(static_path, image.filename)
    with open(file_location, "wb+") as file_object:
        file_object.write(await image.read())  # Используйте 'await' с 'image.read()'
    return file_location

@router.get("/size-guides", response_model=SizeGuideListResponse)
async def get_size_guides(
    request: Request,
    offset: int = Query(0, ge=0),
    limit: int = Query(10, gt=0),
    session: AsyncSession = Depends(get_session)) -> JSONResponse:

    total_query = select(func.count(SizeGuide.id))
    total_count_result = await session.execute(total_query)
    total_count = total_count_result.scalar_one()

    query = select(SizeGuide).offset(offset).limit(limit)
    results = await session.execute(query)
    size_guides = results.scalars().all()

    total_pages = ceil(total_count / limit)

    # Преобразование экземпляров SizeGuide в SizeGuideResponse
    size_guide_responses = [
        {
            "id": guide.id,
            "name": guide.name,
            "image": str(request.url_for('static', path=f"images/{os.path.basename(guide.image)}"))
        } for guide in size_guides
    ]

    response = {
        "total_count": total_count,
        "total_pages": total_pages,
        "size_guides": size_guide_responses
    }

    return JSONResponse(content=response)

@router.post("/size-guide", response_model=SizeGuideResponse)
async def create_size_guide(
    request: Request,
    name: str = Form(...),  # Принимаем name как часть формы
    image: UploadFile = File(...),
    session: AsyncSession = Depends(get_session)
    ):

    image_path = await save_image(image)
    db_size_guide = SizeGuide(name=name, image=image_path)
    session.add(db_size_guide)
    await session.commit()
    await session.refresh(db_size_guide)
    
    # Правильное создание URL для изображения с использованием 'url_for'
    image_url = str(request.url_for('static', path=f"images/{image.filename}"))  # Настройте путь по мере необходимости

    return SizeGuideResponse(
        id=db_size_guide.id,
        name=db_size_guide.name,
        image=image_url
    )

@router.put("/size-guide/{size_guide_id}", response_model=SizeGuideResponse)
async def update_size_guide(
    size_guide_id: int,
    request: Request,
    name: Optional[str] = Form(None),  # Имя необязательно к обновлению
    image: Optional[UploadFile] = File(None),  # Изображение тоже необязательно
    session: AsyncSession = Depends(get_session)
):
    async with session.begin():
        # Пытаемся найти существующую размерную сетку
        db_size_guide = await session.get(SizeGuide, size_guide_id)
        if not db_size_guide:
            raise HTTPException(status_code=404, detail=f"SizeGuide with ID {size_guide_id} not found")

        # Обновляем имя, если оно предоставлено
        if name is not None:
            db_size_guide.name = name

        # Если предоставлено новое изображение, сохраняем его и обновляем путь к изображению в базе данных
        if image:
            image_path = await save_image(image)
            db_size_guide.image = image_path

        # Не нужно явно добавлять объект обратно, так как изменения уже отслеживаются
        await session.commit()

    # Генерируем новый URL для изображения (или используем существующий)
    image_url = str(request.url_for('static', path=f"images/{os.path.basename(db_size_guide.image)}"))

    return SizeGuideResponse(
        id=db_size_guide.id,
        name=db_size_guide.name,
        image=image_url
    )
