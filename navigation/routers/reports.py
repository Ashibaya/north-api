from fastapi import APIRouter
from navigation.routers.report_routers import reports


router = APIRouter(
    prefix="/rep",
    tags=['Reports']
)

# Unit

router.include_router(reports.router)
