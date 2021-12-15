from sqlalchemy import Column, String, Integer, Float, Date, DateTime, Boolean
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from navigation.nav.models import dicts
from auth.database import Base


class Decada(Base):
    __tablename__ = "decadas"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    part = Column(Integer, index=True)
    month = Column(Integer, index=True)
    year = Column(Integer, index=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    org_id = Column(Integer, ForeignKey(dicts.Org.id), unique=True)
    org = relationship(dicts.Org, uselist=False)


class Supplier(Base):
    __tablename__ = "suppliers"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    org_id = Column(Integer, ForeignKey(dicts.Org.id), unique=True)
    org = relationship(dicts.Org, uselist=False)


class Carrier(Base):
    __tablename__ = "carriers"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    org_id = Column(Integer, ForeignKey(dicts.Org.id), unique=True)
    org = relationship(dicts.Org, uselist=False)


class Owner(Base):
    __tablename__ = "owners"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    org_id = Column(Integer, ForeignKey(dicts.Org.id), unique=True)
    org = relationship(dicts.Org, uselist=False)


class Bid(Base):
    __tablename__ = "bids"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    point_id = Column(Integer, ForeignKey("points.id"))
    cargo_id = Column(Integer, ForeignKey("cargos.id"))
    quantity = Column(Float)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    created_date = Column(DateTime, default=datetime.today)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    point = relationship(dicts.Point, uselist=False)
    cargo = relationship(dicts.Cargo, uselist=False)
    #customer = relationship(Customer, uselist=False)
    #supplier_id = relationship(Supplier, uselist=False)


class BidConfirm(Base):
    __tablename__ = "bid_confirm"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    bid_id = Column(Integer, ForeignKey("bids.id"))
    is_confirm = Column(Boolean, nullable=True)
    confirm_date = Column(DateTime, default=datetime.today)
    description = Column(String(255), nullable=True)
    bid = relationship(Bid, backref="bid_confirm")


class BidDelivery(Base):
    __tablename__ = "bid_deliveries"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    bid_id = Column(Integer, ForeignKey("bids.id"))
    start_point = Column(Integer, ForeignKey("points.id"))
    end_point = Column(Integer, ForeignKey("points.id"))
    quantity = Column(Float)
    carrier_id = Column(Integer, ForeignKey("carriers.id"))
    created_date = Column(DateTime, default=datetime.today)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)


class BidDeliveryConfirm(Base):
    __tablename__ = "bid_delivery_confirm"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    delivery_id = Column(Integer, ForeignKey("bid_deliveries.id"))
    is_confirm = Column(Boolean, nullable=True)
    confirm_date = Column(DateTime, default=datetime.today)
    description = Column(String(255), nullable=True)
    bid_delivery = relationship(BidDelivery, backref="bid_delivery_confirm")


class BidOwnerConfirm(Base):
    __tablename__ = "bid_owner_confirm"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    bid_id = Column(Integer, ForeignKey("bids.id"))
    is_confirm = Column(Boolean, nullable=True)
    confirm_date = Column(DateTime, default=datetime.today)
    description = Column(String(255), nullable=True)
    bid = relationship(Bid, backref="bid_owner_confirm")
