from sqlalchemy.orm import Session, query, session
from fastapi import HTTPException, status
from navigation.nav.schemas import nav as schemas, dicts as dict_schemas
from navigation.nav.models import nav as models, dicts as dict_models
from navigation.nav.repository import nav as nav_repo, dicts as dict_repo


def get_bid_plan(db: Session):
    return nav_repo.select_bids(db).all()
