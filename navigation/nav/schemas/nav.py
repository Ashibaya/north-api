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
    id: int
    org_id: int

class Customer(CustomerBaseModel):
    class Config:
        orm_mode = True

class CustomerShow(CustomerBaseModel):
    pass

#Поставщик
class SupplierBaseModel(BaseModel):
    id: int
    org_id: int


#Перевозщик
class CarrierBaseModel(BaseModel):
    id: int
    org_id: int

    
#Владелец
class OwnerBaseModel(BaseModel):
    id: int
    org_id: int
    
#Заявка
class BidBaseModel(BaseModel):
    id: Optional[int] = None
    point_id: int
    cargo_id: int
    quantity: float
    customer_id: int
    supplier_id: int
    create_date: Optional[datetime] = None
    start_date: date
    end_date: date

#Подтверждение заявки
class BidConfirmBaseModel(BaseModel):
    id: Optional[int] = None
    bid_id: int
    is_confirm: Optional[bool] = None
    confirm_date: Optional[datetime] = None
    description: Optional[str] = None

#Доставка заявки
class BidDeliveryBaseModel(BaseModel):
    id: Optional[int] = None
    bid_id: int
    start_point: int
    end_point: int
    quantity: float
    carrier_id: int
    created_date: Optional[datetime] = None
    start_date: date
    end_date: date

#Подтверждение доставки
class BidDeliveryConfirmBaseModel(BaseModel):
    id: Optional[int] = None
    bid_delivery_id: int
    is_confirm: Optional[bool] = None
    confirm_date: Optional[datetime] = None
    description: Optional[str] = None


#подтверждение заявки владельцем
class BidOwnerConfirm(BaseModel):
    id: Optional[int]= None
    bid_id: int
    is_confirm: Optional[bool] = None
    confirm_date: Optional[datetime] = None
    description: Optional[str]= None
