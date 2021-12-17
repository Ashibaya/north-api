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
    dayquery = extract('day', nav_models.Bid.end_date)
    caseblock = case(
        [
            (dayquery < 11, 1),
            (dayquery < 21, 2),
            (dayquery > 21, 3)
        ]
    )
    bids = nav_repo.select_bids(db).join(confirm, bid.id == confirm.columns.bid_id)\
        .group_by(bid.id,
                  bid.customer_id,
                  bid.cargo_id,
                  bid.point_id,
                  extract('month', nav_models.Bid.end_date).label("month"),
                  extract('year', nav_models.Bid.end_date).label("year"),
                  caseblock.label("decade"))\
        .with_entities(
            bid.id,
            bid.customer_id,
            bid.cargo_id,
            bid.point_id,
            extract('month', nav_models.Bid.end_date).label("month"),
            extract('year', nav_models.Bid.end_date).label("year"),
            caseblock.label("decade"),
            func.sum(nav_models.Bid.quantity).label("total")
    )
    print(bids)
    return bids.all()


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
