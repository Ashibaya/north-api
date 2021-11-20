from navigation.nav.schemas import dicts as schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from navigation.nav.repository import dicts
from auth import database

router = APIRouter(
    prefix="/locality"
)

get_db = database.get_db


@router.post('/', response_model=schemas.LocalityAdd)
def create_locality(request: schemas.LocalityAdd, db: Session = Depends(get_db)):
    return dicts.create_locality(db, request)


@router.delete('/{id}')
def delete_locality(id: int, db: Session = Depends(get_db)):
    return dicts.delete_locality(db, id)


@router.get('/{id}', response_model=schemas.LocalityAdd)
def get_locality(id: int, db: Session = Depends(get_db)):
    return dicts.get_locality(db, id)


@router.get('/')
def get_localities(db: Session = Depends(get_db)):
    return dicts.get_localities(db)
