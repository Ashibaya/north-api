from navigation.nav.schemas import nav as schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from navigation.nav.repository import nav
from auth import database

router = APIRouter(
    prefix="/customer"
)

get_db = database.get_db

# Заказчик


@router.post('/', response_model=schemas.Customer)
def create_customer(request: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return nav.create_customer(db, request)


@router.delete('/{id}')
def delete_customer(id: int, db: Session = Depends(get_db)):
    return nav.delete_customer(db, id)


@router.get('/{id}', response_model=schemas.CustomerShow)
def get_customer(id: int, db: Session = Depends(get_db)):
    return nav.get_customer(db, id)


@router.get('/')
def get_customers(db: Session = Depends(get_db)):
    return nav.get_customers(db)