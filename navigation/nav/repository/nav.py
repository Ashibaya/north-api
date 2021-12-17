from sqlalchemy.orm import Session, query, session, aliased
from fastapi import HTTPException, status
from sqlalchemy import alias
from navigation.nav.schemas import nav as schemas, dicts as dict_schemas
from navigation.nav.models import nav as models, dicts as dict_models
from navigation.nav.repository import dicts as dict_repo


def get_dict_from_row(obj):
    res = obj.__dict__
    res.pop("_sa_instance_state", None)
    return res
# decades


def create_decades(db: Session, year: int):
    # дописать функцию разделения на декады и записать в БД
    if year in db.select(models.Decada).year:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Decade with year = {year} already added")
    return {'status': 'done'}

# customer


def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(**customer.dict())
    if db.query(models.Customer).\
            filter(models.Customer.org_id == db_customer.org_id).one_or_none() != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Customer with id {db_customer.id} already added")
    db.add(db_customer)
    db.commit()
    return db_customer


def select_customers(db: Session):
    return db.query(models.Customer)


def get_customers_origin(db: Session):
    return select_customers(db).all()


def select_customers_joins(db: Session):
    return select_customers(db).join(dict_models.Org).with_entities(models.Customer, dict_models.Org)


def get_customer_origin(db: Session, id: int):
    return db.query(models.Customer).filter(models.Customer.id == id).one_or_none()


def get_customer_by_org(db: Session, org_id: int):
    return db.query(models.Customer).filter(models.Customer.org_id == org_id).one_or_none()


def get_customers(db: Session):
    orgs = get_customers_origin(db)
    res = []
    for item in orgs:
        item = get_dict_from_row(item)
        item["org"] = dict_repo.get_org(db, item.get("org_id"))
        res.append(item)
    return res


def get_customer(db: Session, id: int):
    db_customer = get_customer_origin(db, id)
    customer = get_dict_from_row(db_customer)
    if db_customer == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Customer with id {id} not found")
    customer["org"] = dict_repo.get_org(db, db_customer.org_id)
    return db_customer


def delete_customer(db: Session, org_id: int):
    db_customer = db.query(models.Customer)\
        .filter(models.Customer.org_id == org_id)
    if not db_customer.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Customer with id {id} not found")
    db_customer.delete()
    db.commit()
    return {'status': 'done'}

    # supplier


def create_supplier(db: Session, supplier: schemas.SupplierCreate):
    db_supplier = models.Supplier(**supplier.dict())
    if db.query(models.Supplier).\
            filter(models.Supplier.org_id == db_supplier.org_id).one_or_none() != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Supplier with id {db_supplier.id} already added")
    db.add(db_supplier)
    db.commit()
    return db_supplier


def select_supplier(db: Session, id: int):
    return db.query(models.Supplier).filter(models.Supplier.id == id)


def select_suppliers(db: Session):
    return db.query(models.Supplier)


def get_suppliers_origin(db: Session):
    return select_suppliers(db).all()


def get_supplier_origin(db: Session, id: int):
    return select_supplier(db, id).one_or_none()


def select_suppliers_joins(db: Session):
    return select_suppliers(db).join(dict_models.Org).with_entities(models.Supplier, dict_models.Org)


def select_supplier_joins(db: Session, id: int):
    return select_supplier(db, id).join(dict_models.Org).with_entities(models.Supplier, dict_models.Org)


def get_supplier(db: Session, id: int):
    db_supplier = get_supplier_origin(db, id)
    if db_supplier == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Supplier with id {id} not found")
    supplier = get_dict_from_row(db_supplier)
    supplier["org"] = dict_repo.get_org(db, supplier.get("org_id"))

    return supplier


def get_suppliers(db: Session):
    db_suppliers = get_suppliers_origin(db)
    res = []
    for item in db_suppliers:
        supplier = get_dict_from_row(item)
        supplier["org"] = dict_repo.get_org(db, supplier.get("org_id"))
        res.append(supplier)

    return res


def delete_supplier(db: Session, org_id: int):
    db_supplier = db.query(models.Supplier)\
        .filter(models.Supplier.org_id == org_id)
    if db_supplier.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Supplier with org_id {org_id} not found")
    db_supplier.delete()
    db.commit()
    return {'status': 'done'}

    # carrier


def create_carrier(db: Session, carrier: schemas.CarrierCreate):
    db_carrier = models.Carrier(**carrier.dict())
    if db.query(models.Carrier).\
            filter(models.Carrier.org_id == db_carrier.org_id).one_or_none() != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Carrier with id {db_carrier.id} already added")
    db.add(db_carrier)
    db.commit()
    return db_carrier


def select_carriers(db: Session):
    return db.query(models.Carrier)


def select_carrier(db: Session, id: int):
    return select_carriers(db).filter(models.Carrier.id == id)


def select_carriers_joins(db: Session):
    return select_carriers(db).join(dict_models.Org).with_entities(models.Carrier, dict_models.Org)


def select_carriers_joins(db: Session, id: int):
    return select_carrier(db, id).join(dict_models.Org).with_entities(models.Carrier, dict_models.Org)


def get_carriers_origin(db: Session):
    return select_carriers(db).all()


def get_carriers(db: Session):

    return get_carriers_origin(db)


def get_carrier_origin(db: Session, id: int):
    return select_carrier(db, id).one_or_none()


def get_carrier(db: Session, id: int):
    db_carrier = get_carrier_origin(db, id)
    if db_carrier == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Carrier with id {id} not found")
    carrier = get_dict_from_row(db_carrier)
    carrier["org"] = dict_repo.get_org(db, carrier.get("org_id"))
    return carrier


def delete_carrier(db: Session, org_id: int):
    db_carrier = db.query(models.Carrier)\
        .filter(models.Carrier.org_id == org_id)
    if db_carrier.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Carrier with id {id} not found")
    db_carrier.delete()
    db.commit()
    return {'status': 'done'}

    # owner


def create_owner(db: Session, owner: schemas.Owner):
    db_owner = models.Owner(**owner.dict())
    if db.query(models.Owner).\
            filter(models.Owner.id == db_owner.org_id).one_or_none() != None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Owner with id {db_owner.id} already added")
    db.add(db_owner)
    db.commit()
    return db_owner


def get_owners_origin(db: Session):
    return db.query(models.Owner).all()


def get_owners(db: Session):
    owners = get_carriers_origin(db)
    res = []
    for item in owners:
        owner = get_dict_from_row(item)
        owner["org"] = dict_repo.get_org(db, owner.get("org_id"))
        res.append(owner)
    return res


def get_owner_origin(db: Session, id: int):
    return db.query(models.Owner).filter(models.Owner.id == id).one_or_none()


def get_owner(db: Session, id: int):
    db_owner = get_owner_origin(db, id)
    if db_owner == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Owner with id {id} not found")
    owner = get_dict_from_row(db_owner)
    owner["org"] = dict_repo.get_org(db, owner.get("org_id"))
    return owner


def delete_owner(db: Session, org_id: int):
    db_owner = db.query(models.Owner)\
        .filter(models.Owner.org_id == org_id)
    if db_owner.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Owner with id {id} not found")
    db_owner.delete()
    db.commit()
    return {'status': 'done'}

# bid


def create_bid(db: Session, bid: schemas.BidCreate):
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
    return {'status': 'done'}


def select_bid(db: Session, id: int):
    return db.query(models.Bid).filter(models.Bid.id == id)


def select_bids(db: Session):
    return db.query(models.Bid)


def get_bid(db: Session, id: int):
    return select_bid(db, id).first()


def make_bids(db: Session, bid_id: int = None):
    # bids_db = select_bids.all() if bid_id == None else [
    #    get_bid(db, bid_id)]
    supplier = aliased(select_suppliers_joins(db).subquery(), "supplier")
    customer = aliased(select_customers_joins(db).subquery(), "customer")
    ss = select_bids(db).\
        join(dict_models.Cargo).\
        join(dict_models.Point).\
        join(customer, models.Bid.customer_id == customer.columns.id).\
        join(supplier, models.Bid.supplier_id == supplier.columns.id).\
        with_entities(
            models.Bid.id,
            models.Bid.point_id,
            models.Bid.cargo_id,
            models.Bid.quantity,
            models.Bid.customer_id,
            models.Bid.supplier_id,
            models.Bid.start_date,
            models.Bid.end_date,
            models.Bid.created_date,
            dict_models.Cargo.name.label("cargo_name"),
            dict_models.Point.name.label("point_name"),
            customer.columns.name.label("customer_name"),
            supplier.columns.name.label("supplier_name")

    )
    return ss


def get_bids(db: Session):
    bids = make_bids(db).all()
    dicts = [dict(row) for row in bids]
    return dicts


def get_bid_info(db: Session, id: int):
    res = make_bids(db, id).filter(models.Bid.id == id)
    return res.first()
# bid confirm


def create_bid_confirm(db: Session, bid_confirm: schemas.BidConfirmCreate):
    db_bid_confirm = models.BidConfirm(**bid_confirm.dict())
    db.add(db_bid_confirm)
    db.commit()
    db.refresh(db_bid_confirm)
    return db_bid_confirm


def delete_bid_confirm(db: Session, id: int):
    bid = db.query(models.BidConfirm).filter(models.BidConfirm.id == id)
    if bid.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Bid with id = {id} is not found")
    bid.delete(synchronize_session=False)
    db.commit()
    return {"status": "done"}


def get_bid_confirm(db: Session, id: int):
    bid_confirm = db.query(models.BidConfirm).filter(
        models.BidConfirm.id == id).one_or_none()
    bid = get_bid_info(db, bid_confirm.bid_id)
    bid_confirm = get_dict_from_row(bid_confirm)
    bid_confirm["bid"] = bid
    return bid_confirm


def get_bids_confirm(db: Session):
    bids_confirm = db.query(models.BidConfirm).all()
    bids = []
    for bid in bids_confirm:
        bid = get_dict_from_row(bid)
        bid["bid"] = get_bid_info(db, bid.get("bid_id"))
        bids.append(bid)
    return bids


def update_bid_confirm(db: Session, confirm: schemas.BidConfirm):
    conf = confirm.dict()
    confirm_model = models.BidConfirm(**confirm.dict())
    db_confirm = db.query(models.BidConfirm).filter(
        models.BidConfirm.id == conf.get("id"))
    if db_confirm.one_or_none() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"BidConfirm with id {id} not found")
    db_confirm.update(conf)
    db.commit()
    return confirm_model
# bid_delivery


def create_bid_delivery(db: Session, bid_delivery: schemas.BidDeliveryCreate):
    bid_delivery = models.BidDelivery(**bid_delivery.dict())
    db.add(bid_delivery)
    db.commit()
    db.refresh(bid_delivery)
    return bid_delivery


def delete_bid_delivery(db: Session, id: int):
    bid = db.query(models.BidDelivery).filter(models.BidDelivery.id == id)
    bid.delete(synchronize_session=False)
    db.commit()
    return {"status": "done"}


def get_bid_delivery(db: Session, id: int):
    return db.query(models.BidDelivery).filter(models.BidDelivery.id == id).one_or_none()


def get_bids_delivery(db: Session, bid_id: int = None):
    bids_delivery_query = db.query(models.BidDelivery).filter(
        models.BidDelivery.bid_id == bid_id) if id else db.query(models.BidDelivery)
    bids_delivery = bids_delivery_query.all()
    bid_dict = {it.get("id"): it for it in get_bids(db)}
    carrier_dict = {it.id: dict_repo.get_org(
        db, it.org_id).name for it in get_carriers_origin(db)}
    print(carrier_dict)
    bids = []
    for bid_delivery in bids_delivery:
        bid_delivery = get_dict_from_row(bid_delivery)
        print(bid_delivery)
        bid_delivery["bid"] = bid_dict.get(bid_delivery.get("bid_id"))
        bid_delivery["carrier_name"] = carrier_dict.get(
            bid_delivery.get("carrier_id"))
        bids.append(bid_delivery)
    return bids


# bid_delivery_confirm

def create_bid_delivery_confirm(db: Session, confirm: schemas.BidDeliveryConfirmCreate):
    db_conf = models.BidDeliveryConfirm(**confirm.dict())
    db.add(db_conf)
    db.commit()
    db.refresh(db_conf)
    return db_conf


def delete_bid_delivery_confirm(db: Session, id: int):
    db_conf = db.query(models.BidDeliveryConfirm).filter(
        models.BidDeliveryConfirm.id == id)
    if db_conf.one_or_none() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"BidDeliveryConfirm with id {id} not found")
    db_conf.delete(synchronize_session=False)
    db.commit()
    return {"status": "done"}


def get_bid_delivery_confirm(db: Session, id: int):
    return db.query(models.BidDeliveryConfirm).filter(models.BidDeliveryConfirm.id == id).one_or_none()


def get_bids_delivery_confirm(db: Session, bid_id: int = None):
    bids_conf = db.query(models.BidDeliveryConfirm).all(
    ) if bid_id == None else get_bid_delivery_confirm(db, bid_id)
    bid_delivery_dict = {
        item.get("id"): item for item in get_bids_delivery(db)}
    resault = []
    for item in bids_conf:
        item = get_dict_from_row(item)
        item["bid_delivery"] = bid_delivery_dict.get(item.get("delivery_id"))
        resault.append(item)
    return resault


def update_bid_delivery_confirm(db: Session, confirm_schema: schemas.BidDeliveryConfirm):
    confirm = confirm_schema.dict()
    confirm_model = models.BidDeliveryConfirm(**confirm_schema.dict())
    db_confirm = db.query(models.BidDeliveryConfirm).filter(
        models.BidDeliveryConfirm.id == confirm.get("id"))
    if db_confirm.one_or_none() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"BidDeliveryConfirm with id {id} not found")
    db_confirm.update(confirm)
    db.commit()
    return confirm_model
# bid_owner_confirm


def create_bid_owner_confirm(db: Session, confirm: schemas.BidOwnerConfirmCreate):
    db_conf = models.BidOwnerConfirm(**confirm.dict())
    db.add(db_conf)
    db.commit()
    db.refresh(db_conf)
    return db_conf


def delete_bid_owner_confirm(db: Session, id: int):
    db_conf = db.query(models.BidOwnerConfirm).filter(
        models.BidOwnerConfirm.id == id)
    if db_conf.one_or_none() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"BidOwnerConfirm with id {id} not found")
    db_conf.delete(synchronize_session=False)
    db.commit()
    return {"status": "done"}


def get_bid_owner_confirm(db: Session, id: int):
    return db.query(models.BidOwnerConfirm).filter(models.BidOwnerConfirm.bid_id == id).one_or_none()


def get_bids_owner_confirm(db: Session):
    bids_conf = db.query(models.BidOwnerConfirm).all()
    bid_dict = {item.get("id"): item for item in get_bids(db)}
    resault = []
    for item in bids_conf:
        item = get_dict_from_row(item)
        item["bid"] = bid_dict.get(item.get("bid_id"))
        item["bid_delivery"] = get_bids_delivery(db, item.get("bid_id"))
        resault.append(item)
    return resault


def update_bid_owner_confirm(db: Session, confirm_schema: schemas.BidOwnerConfirm):
    confirm = confirm_schema.dict()
    confirm_model = models.BidOwnerConfirm(**confirm_schema.dict())
    db_confirm = db.query(models.BidOwnerConfirm).filter(
        models.BidOwnerConfirm.id == confirm.get("id"))
    if db_confirm.one_or_none() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"BidOwnerConfirm with id {id} not found")
    db_confirm.update(confirm)
    return confirm_model
