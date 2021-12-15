from navigation.nav.schemas import reports as schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from navigation.nav.repository import reports
from typing import List
from auth import database

router = APIRouter(
    prefix="/plan_bid"
)

get_db = database.get_db

# Заказчик


@router.get('/')
def get_report(db: Session = Depends(get_db)):
    return reports.get_bid_plan(db)
