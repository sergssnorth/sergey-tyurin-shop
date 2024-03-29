import datetime
from math import ceil
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Client
from app.db import get_session

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, func, or_
from typing import List
from math import ceil
from pydantic import BaseModel

router = APIRouter()

class ClientsResponseModel(BaseModel):
    total_count: int
    total_pages: int
    clients: List[Client]

@router.get("/clients", response_model=ClientsResponseModel)
async def get_clients(offset: int = Query(0, ge=0),
                    limit: int = Query(50, gt=0),
                    search: str = Query(None),
                    client_id: int = Query(None),
                    
                    sort_by: str = Query(None, description="Sort by 'name' or 'id'."),
                    order: str = Query("desc", description="Sort order: 'asc' or 'desc'."),
                    
                    session: AsyncSession = Depends(get_session)):

    query = select(Client)

    if search:
        query = query.filter(or_(
            Client.name.ilike(f"%{search}%")
        ))

    if client_id:
        query = query.filter(Client.id == client_id)

    if sort_by and order:
        if sort_by == "name":
            query = query.order_by(Client.name.desc() if order == "desc" else Client.name.asc())
        elif sort_by == "id":
            query = query.order_by(Client.id.desc() if order == "desc" else Client.id.asc())
    else:
        #Сортировака по умолчанию
        query = query.order_by(Client.id.desc() if order == "desc" else Client.id.asc())

    total_count_query = select(func.count()).select_from(query)
    total_count_result = await session.execute(total_count_query)
    total_count = total_count_result.scalar()
    total_pages = ceil(total_count / limit)


    query = query.offset(offset).limit(limit)
    client_result = await session.execute(query)
    clients = client_result.scalars().all()

    return ClientsResponseModel(
        total_count=total_count,
        total_pages=total_pages,
        clients=[
            Client(
                id=client.id,
                name=client.name,
                phone=client.phone,
                email=client.email,
                created_at=client.created_at
            ) for client in clients
        ]
    )



@router.post("/client")
async def add_client(client: Client, session: AsyncSession = Depends(get_session)):
    new_client = Client(
        name=client.name,
        phone=client.phone,
        email=client.email,
        created_at=datetime.datetime.now() # Убедитесь, что это поле устанавливается автоматически, если необходимо
    )
    session.add(new_client)
    await session.commit()
    await session.refresh(new_client)
    return new_client

@router.put("/client/{client_id}")
async def update_client(client_id: int, updated_client: Client, session: AsyncSession = Depends(get_session)):
    existing_client = await session.get(Client, client_id)
    if existing_client is None:
        raise HTTPException(status_code=404, detail="Клиент не найден")
    
    existing_client.name = updated_client.name
    existing_client.phone = updated_client.phone
    existing_client.email = updated_client.email
    
    await session.commit()
    await session.refresh(existing_client)
    return existing_client

@router.delete("/client/{client_id}")
async def delete_client(client_id: int, session: AsyncSession = Depends(get_session)):
    client = await session.get(Client, client_id)
    if client is None:
        raise HTTPException(status_code=404, detail="Клиент не найден")
    try:
        await session.delete(client)
        await session.commit()
        return {"message": "Клиент успешно удален"}
    except Exception as e:
        print(f"Ошибка при удалении Заказа: {e}")
        await session.rollback()  # Откат изменений в случае ошибки