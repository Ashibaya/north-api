from navigation.nav.schemas import nav as schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from navigation.nav.repository import nav
from typing import List
from auth import database

router = APIRouter(
    prefix="/bid_owner_confirm"
)

get_db = database.get_db

# Заказчик


@router.post('/')
def create_bid_owner_confirm(request: schemas.BidOwnerConfirmCreate, db: Session = Depends(get_db)):
    return nav.create_bid_owner_confirm(db, request)


@router.delete('/{id}')
def delete_bid_owner_confirm(id: int, db: Session = Depends(get_db)):
    return nav.delete_bid_owner_confirm(db, id)


@router.get('/{id}', response_model=schemas.BidOwnerConfirmShow)
def get_bid_owner_confirm(id: int, db: Session = Depends(get_db)):
    return nav.get_bid_owner_confirm(db, id)


@router.get('/', response_model=List[schemas.BidOwnerConfirmShow])
def get_bids_owner_confirm(db: Session = Depends(get_db)):
    return nav.get_bids_owner_confirm(db)


@router.put('/', response_model=schemas.BidOwnerConfirm)
def update_bid_owner_confirm(request: schemas.BidOwnerConfirm, db: Session = Depends(get_db)):
    return nav.update_bid_owner_confirm(db, request)
