from navigation.nav.schemas import dicts as schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from navigation.nav.repository import dicts
from typing import List
from auth import database

router = APIRouter(
    prefix="/org",
)

get_db = database.get_db


@router.post('/', response_model=schemas.OrgAdd)
def create_org(request: schemas.OrgAdd, db: Session = Depends(get_db)):
    return dicts.create_org(db, request)


@router.put('/', response_model=schemas.OrgAdd)
def update_org(request: schemas.OrgAdd, db: Session = Depends(get_db)):
    return dicts.update_org(db, request)


@router.delete('/{id}')
def delete_org(id: int, db: Session = Depends(get_db)):
    return dicts.delete_org(db, id)


@router.get('/{id}', response_model=schemas.OrgShowAll)
def get_org(id: int, db: Session = Depends(get_db)):
    return dicts.get_org(db, id)


@router.get('/', response_model=List[schemas.OrgShowAll])
def get_orgs(db: Session = Depends(get_db)):
    return dicts.get_orgs(db)
