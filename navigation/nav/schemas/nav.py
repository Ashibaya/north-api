from typing import Optional, List
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
    org_id: int

class Customer(CustomerBaseModel):
    class Config:
        orm_mode = True

class CustomerShow(CustomerBaseModel):
    id: Optional[int] = None
    class Config:
        orm_mode = True

#Поставщик
class SupplierBaseModel(BaseModel):
    org_id: int

class Supplier(SupplierBaseModel):
    class Config:
        orm_mode = True

class SupplierShow(SupplierBaseModel):
    id: Optional[int] = None
    class Config:
        orm_mode = True

#Перевозщик
class CarrierBaseModel(BaseModel):
    org_id: int

class Carrier(CarrierBaseModel):
    class Config:
        orm_mode = True

class CarrierShow(CarrierBaseModel):
    id: Optional[int] = None
    class Config:
        orm_mode = True
#Владелец
class OwnerBaseModel(BaseModel):
    org_id: int

class Owner(OwnerBaseModel):
    class Config:
        orm_mode = True   

class OwnerShow(OwnerBaseModel):
    id: Optional[int] = None
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
    bid_delivery_id: int
    is_confirm: Optional[bool] = None
    description: Optional[str] = None


class BidDeliveryConfirmCreate(BidDeliveryConfirmBaseModel):
    class Config:
        orm_mode = True

class BidDeliveryConfirm(BidDeliveryConfirmBaseModel):
    id: Optional[int] = None
    confirm_date: Optional[datetime] = None
    class Config:
        orm_mode = True

class BidDeliveryConfirmShow(BidDeliveryConfirm):
    bid_delivery: Optional[BidDeliveryShow] = None
    

#подтверждение заявки владельцем
class BidOwnerConfirmBaseModel(BaseModel):
    bid_id: int
    is_confirm: Optional[bool] = None
    description: Optional[str]= None

class BidOwnerConfirmCreate(BidOwnerConfirmBaseModel):
    class Config:
        orm_mode = True

class BidOwnerConfirm(BidOwnerConfirmBaseModel):
    id: Optional[int]= None
    confirm_date: Optional[datetime] = None
    class Config:
        orm_mode = True

class BidOwnerConfirmShow(BidOwnerConfirm):
    bid: Optional[BidShow] = None
    bid_delivery: List[BidDeliveryShow]
    
