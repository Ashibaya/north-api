from navigation.nav.schemas import nav as schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from navigation.nav.repository import nav
from typing import List
from auth import database

router = APIRouter(
    prefix="/bid_delivery"
)

get_db = database.get_db

# Заказчик


@router.post('/', response_model=schemas.BidDelivery)
def create_bid_delivery(request: schemas.BidDeliveryCreate, db: Session = Depends(get_db)):
    return nav.create_bid_delivery(db, request)


@router.delete('/{id}')
def delete_bid_delivery(id: int, db: Session = Depends(get_db)):
    return nav.delete_bid_delivery(db, id)


@router.get('/{id}', response_model=schemas.BidDeliveryShow)
def get_bid_delivery(id: int, db: Session = Depends(get_db)):
    return nav.get_bid_delivery(db, id)


@router.get('/', response_model=List[schemas.BidDeliveryShow])
def get_bids_delivery(db: Session = Depends(get_db)):
    return nav.get_bids_delivery(db)
    