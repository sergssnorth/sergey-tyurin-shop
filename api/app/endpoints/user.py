from datetime import datetime
from math import ceil
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import User
from app.db import get_session

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, func, or_
from typing import List
from math import ceil
from pydantic import BaseModel

router = APIRouter()

class UserResponseModel(BaseModel):
    total_count: int
    total_pages: int
    users: List[User]

@router.get("/users", response_model=UserResponseModel)
async def get_users(offset: int = Query(0, ge=0),
                    limit: int = Query(50, gt=0),
                    search: str = Query(None),
                    
                    sort_by: str = Query(None, description="Sort by 'name' or 'id'."),
                    order: str = Query("desc", description="Sort order: 'asc' or 'desc'."),
                    
                    session: AsyncSession = Depends(get_session)):

    query = select(User)

    if search:
        query = query.filter(or_(
            User.name.ilike(f"%{search}%")
        ))

    if sort_by and order:
        if sort_by == "name":
            query = query.order_by(User.name.desc() if order == "desc" else User.name.asc())
        elif sort_by == "id":
            query = query.order_by(User.id.desc() if order == "desc" else User.id.asc())
    else:
        #Сортировака по умолчанию
        query = query.order_by(User.id.desc() if order == "desc" else User.id.asc())

    total_count_query = select(func.count()).select_from(query)
    total_count_result = await session.execute(total_count_query)
    total_count = total_count_result.scalar()
    total_pages = ceil(total_count / limit)


    query = query.offset(offset).limit(limit)
    user_result = await session.execute(query)
    users = user_result.scalars().all()

    return UserResponseModel(
        total_count=total_count,
        total_pages=total_pages,
        users=[
            User(
                id=user.id,
                login=user.login,
                password=user.password,
                email=user.email,
                registration_at=user.registration_at,
            ) for user in users
        ]
    )



@router.post("/user")
async def add_user(user: User, session: AsyncSession = Depends(get_session)):
    new_user = User(
        login=user.login,
        password=user.password,
        email=user.email,
        registration_at = datetime.now()
    )
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user

@router.put("/user/{user_id}")
async def update_client(user_id: int, updated_user: User, session: AsyncSession = Depends(get_session)):
    existing_user = await session.get(User, user_id)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    
    existing_user.login = updated_user.login
    existing_user.password = updated_user.password
    existing_user.email = updated_user.email
    
    await session.commit()
    await session.refresh(existing_user)
    return existing_user

@router.delete("/user/{user_id}")
async def delete_user(user_id: int, session: AsyncSession = Depends(get_session)):
    user = await session.get(User, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    try:
        await session.delete(user)
        await session.commit()
        return {"message": "Пользователь успешно удален"}
    except Exception as e:
        print(f"Ошибка при удалении Пользователя: {e}")
        await session.rollback()  # Откат изменений в случае ошибки