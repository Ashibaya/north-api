from logging import disable
from sqlalchemy.orm import Session, query, session
from fastapi import HTTPException, status
from sqlalchemy.sql.expression import select
from navigation.nav.schemas import nav as schemas, dicts as dict_schemas
from navigation.nav.models import nav as models, dicts as dict_models
from navigation.nav.repository import dicts as dict_repo
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
    .filter(models.Customer.id_org  == id_org)
    if not db_customer.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Customer with id {id} not found")
    db_customer.delete()
    db.commit()
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
    .filter(models.Supplier.id_org  == id_org)
    if not db_supplier.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Supplier with id {id} not found")
    db_supplier.delete()
    db.commit()
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
    .filter(models.Carrier.id_org  == id_org)
    if not db_carrier.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Carrier with id {id} not found")
    db_carrier.delete()
    db.commit()
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

def get_owners(db: Session):
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
    .filter(models.Owner.id_org  == id_org)
    if not db_owner.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Owner with id {id} not found")
    db_owner.delete()
    db.commit()
    return {'status':'done'}

#bid

def create_bid(db:Session, bid: schemas.BidCreate):
    db_bid = models.Bid(**bid.dict())
    db.add(db_bid)
    db.commit()
    db.refresh(db_bid)
    return db_bid

def delete_bid(db: Session, id: int):
    db_bid = db.query(models.Bid).filter(models.Bid.id == id)
    if db_bid.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Bid with id = {id} is not found")
    db_bid.delete(synchronize_session=False)
    db.commit()
    return {'status':'done'}

def get_bid(db: Session, id: int):
    return db.query(models.Bid).filter(models.Bid.id == id).first()

def make_bids(db: Session, bid_id: int = None):
    bid = f" WHERE bids.id = {bid_id}" if bid_id else ""
    return db.execute("SELECT bids.*,points.name  as point_name,"\
                    " cargos.name as cargo_name, customers.name as customer_name,"\
                    " suppliers.name as supplier_name FROM bids JOIN points ON bids.point_id = points.id"\
                    " JOIN cargo ON bids.cargo_id = cargos.id JOIN customers ON bids.customer_id = customers.id"\
                    " JOIN suppliers ON bids.supplier_id = suppliers.id"+bid)

def get_bids(db: Session):
    return make_bids(db).all()

def get_bid_info(db: Session, id: int):
    return make_bids(db, id).one_or_none()
#bid confirm

def create_bid_confirm(db: Session, bid_confirm: schemas.BidConfirmCreate):
    db_bid_confirm = models.BidConfirm(**bid_confirm.dict())
    db.add(db_bid_confirm)
    db.commit()
    db.refresh(db_bid_confirm)
    return db_bid_confirm

def delete_bid_confirm(db: Session,id: int):
    bid = db.query(models.BidConfirm).filter(models.BidConfirm.id == id)
    bid.delete()
    db.commit()
    return {"status":"done"}

def get_bid_confirm(db: Session, id: int):
    bid_confirm = db.query(models.BidConfirm).filter(models.BidConfirm.id == id).one_or_none()
    bid = get_bid_info(db, bid_confirm.bid_id)
    bid_confirm["bid"] = bid
    return bid_confirm

def get_bids_confirm(db: Session):
    bids_confirm = db.query(models.BidConfirm).all()
    bids = []
    for bid in bids_confirm:
        bid["bid"] = get_bid_info(db, bid.bid_id) 
        bids.append(bid)
    return bids

#bid_delivery

def create_bid_delivery(db: Session, bid_delivery: schemas.BidDeliveryCreate):
    bid_delivery = models.BidDelivery(**bid_delivery.dict())
    db.add(bid_delivery)
    db.commit()
    db.refresh(bid_delivery)
    return bid_delivery

def delete_bid_delivery(db: Session, id: int):
    bid = db.query(models.BidDelivery).filter(models.BidDelivery.id == id)
    bid.delete()
    db.commit()
    return {"status": "done"}

def get_bid_delivery(db: Session, id: int):
    return db.query(models.BidDelivery).filter(models.BidDelivery.id == id).one_or_none()


def get_bids_delivery(db: Session):
    bids_delivery = db.query(models.BidDelivery).all()
    bid_dict = {it.id : it for it in get_bids(db)}
    carrier_dict = { it.id: dict_repo.get_org(db, it.org_id) for it in dict_repo.get_carriers(db)}
    bids = []
    for bid_delivery in bids_delivery:
        bid_delivery["bid"] = bid_dict.get(bid_delivery.bid_id)
        bid_delivery["carrier_name"] = carrier_dict.get(bid_delivery.carrier_id)
        bids.append(bid_delivery)
    return bids
