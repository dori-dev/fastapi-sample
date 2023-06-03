from fastapi import (
    status,
    Depends,
    HTTPException,
    APIRouter,
)
from sqlalchemy.orm import Session
from sqlalchemy import or_

from schemas import users as schemas
from models import users as models
from utils import hash_password
from dependencies import get_db


router = APIRouter()


@router.post('/user/', response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(or_(
        models.User.email == user.email,
        models.User.username == user.username,
    )).first()
    if db_user:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            "Email or username already exists.",
        )
    hashed_password, salt = hash_password(user.password)
    user = models.User(
        email=user.email,
        username=user.username,
        hashed_password=hashed_password,
        salt=salt,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.get('/user/{user_id}', response_model=schemas.User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(
        models.User.id == user_id,
    ).first()
    if db_user is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found.")
    return db_user
