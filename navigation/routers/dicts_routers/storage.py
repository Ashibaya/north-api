from navigation.nav.schemas import dicts as schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from navigation.nav.repository import dicts
from auth import database
from typing import List
router = APIRouter(
    prefix="/storage",
)

get_db = database.get_db

# Unit


@router.post('/', response_model=schemas.StorageAdd)
def create_storage(request: schemas.StorageAdd, db: Session = Depends(get_db)):
    return dicts.create_storage(db, request)


@router.put('/', response_model=schemas.StorageAdd)
def update_storage(request: schemas.StorageAdd, db: Session = Depends(get_db)):
    return dicts.update_storage(db, request)


@router.delete('/{id}')
def delete_storage(id: int, db: Session = Depends(get_db)):
    return dicts.delete_storage(db, id)


@router.get('/{id}', response_model=schemas.StorageShow)
def get_storage(id: int, db: Session = Depends(get_db)):
    return dicts.get_storage(db, id)


@router.get('/', response_model=List[schemas.StorageShow])
def get_storages(db: Session = Depends(get_db)):
    return dicts.get_storages(db)
