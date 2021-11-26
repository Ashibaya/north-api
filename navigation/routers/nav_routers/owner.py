from navigation.nav.schemas import nav as schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from navigation.nav.repository import nav
from auth import database

router = APIRouter(
    prefix="/owner"
)

get_db = database.get_db

# Заказчик


@router.post('/', response_model=schemas.OwnerShow)
def create_owner(request: schemas.Owner, db: Session = Depends(get_db)):
    return nav.create_owner(db, request)


@router.delete('/{id}')
def delete_carrier(id: int, db: Session = Depends(get_db)):
    return nav.delete_carrier(db, id)


@router.get('/{id}', response_model=schemas.OwnerShow)
def get_owner(id: int, db: Session = Depends(get_db)):
    return nav.get_owner(db, id)


@router.get('/')
def get_owners(db: Session = Depends(get_db)):
    return nav.get_owners(db)
    