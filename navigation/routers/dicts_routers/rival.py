from navigation.nav.schemas import dicts as schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from navigation.nav.repository import dicts
from auth import database
router = APIRouter(
    prefix="/rival",
)

get_db = database.get_db


@router.post('/', response_model=schemas.RivalAdd)
def create_rival(request: schemas.RivalAdd, db: Session = Depends(get_db)):
    return dicts.create_rival(db, request)


@router.delete('/{id}')
def delete_rival(id: int, db: Session = Depends(get_db)):
    return dicts.delete_rival(db, id)


@router.get('/{id}', response_model=schemas.RivalAdd)
def get_rival(id: int, db: Session = Depends(get_db)):
    return dicts.get_rival(db, id)


@router.get('/')
def get_rivals(db: Session = Depends(get_db)):
    return dicts.get_rivals(db)
