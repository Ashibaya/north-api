from navigation.nav.schemas import dicts as schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from navigation.nav.repository import dicts
from auth import database
from typing import List
router = APIRouter(
    prefix="/boat"
)

get_db = database.get_db

# Unit


@router.post('/', response_model=schemas.BoatAdd)
def create_boat(request: schemas.BoatAdd, db: Session = Depends(get_db)):
    return dicts.create_boat(db, request)


@router.put('/', response_model=schemas.BoatAdd)
def update_boat(request: schemas.BoatAdd, db: Session = Depends(get_db)):
    return dicts.update_boat(db, request)


@router.delete('/{id}')
def delete_boat(id: int, db: Session = Depends(get_db)):
    return dicts.delete_boat(db, id)


@router.get('/{id}', response_model=schemas.BoatShow)
def get_boat(id: int, db: Session = Depends(get_db)):
    return dicts.get_boat(db, id)


@router.get('/', response_model=List[schemas.BoatShow])
def get_boats(db: Session = Depends(get_db)):
    return dicts.get_boats(db)
