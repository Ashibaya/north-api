from navigation.nav.schemas import nav as schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from navigation.nav.repository import nav
from auth import database

router = APIRouter(
    prefix="/bid"
)

get_db = database.get_db

# Заказчик


@router.post('/', response_model=schemas.Bid)
def create_bid(request: schemas.BidCreate, db: Session = Depends(get_db)):
    return nav.create_bid(db, request)


@router.delete('/{id}')
def delete_bid(id: int, db: Session = Depends(get_db)):
    return nav.delete_bid(db, id)


@router.get('/{id}', response_model=schemas.BidShow)
def get_bid(id: int, db: Session = Depends(get_db)):
    return nav.get_bid(db, id)


@router.get('/')
def get_bids(db: Session = Depends(get_db)):
    return nav.get_bids(db)
    