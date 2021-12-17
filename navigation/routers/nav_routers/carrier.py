from navigation.nav.schemas import nav as schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from navigation.nav.repository import nav
from auth import database
from typing import List
router = APIRouter(
    prefix="/carrier"
)

get_db = database.get_db

# Заказчик


@router.post('/', response_model=schemas.Carrier)
def create_carrier(request: schemas.CarrierCreate, db: Session = Depends(get_db)):
    return nav.create_carrier(db, request)


@router.delete('/{id}')
def delete_carrier(id: int, db: Session = Depends(get_db)):
    return nav.delete_carrier(db, id)


@router.get('/{id}', response_model=schemas.CarrierShow)
def get_carrier(id: int, db: Session = Depends(get_db)):
    return nav.get_carrier(db, id)


@router.get('/', response_model=List[schemas.CarrierShow])
def get_carriers(db: Session = Depends(get_db)):
    return nav.get_carriers(db)
