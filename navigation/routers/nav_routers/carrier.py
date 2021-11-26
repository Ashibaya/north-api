from navigation.nav.schemas import nav as schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from navigation.nav.repository import nav
from auth import database

router = APIRouter(
    prefix="/carrier"
)

get_db = database.get_db

# Заказчик


@router.post('/', response_model=schemas.CarrierShow)
def create_carrier(request: schemas.Carrier, db: Session = Depends(get_db)):
    return nav.create_carrier(db, request)


@router.delete('/{id}')
def delete_carrier(id: int, db: Session = Depends(get_db)):
    return nav.delete_carrier(db, id)


@router.get('/{id}', response_model=schemas.CarrierShow)
def get_carrier(id: int, db: Session = Depends(get_db)):
    return nav.get_carrier(db, id)


@router.get('/')
def get_carriers(db: Session = Depends(get_db)):
    return nav.get_carriers(db)
    