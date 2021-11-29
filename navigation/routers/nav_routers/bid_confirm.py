from navigation.nav.schemas import nav as schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from navigation.nav.repository import nav
from typing import List
from auth import database

router = APIRouter(
    prefix="/bid_confirm"
)

get_db = database.get_db

# Заказчик


@router.post('/', response_model=schemas.BidConfirm)
def create_bid_confirm(request: schemas.BidConfirmCreate, db: Session = Depends(get_db)):
    return nav.create_bid_confirm(db, request)


@router.delete('/{id}')
def delete_bid_confirm(id: int, db: Session = Depends(get_db)):
    return nav.delete_bid_confirm(db, id)


@router.get('/{id}', response_model=schemas.BidConfirmShow)
def get_bid_confirm(id: int, db: Session = Depends(get_db)):
    return nav.get_bid_confirm(db, id)


@router.get('/')
def get_bids_confirm(db: Session = Depends(get_db)):
    return nav.get_bids_confirm(db)

@router.put('/', response_model=schemas.BidConfirm)
def update_bid_confirm(request : schemas.BidConfirm, db: Session = Depends(get_db)):
    return nav.update_bid_confirm(db, request)
    