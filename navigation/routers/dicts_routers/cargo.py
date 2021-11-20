from navigation.nav.schemas import dicts as schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from navigation.nav.repository import dicts
from auth import database

router = APIRouter(
    prefix="/cargo"
)

get_db = database.get_db


@router.post('/', response_model=schemas.CargoAdd)
def create_cargo(request: schemas.CargoAdd, db: Session = Depends(get_db)):
    return dicts.create_cargo(db, request)


@router.delete('/{id}')
def delete_cargo(id: int, db: Session = Depends(get_db)):
    return dicts.delete_cargo(db, id)


@router.get('/{id}', response_model=schemas.CargoAdd)
def get_cargo(id: int, db: Session = Depends(get_db)):
    return dicts.get_cargo(db, id)


@router.get('/')
def get_cargos(db: Session = Depends(get_db)):
    return dicts.get_cargos(db)
