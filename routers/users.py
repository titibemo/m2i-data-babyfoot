
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from models.users import User, UserRole
from models.schemas import UserRegister, UserPublic, GetUser
from db import user_db
from core.database import get_db
from services.users import get_user_by_username, create_user, delete_user_by_id, update_user_by_id

from sqlalchemy.orm import Session



router = APIRouter(prefix="/users", tags=["Users"])

@router.post("", response_model=UserRegister, status_code=status.HTTP_201_CREATED)
async def create_new_user(payload: UserRegister, db: Session = Depends(get_db)):


    existing_user = get_user_by_username(db, payload.username)
    if existing_user is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ce nom d'utilisateur existe déjà.",
        )

    created_user = create_user(
        db=db,
        username=payload.username,
        password=payload.password,
        role=UserRole.USER.value,
    )

    return created_user


@router.get("/by-username", response_model=UserPublic)
async def get_user(username: str, db: Session = Depends(get_db) ):
    user = get_user_by_username(db, username)
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    await delete_user_by_id(db, user_id)
    return {"detail": "Utilisateur supprimé"}

@router.put("/{user_id}")
async def update_user(user_id: int, payload: UserRegister, db: Session = Depends(get_db)):
    update_user_by_id(db, user_id, payload.username, payload.password)
    return {"detail": "Utilisateur modifié"}