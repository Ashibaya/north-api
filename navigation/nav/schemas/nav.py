from typing import Optional
from pydantic import BaseModel
from pydantic.types import constr
from datetime import date, datetime

#Декады
class DecadaBaseModel(BaseModel):
    id: Optional[int] = None
    part: int
    month: int
    year: int
    start_date: date
    end_date: date


class Decada(DecadaBaseModel):
    class Config:
        orm_mode = True

class DecadaShow(DecadaBaseModel):
    pass    

#Заказчик

class CustomerBaseModel(BaseModel):
    id: Optional[int] = None
    org_id: int

class Customer(CustomerBaseModel):
    class Config:
        orm_mode = True

class CustomerShow(CustomerBaseModel):
    pass

#Поставщик
class SupplierBaseModel(BaseModel):
    id: Optional[int] = None
    org_id: int

class Supplier(SupplierBaseModel):
    class Config:
        orm_mode = True
#Перевозщик
class CarrierBaseModel(BaseModel):
    id: Optional[int] = None
    org_id: int
class Carrier(CarrierBaseModel):
    class Config:
        orm_mode = True

#Владелец
class OwnerBaseModel(BaseModel):
    id: Optional[int] = None
    org_id: int
class Owner(OwnerBaseModel):
    class Config:
        orm_mode = True    
#Заявка
class BidBaseModel(BaseModel):
    point_id: int
    cargo_id: int
    quantity: float
    customer_id: int
    supplier_id: int
    start_date: date
    end_date: date

class BidCreate(BidBaseModel):
    class Config:
        orm_mode = True

class Bid(BidBaseModel):
    id: Optional[int] = None
    created_date: Optional[datetime] = None
    class Config:
        orm_mode = True
class BidShow(Bid):
    point_name: str
    cargo_name: int
    customer_name: int
    supplier_name: int

#Подтверждение заявки
class BidConfirmBaseModel(BaseModel):
    bid_id: int
    is_confirm: Optional[bool] = None
    description: Optional[str] = None

class BidConfirmCreate(BidConfirmBaseModel):
    class Config:
        orm_mode = True

class BidConfirmShow(BidConfirmBaseModel):
    id: Optional[int] = None
    confirm_date: Optional[datetime] = None
    bid: Optional[BidShow] = None
    class Config:
        orm_mode = True


#Доставка заявки
class BidDeliveryBaseModel(BaseModel):
    bid_id: int
    start_point: int
    end_point: int
    quantity: float
    carrier_id: int
    start_date: date
    end_date: date

class BidDeliveryCreate(BidDeliveryBaseModel):
    class Config:
        orm_mode = True

class BidDeliveryShow(BidDeliveryBaseModel):
    id: Optional[int] = None
    created_date: Optional[datetime] = None
    bid: Optional[BidShow] = None
    carrier_name: str
    class Config:
        orm_mode = True
#Подтверждение доставки
class BidDeliveryConfirmBaseModel(BaseModel):
    id: Optional[int] = None
    bid_delivery_id: int
    is_confirm: Optional[bool] = None
    confirm_date: Optional[datetime] = None
    description: Optional[str] = None
    class Config:
        orm_mode = True

#подтверждение заявки владельцем
class BidOwnerConfirm(BaseModel):
    id: Optional[int]= None
    bid_id: int
    is_confirm: Optional[bool] = None
    confirm_date: Optional[datetime] = None
    description: Optional[str]= None
    class Config:
        orm_mode = True