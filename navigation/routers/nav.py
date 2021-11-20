from fastapi import APIRouter
from navigation.routers.nav_routers import customer


router = APIRouter(
    prefix="/navi",
    tags=['Navigation']
)

# Unit

router.include_router(customer.router)