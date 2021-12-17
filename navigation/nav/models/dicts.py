from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from auth.database import Base


class Unit(Base):
    __tablename__ = "units"

    id = Column("id", Integer, autoincrement=True,
                primary_key=True, index=True)
    name = Column("name", String(255), index=True)
    short_name = Column("short_name", String(12), index=True)


class Cargo(Base):
    __tablename__ = "cargos"
    id = Column("id", Integer, autoincrement=True,
                primary_key=True, index=True)
    name = Column("name", String(255), index=True)
    unit_id = Column("unit_id", ForeignKey('units.id'))
    unit = relationship(Unit)


class Region(Base):
    __tablename__ = "regions"

    id = Column("id", Integer, autoincrement=True,
                primary_key=True, index=True)
    name = Column("name", String(255), index=True)


class Locality(Base):
    __tablename__ = "localities"

    id = Column("id", Integer, autoincrement=True,
                primary_key=True, index=True)
    name = Column("name", String(255), index=True)
    region_id = Column("region_id", ForeignKey("regions.id"))
    region = relationship(Region)


class Rival(Base):
    __tablename__ = "rivals"

    id = Column("id", Integer, autoincrement=True,
                primary_key=True, index=True)
    name = Column("name", String(255), index=True)


class Org(Base):
    __tablename__ = "orgs"

    id = Column("id", Integer, autoincrement=True,
                primary_key=True, index=True)
    name = Column("name", String(255), index=True)
    inn = Column("inn", String(255), index=True)
    address = Column("address", String(255), index=True)
    phone = Column("phone", String(255), index=True)


class Point(Base):
    __tablename__ = "points"

    id = Column("id", Integer, autoincrement=True,
                primary_key=True, index=True)
    name = Column("name", String(255), index=True)
    local_id = Column("local_id", ForeignKey("localities.id"))
    rival_id = Column("rival_id", ForeignKey("rivals.id"))
    locality = relationship(Locality)
    rival = relationship(Rival)


class Boat(Base):
    __tablename__ = "boats"

    id = Column("id", Integer, autoincrement=True,
                primary_key=True, index=True)
    name = Column("name", String(255), index=True)
    org_id = Column("org_id", ForeignKey("orgs.id"))
    org = relationship(Org)


class Storage(Base):
    __tablename__ = "storages"

    id = Column("id", Integer, autoincrement=True,
                primary_key=True, index=True)
    name = Column("name", String(255), index=True)
    org_id = Column("org_id", ForeignKey("orgs.id"))
    point_id = Column("point_id", ForeignKey("points.id"))
    cargo_id = Column("cargo_id", ForeignKey("cargos.id"))
    point = relationship(Point)
    cargos = relationship(Cargo)
