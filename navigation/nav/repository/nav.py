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
    db_customer = models.Customer(**customer.dict())
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
    

    #supplier

def create_supplier(db:Session, supplier: schemas.Supplier):
    db_supplier = models.Supplier(**supplier.dict())
    if not db.query(models.Supplier).\
        filter(models.Supplier.id == db_supplier.id_org).one_or_none():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Supplier with id {db_supplier.id} already added")
    db.add(db_supplier)
    db.commit()
    return db_supplier

def get_suppliers(db: Session):
    return db.query(dict_models.Org)\
    .filter(dict_models.Org.id  == models.Supplier.id_org).all()

def get_supplier(db: Session, id_org: int):
    db_supplier = db.query(dict_models.Org)\
    .filter(dict_models.Org.id  == id_org).first()
    if not db_supplier:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Supplier with id {id} not found")
    return db_supplier

def delete_supplier(db: Session, id_org: int):
    db_supplier = db.query(models.Supplier)\
    .filter(models.Supplier.id_org  == id_org).first()
    if not db_supplier:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Supplier with id {id} not found")
    return {'status':'done'}

    #carrier

def create_carrier(db:Session, carrier: schemas.Carrier):
    db_carrier = models.Carrier(**carrier.dict())
    if not db.query(models.Carrier).\
        filter(models.Carrier.id == db_carrier.id_org).one_or_none():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Carrier with id {db_carrier.id} already added")
    db.add(db_carrier)
    db.commit()
    return db_carrier

def get_carriers(db: Session):
    return db.query(dict_models.Org)\
    .filter(dict_models.Org.id._in(models.Carrier.id_org)).all()

def get_carrier(db: Session, id_org: int):
    db_carrier = db.query(dict_models.Org)\
    .filter(dict_models.Org.id  == id_org).first()
    if not db_carrier:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Carrier with id {id} not found")
    return db_carrier

def delete_carrier(db: Session, id_org: int):
    db_carrier = db.query(models.Carrier)\
    .filter(models.Carrier.id_org  == id_org).first()
    if not db_carrier:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Carrier with id {id} not found")
    return {'status':'done'}

    #owner

def create_owner(db:Session, owner: schemas.Owner):
    db_owner = models.Owner(**owner.dict())
    if not db.query(models.Owner).\
        filter(models.Owner.id == db_owner.id_org).one_or_none():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Owner with id {db_owner.id} already added")
    db.add(db_owner)
    db.commit()
    return db_owner

def get_cowners(db: Session):
    return db.query(dict_models.Org)\
    .filter(dict_models.Org.id  == models.Owner.id_org).all()

def get_owner(db: Session, id_org: int):
    db_owner = db.query(dict_models.Org)\
    .filter(dict_models.Org.id  == id_org).first()
    if not db_owner:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Owner with id {id} not found")
    return db_owner

def delete_owner(db: Session, id_org: int):
    db_owner = db.query(models.Owner)\
    .filter(models.Owner.id_org  == id_org).first()
    if not db_owner:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Owner with id {id} not found")
    return {'status':'done'}

#bid