from navigation.nav.schemas import nav as schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from navigation.nav.repository import nav
from typing import List
from auth import database

router = APIRouter(
    prefix="/bid_delivery_confirm"
)

get_db = database.get_db

# Заказчик


@router.post('/', response_model=schemas.BidDeliveryConfirmShow)
def create_bid_delivery_confirm(request: schemas.BidDeliveryConfirmCreate, db: Session = Depends(get_db)):
    return nav.create_bid_delivery_confirm(db, request)


@router.delete('/{id}')
def delete_bid_delivery_confirm(id: int, db: Session = Depends(get_db)):
    return nav.delete_bid_delivery_confirm(db, id)


@router.get('/{id}', response_model=schemas.BidDeliveryConfirmShow)
def get_bid_delivery_confirm(id: int, db: Session = Depends(get_db)):
    return nav.get_bid_delivery_confirm(db, id)


@router.get('/', response_model=List[schemas.BidDeliveryConfirmShow])
def get_bids_delivery_confirm(db: Session = Depends(get_db)):
    return nav.get_bids_delivery_confirm(db)
    