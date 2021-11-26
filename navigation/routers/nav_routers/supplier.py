from navigation.nav.schemas import nav as schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from navigation.nav.repository import nav
from auth import database

router = APIRouter(
    prefix="/supplier"
)

get_db = database.get_db

# Заказчик


@router.post('/', response_model=schemas.SupplierShow)
def create_supplier(request: schemas.Supplier, db: Session = Depends(get_db)):
    return nav.create_supplier(db, request)


@router.delete('/{id}')
def delete_supplier(id: int, db: Session = Depends(get_db)):
    return nav.delete_supplier(db, id)


@router.get('/{id}', response_model=schemas.SupplierShow)
def get_supplier(id: int, db: Session = Depends(get_db)):
    return nav.get_supplier(db, id)


@router.get('/')
def get_suppliers(db: Session = Depends(get_db)):
    return nav.get_suppliers(db)