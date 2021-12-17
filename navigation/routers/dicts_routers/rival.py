from sqlalchemy import schema
from navigation.nav.schemas import dicts as schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from navigation.nav.repository import dicts
from auth import database
from typing import List
router = APIRouter(
    prefix="/rival",
)

get_db = database.get_db


@router.post('/', response_model=schemas.RivalAdd)
def create_rival(request: schemas.RivalAdd, db: Session = Depends(get_db)):
    return dicts.create_rival(db, request)


@router.put('/', response_model=schemas.RivalAdd)
def update_rival(request: schemas.RivalAdd, db: Session = Depends(get_db)):
    return dicts.update_rival(db, request)


@router.delete('/{id}')
def delete_rival(id: int, db: Session = Depends(get_db)):
    return dicts.delete_rival(db, id)


@router.get('/{id}', response_model=schemas.RivalShow)
def get_rival(id: int, db: Session = Depends(get_db)):
    return dicts.get_rival(db, id)


@router.get('/', response_model=List[schemas.RivalShow])
def get_rivals(db: Session = Depends(get_db)):
    return dicts.get_rivals(db)
