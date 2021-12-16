from navigation.nav.schemas import reports as schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from navigation.nav.repository import reports
from typing import List
from auth import database

router = APIRouter(
    prefix="/plan"
)

get_db = database.get_db

# Заказчик


@router.get('/bid')
def get_report(db: Session = Depends(get_db)):
    return reports.get_bid_plan(db)


@router.get('/plan_stat/year={year},month={month},customer_id={customer_id}')
def get_bid_plan_stat(year: int, month:int, customer_id: int, db: Session = Depends(get_db)):
    return reports.get_bid_plan_stat(db, year, month, customer_id)