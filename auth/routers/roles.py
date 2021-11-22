import re
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
    prefix="/roles",
    tags=['Roles']
)

get_db = database.get_db


@router.post('/', response_model=schemas.Role)
def create_role(request: schemas.RoleCreate, db: Session = Depends(get_db)):
    return user.create_roles(db, request)

@router.put('/', response_model=schemas.Role)
def update_role(request: schemas.RoleCreate, db: Session = Depends(get_db)):
    return user.update_role(db, request)

@router.get('/{id}', response_model=schemas.Role)
def show_role(id: int, db: Session = Depends(get_db)):
    return user.get_role(db, id)


@router.get('/')
def show_roles(db: Session = Depends(get_db)):
    return user.get_roles(db)


@router.delete('/{id}')
def delete_role(id: int, db: Session = Depends(get_db)):
    return user.delete_role(db, id)
