from auth.login import models
from auth.auth import login
from fastapi import APIRouter
from auth.login.schemas import login as schemas
from auth.login.models import login as models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from auth.login.repository import login as user
from auth import database

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', response_model=schemas.UserCreate)
def create_user(request: schemas.UserCreate, db: Session = Depends(get_db)):
    return user.create_user(db, request)

@router.put('/', response_model=schemas.UserCreate)
def update_user(request: schemas.UserCreate, db: Session = Depends(get_db)):
    return user.update_user(db, request)

@router.delete('/{id}')
def delete_user(id: int, db: Session = Depends(get_db)):
    return user.delete_user(db, id)


@router.get('/{id}', response_model=schemas.User)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user(db, id)


@router.get('/')
def get_users(db: Session = Depends(get_db)):
    return user.get_users(db)
