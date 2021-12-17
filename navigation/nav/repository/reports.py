from sqlalchemy.orm import Session, query, session, aliased
from fastapi import HTTPException, status
from sqlalchemy import func, case
from sqlalchemy.sql import extract
from navigation.nav import models
from navigation.nav.schemas import nav as nav_schemas, dicts as dict_schemas
from navigation.nav.models import nav as nav_models, dicts as dict_models
from navigation.nav.repository import nav as nav_repo, dicts as dict_repo


def get_bid_plan(db: Session):
    bid = nav_models.Bid
    confirm_query = db.query(nav_models.BidOwnerConfirm).filter(
        nav_models.BidOwnerConfirm.is_confirm == True)
    confirm = aliased(confirm_query.subquery(), "confirm")

    bids = nav_repo.select_bids(db).join(confirm, bid.id == confirm.columns.bid_id)\
        .group_by(
        bid.customer_id,
        bid.cargo_id,
        bid.point_id,
        bid.end_point_id,
        extract('month', nav_models.Bid.end_date).label("month"),
        extract('year', nav_models.Bid.end_date).label("year"),
    )\
        .with_entities(
            bid.customer_id,
            bid.cargo_id,
            bid.point_id,
            bid.end_point_id,
            extract('month', nav_models.Bid.end_date).label("month"),
            extract('year', nav_models.Bid.end_date).label("year"),
            func.sum(nav_models.Bid.quantity).label("total")
    )
    print(bids)
    return bids.all()


def get_bid_delivery(db: Session):
    dayquery = extract('day', nav_models.BidDelivery.end_date)
    caseblock = case(
        [
            (0 < dayquery < 11, 1),
            (11 < dayquery < 21, 2),
            (dayquery > 21, 3)
        ]
    )
    delivery_confirm_query = db.query(nav_models.BidDeliveryConfirm)\
        .filter(nav_models.nav_models.BidDeliveryConfirm.is_confirm == True)
    delivery_confirm = aliased(
        delivery_confirm_query.subquery(), "delivery_confirm")
    delivery_query = db.query(nav_models.BidDelivery)\
        .join(delivery_confirm, nav_models.BidDelivery.id == delivery_confirm.columns.delivery_id)
    print(delivery_query)
    return delivery_query.all()


def get_bid_plan_stat(db: Session, year: int, month: int, customer_id: int):
    bids = nav_repo.select_bids(db)
    by_year = bids if year == 0 else bids.filter(
        extract('year', nav_models.Bid.end_date) == year)
    by_month = by_year if month == 0 else by_year.filter(
        extract('month', nav_models.Bid.end_date) == month)
    res = by_month.filter(nav_models.Bid.customer_id ==
                          customer_id) if customer_id != 0 else by_month
    return res.group_by(nav_models.Bid.customer_id).\
        join(nav_models.Customer).\
        join(dict_models.Org).\
        with_entities(dict_models.Org.name, func.count().label("count"))\
        .all()
