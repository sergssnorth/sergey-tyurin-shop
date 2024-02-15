from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Client
from app.db import get_session
from sqlmodel import select


router = APIRouter()


@router.get("/clients", response_model=list[Client])
async def get_clients(
    page: int = Query(1, gt=0),  # Номер страницы, начиная с 1
    page_size: int = Query(10, gt=0),
    session: AsyncSession = Depends(get_session)):
    
    start_index = (page - 1) * page_size

    result = await session.execute(select(Client).offset(start_index).limit(page_size))

    clients = result.scalars().all()
    return [Client(id=client.id, name=client.name, slug=client.slug) for client in clients]

@router.post("/client")
async def add_client(client: Client, session: AsyncSession = Depends(get_session)):
    new_client = Client(name=client.name, slug=client.slug,)
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
    existing_client.slug = updated_client.slug
    
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