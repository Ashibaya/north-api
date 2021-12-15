from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from navigation.nav.schemas import dicts as schemas
from navigation.nav.models import dicts as models

# UNIT


def create_unit(db: Session, unit: schemas.UnitAdd):
    db_unit = models.Unit(name=unit.name, short_name=unit.short_name)
    db.add(db_unit)
    db.commit()
    db.refresh(db_unit)
    return db_unit


def update_unit(db: Session, unit: schemas.UnitAdd):
    vals = unit.dict()
    model = models.Unit(**unit.dict())
    db_unit = db.query(models.Unit).filter(models.Unit.id == model.id)
    if not db_unit.one_or_none():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Unit with id {id} not found")
    db_unit.update(vals)
    db.commit()
    return model


def select_unit(db: Session, id: int):
    return db.query(models.Unit).filter(models.Unit.id == id)


def select_units(db: Session):
    return db.query(models.Unit)


def get_unit(db: Session, id: int):
    return select_unit(db, id).first()


def get_units(db: Session):
    return select_units(db).all()


def delete_unit(db: Session, id: int):
    db_unit = db.query(models.Unit).filter(models.Unit.id == id)
    if not db_unit.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Unit with id {id} not found")
    db_unit.delete(synchronize_session=False)
    db.commit()
    return {'status': 'done'}

# Cargo


def create_cargo(db: Session, cargo: schemas.CargoAdd):
    db_cargo = models.Cargo(name=cargo.name, unit_id=cargo.unit_id)
    db.add(db_cargo)
    db.commit()
    db.refresh(db_cargo)
    return db_cargo


def select_cargo(db: Session, id: int):
    return db.query(models.Cargo).filter(models.Cargo.id == id)


def select_cargos(db: Session):
    return db.query(models.Cargo)


def get_cargos(db: Session):
    return select_cargos(db).all()


def get_cargo(db: Session, id: int):
    return select_cargo(db, id).first()


def update_cargo(db: Session, cargo: schemas.CargoAdd):
    vals = cargo.dict()
    model = models.Cargo(**cargo.dict())
    db_cargo = db.query(models.Cargo).filter(models.Cargo.id == model.id)
    if not db_cargo.one_or_none():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Cargo with id {id} not found")
    db_cargo.update(vals)
    db.commit()
    return model


def delete_cargo(db: Session, id: int):
    db_cargo = db.query(models.Cargo).filter(models.Cargo.id == id)
    if not db_cargo.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Cargo with id {id} not found")
    db_cargo.delete(synchronize_session=False)
    db.commit()
    return {'status': 'done'}


# Region

def create_region(db: Session, region: schemas.RegionAdd):
    db_region = models.Region(name=region.name)
    db.add(db_region)
    db.commit()
    db.refresh(db_region)
    return db_region


def select_regions(db: Session):
    return db.query(models.Region)


def select_region(db: Session, id: int):
    return db.query(models.Region).filter(models.Region.id == id)


def get_regions(db: Session):
    return select_regions(db).all()


def get_region(db: Session, id: int):
    return select_region(db, id).first()


def update_region(db: Session, region: schemas.RegionAdd):
    vals = region.dict()
    model = models.Region(**region.dict())
    db_region = db.query(models.Region).filter(models.Region.id == model.id)
    if not db_region.one_or_none():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Region with id {id} not found")
    db_region.update(vals)
    db.commit()
    return model


def delete_region(db: Session, id: int):
    db_region = db.query(models.Region).filter(models.Region.id == id)
    if not db_region.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Region with id {id} not found")
    db_region.delete(synchronize_session=False)
    db.commit()
    return {'status': 'done'}


# Locality

def create_locality(db: Session, locality: schemas.LocalityAdd):
    db_locality = models.Locality(
        name=locality.name, region_id=locality.region_id)
    db.add(db_locality)
    db.commit()
    db.refresh(db_locality)
    return db_locality


def select_localities(db: Session):
    return db.query(models.Locality)


def select_locality(db: Session, id: int):
    return db.query(models.Locality).filter(models.Locality.id == id)


def get_localities(db: Session):
    return select_localities(db).all()


def get_locality(db: Session, id: int):
    return select_locality(db, id).first()


def update_locality(db: Session, locality: schemas.LocalityAdd):
    vals = locality.dict()
    model = models.Locality(**locality.dict())
    db_locality = db.query(models.Locality).filter(
        models.Locality.id == model.id)
    if not db_locality.one_or_none():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Locality with id {id} not found")
    db_locality.update(vals)
    db.commit()
    return model


def delete_locality(db: Session, id: int):
    db_locality = db.query(models.Locality).filter(models.Locality.id == id)
    if not db_locality.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Locality with id {id} not found")
    db_locality.delete(synchronize_session=False)
    db.commit()
    return {'status': 'done'}

# Rival


def create_rival(db: Session, rival: schemas.RivalAdd):
    db_rival = models.Rival(name=rival.name)
    db.add(db_rival)
    db.commit()
    db.refresh(db_rival)
    return db_rival


def select_rivals(db: Session):
    return db.query(models.Rival)


def select_rival(db: Session, id: int):
    return db.query(models.Rival).filter(models.Rival.id == id)


def get_rivals(db: Session):
    return select_rivals(db).all()


def get_rival(db: Session, id: int):
    return select_rival(db, id).first()


def update_rival(db: Session, rival: schemas.RivalAdd):
    vals = rival.dict()
    model = models.Rival(**rival.dict())
    db_rival = db.query(models.Rival).filter(models.Rival.id == model.id)
    if not db_rival.one_or_none():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Rival with id {id} not found")
    db_rival.update(vals)
    db.commit()
    return model


def delete_rival(db: Session, id: int):
    db_rival = db.query(models.Rival).filter(models.Rival.id == id)
    if not db_rival.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Rival with id {id} not found")
    db_rival.delete(synchronize_session=False)
    db.commit()
    return {'status': 'done'}


# Org


def create_org(db: Session, org: schemas.OrgAdd):
    db_org = models.Org(name=org.name,
                        inn=org.inn,
                        address=org.address,
                        phone=org.phone)
    db.add(db_org)
    db.commit()
    db.refresh(db_org)
    return db_org


def select_orgs(db: Session):
    return db.query(models.Org)


def select_org(db: Session, id: int):
    return db.query(models.Org).filter(models.Org.id == id)


def get_orgs(db: Session):
    return select_orgs(db).all()


def get_org(db: Session, id: int):
    return select_org(db, id).first()


def update_org(db: Session, org: schemas.OrgAdd):
    vals = org.dict()
    model = models.Org(**org.dict())
    db_org = db.query(models.Org).filter(models.Org.id == model.id)
    if not db_org.one_or_none():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Org with id {id} not found")
    db_org.update(vals)
    db.commit()
    return model


def delete_org(db: Session, id: int):
    db_org = db.query(models.Org).filter(models.Org.id == id)
    if not db_org.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Org with id {id} not found")
    db_org.delete(synchronize_session=False)
    db.commit()
    return {'status': 'done'}


# Point


def create_point(db: Session, point: schemas.PointAdd):
    db_point = models.Point(
        name=point.name, local_id=point.local_id, rival_id=point.rival_id)
    db.add(db_point)
    db.commit()
    db.refresh(db_point)
    return db_point


def select_points(db: Session):
    return db.query(models.Point)


def select_point(db: Session, id: int):
    return db.query(models.Point).filter(models.Point.id == id)


def get_points(db: Session):
    return select_points(db).all()


def get_point(db: Session, id: int):
    return select_point(db, id).first()


def update_point(db: Session, point: schemas.PointAdd):
    vals = point.dict()
    model = models.Point(**point.dict())
    db_point = db.query(models.Point).filter(models.Point.id == model.id)
    if not db_point.one_or_none():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Point with id {id} not found")
    db_point.update(vals)
    db.commit()
    return model


def delete_point(db: Session, id: int):
    db_point = db.query(models.Point).filter(models.Point.id == id)
    if not db_point.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Point with id {id} not found")
    db_point.delete(synchronize_session=False)
    db.commit()
    return {'status': 'done'}


# Boat


def create_boat(db: Session, boat: schemas.BoatAdd):
    db_boat = models.Boat(
        name=boat.name, org_id=boat.org_id)
    db.add(db_boat)
    db.commit()
    db.refresh(db_boat)
    return db_boat


def select_boats(db: Session):
    return db.query(models.Boat)


def select_boat(db: Session, id: int):
    return db.query(models.Boat).filter(models.Boat.id == id)


def get_boats(db: Session):
    return select_boats(db).all()


def get_boat(db: Session, id: int):
    return select_boat(db, id).first()


def update_boat(db: Session, boat: schemas.BoatAdd):
    vals = boat.dict()
    model = models.Boat(**boat.dict())
    db_boat = db.query(models.Boat).filter(models.Boat.id == model.id)
    if not db_boat.one_or_none():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Boat with id {id} not found")
    db_boat.update(vals)
    db.commit()
    return model


def delete_boat(db: Session, id: int):
    db_boat = db.query(models.Boat).filter(models.Boat.id == id)
    if not db_boat.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Boat with id {id} not found")
    db_boat.delete(synchronize_session=False)
    db.commit()
    return {'status': 'done'}

# Storage


def create_storage(db: Session, storage: schemas.StorageAdd):
    db_storage = models.Storage(
        name=storage.name,
        org_id=storage.org_id,
        point_id=storage.point_id,
        cargo_id=storage.cargo_id)
    db.add(db_storage)
    db.commit()
    db.refresh(db_storage)
    return db_storage


def select_storages(db: Session):
    return db.query(models.Storage)


def select_storage(db: Session, id: int):
    return db.query(models.Storage).filter(models.Storage.id == id)


def get_storages(db: Session):
    return select_storages.all()


def get_storage(db: Session, id: int):
    return select_storage(db, id).first()


def update_storage(db: Session, storage: schemas.StorageAdd):
    vals = storage.dict()
    model = models.Storage(**storage.dict())
    db_storage = db.query(models.Storage).filter(models.Storage.id == model.id)
    if not db_storage.one_or_none():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Storage with id {id} not found")
    db_storage.update(vals)
    db.commit()
    return model


def delete_storage(db: Session, id: int):
    db_storage = db.query(models.Storage).filter(models.Storage.id == id)
    if not db_storage.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Storage with id {id} not found")
    db_storage.delete(synchronize_session=False)
    db.commit()
    return {'status': 'done'}
