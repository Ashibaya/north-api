from fastapi import APIRouter
from navigation.routers import dicts, nav, reports
from navigation.nav.models import dicts as dict_models, nav as nav_models
from auth.database import engine
router = APIRouter()

dict_models.Base.metadata.create_all(engine)
nav_models.Base.metadata.create_all(engine)

router.include_router(dicts.router)
router.include_router(nav.router)
router.include_router(reports.router)
