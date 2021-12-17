from navigation.nav.schemas import dicts as schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from navigation.nav.repository import dicts
from auth import database
from typing import List
router = APIRouter(
    prefix="/region",
)

get_db = database.get_db


@router.post('/', response_model=schemas.RegionAdd)
def create_region(request: schemas.RegionAdd, db: Session = Depends(get_db)):
    return dicts.create_region(db, request)


@router.put('/', response_model=schemas.RegionAdd)
def update_region(request: schemas.RegionAdd, db: Session = Depends(get_db)):
    return dicts.update_region(db, request)


@router.delete('/{id}')
def delete_region(id: int, db: Session = Depends(get_db)):
    return dicts.delete_region(db, id)


@router.get('/{id}', response_model=schemas.RegionShow)
def get_region(id: int, db: Session = Depends(get_db)):
    return dicts.get_region(db, id)


@router.get('/', response_model=List[schemas.RegionShow])
def get_regions(db: Session = Depends(get_db)):
    return dicts.get_regions(db)
