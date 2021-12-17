from navigation.nav.schemas import dicts as schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from navigation.nav.repository import dicts
from auth import database
from typing import List
router = APIRouter(
    prefix="/unit",
)

get_db = database.get_db

# Unit


@router.post('/', response_model=schemas.UnitAdd)
def create_unit(request: schemas.UnitAdd, db: Session = Depends(get_db)):
    return dicts.create_unit(db, request)


@router.delete('/{id}')
def delete_unit(id: int, db: Session = Depends(get_db)):
    return dicts.delete_unit(db, id)


@router.put('/', response_model=schemas.UnitAdd)
def update_unit(request: schemas.UnitAdd, db: Session = Depends(get_db)):
    return dicts.update_unit(db, request)


@router.get('/{id}', response_model=schemas.UnitShow)
def get_unit(id: int, db: Session = Depends(get_db)):
    return dicts.get_unit(db, id)


@router.get('/', response_model=List[schemas.UnitShow])
def get_units(db: Session = Depends(get_db)):
    return dicts.get_units(db)
