from typing import List

from fastapi import APIRouter, HTTPException, status
from sqlmodel import select
from app.models.model import User, UserCreate, UserResponse
from app.core.database import SessionDep

router = APIRouter()

@router.post('/user', response_model=UserResponse)
async def create_user(user: UserCreate, session: SessionDep):
    db_user = User.model_validate(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@router.get('/user/{user_id}')
async def get_user(user_id: int, session: SessionDep):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
    return user

@router.get('/users', response_model=List[UserResponse])
async def get_users(session: SessionDep, skip: int = 0, limit: int = 100):
    users = session.exec(select(User).offset(skip).limit(limit)).all()
    return users