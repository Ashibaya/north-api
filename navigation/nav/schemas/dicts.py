from typing import Optional
from pydantic import BaseModel
from pydantic.types import constr


class UnitBaseModel(BaseModel):
    id: Optional[int] = None
    name: Optional[constr(max_length=255)] = None
    short_name: Optional[constr(max_length=12)] = None


class UnitAdd(UnitBaseModel):
    class Config:
        orm_mode = True


class UnitShow(UnitBaseModel):
    class Config:
        orm_mode = True


class CargoBaseModel(BaseModel):
    id: Optional[int] = None
    name: Optional[constr(max_length=255)]


class CargoAdd(CargoBaseModel):
    unit_id: Optional[int] = None

    class Config:
        orm_mode = True


class CargoShow(CargoAdd):
    unit: Optional[UnitShow]


class RegionBaseModel(BaseModel):
    id: Optional[int] = None
    name: Optional[constr(max_length=255)]


class RegionAdd(RegionBaseModel):
    class Config:
        orm_mode = True


class RegionShow(RegionBaseModel):
    class Config:
        orm_mode = True


class LocalityBaseModel(BaseModel):
    id: Optional[int] = None
    name: Optional[constr(max_length=255)]


class LocalityAdd(LocalityBaseModel):
    region_id: Optional[int] = None

    class Config:
        orm_mode = True


class LocalityShow(LocalityAdd):
    region: Optional[RegionShow]


class RivalBaseModel(BaseModel):
    id: Optional[int] = None
    name: Optional[constr(max_length=255)]


class RivalAdd(RivalBaseModel):
    class Config:
        orm_mode = True


class RivalShow(RivalBaseModel):
    class Config:
        orm_mode = True


class OrgBaseModel(BaseModel):
    id: Optional[int] = None
    name: Optional[constr(max_length=255)]


class OrgShow(OrgBaseModel):
    pass


class OrgAdd(OrgBaseModel):
    inn: Optional[constr(max_length=255)]
    address: Optional[constr(max_length=255)]
    phone: Optional[constr(max_length=255)]

    class Config:
        orm_mode = True


class OrgShowAll(OrgAdd):
    pass


class PointBaseModel(BaseModel):
    id: Optional[int] = None
    name: Optional[constr(max_length=255)]


class PointAdd(PointBaseModel):
    local_id: Optional[int]
    rival_id: Optional[int]

    class Config:
        orm_mode = True


class PointShow(PointAdd):
    locality: Optional[LocalityShow]
    rival: Optional[RivalShow]


class BoatBaseModel(BaseModel):
    id: Optional[int] = None
    name: Optional[constr(max_length=255)]


class BoatAdd(BoatBaseModel):
    org_id: Optional[int]

    class Config:
        orm_mode = True


class BoatShow(BoatAdd):
    org: Optional[OrgShowAll]


class StorageBaseModel(BaseModel):
    id: Optional[int] = None
    name: Optional[constr(max_length=255)]


class StorageAdd(StorageBaseModel):
    org_id: Optional[int]
    point_id: Optional[int]
    cargo_id: Optional[int]

    class Config:
        orm_mode = True


class StorageShow(StorageAdd):
    point: Optional[PointShow]
    cargos: Optional[CargoShow]
