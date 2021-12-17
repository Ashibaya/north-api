from navigation.nav.schemas import dicts as schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from navigation.nav.repository import dicts
from auth import database
from typing import List

router = APIRouter(
    prefix="/point",
)

get_db = database.get_db

# Unit


@router.post('/', response_model=schemas.PointAdd)
def create_point(request: schemas.PointAdd, db: Session = Depends(get_db)):
    return dicts.create_point(db, request)


@router.put('/', response_model=schemas.PointAdd)
def update_point(request: schemas.PointAdd, db: Session = Depends(get_db)):
    return dicts.update_point(db, request)


@router.delete('/{id}')
def delete_point(id: int, db: Session = Depends(get_db)):
    return dicts.delete_point(db, id)


@router.get('/{id}', response_model=schemas.PointShow)
def get_point(id: int, db: Session = Depends(get_db)):
    return dicts.get_point(db, id)


@router.get('/', response_model=List[schemas.PointShow])
def get_points(db: Session = Depends(get_db)):
    return dicts.get_points(db)
