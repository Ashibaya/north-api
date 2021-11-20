from auth.routers.authentication import login
from fastapi import APIRouter
from auth.routers import login, authentication, roles
from auth.login.models import login as models
from auth.database import engine
router = APIRouter()

models.Base.metadata.create_all(engine)

router.include_router(login.router)
router.include_router(authentication.router)
router.include_router(roles.router)
