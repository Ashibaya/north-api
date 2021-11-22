from sqlalchemy.orm import Session, query
from fastapi import HTTPException, status
from sqlalchemy.sql.expression import select
from navigation.nav.schemas import nav as schemas, dicts as dict_schemas
from navigation.nav.models import nav as models, dicts as dict_models

#decades

def create_decades(db: Session, year: int):
    #дописать функцию разделения на декады и записать в БД
    if year in db.select(models.Decada).year:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Decade with year = {year} already added")
    return {'status':'done'}

#customer

def create_customer(db:Session, customer: schemas.Customer):
    db_customer = models.Customer(**customer)
    if not db.query(models.Customer).\
        filter(models.Customer.id == db_customer.id_org).one_or_none():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Customer with id {db_customer.id} already added")
    db.add(db_customer)
    db.commit()
    return db_customer

def get_customers(db: Session):
    return db.query(dict_models.Org)\
    .filter(dict_models.Org.id  == models.Customer.id_org).all()

def get_customer(db: Session, id_org: int):
    db_customer = db.query(dict_models.Org)\
    .filter(dict_models.Org.id  == id_org).first()
    if not db_customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Customer with id {id} not found")
    return db_customer

def delete_customer(db: Session, id_org: int):
    db_customer = db.query(models.Customer)\
    .filter(models.Customer.id_org  == id_org).first()
    if not db_customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Customer with id {id} not found")
    return {'status':'done'}