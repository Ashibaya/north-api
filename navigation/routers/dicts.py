from fastapi import APIRouter
from navigation.routers.dicts_routers import unit, cargo, region, locality, rival, org, boat, storage, point


router = APIRouter(
    prefix="/dicts",
    tags=['Dicts']
)

# Unit

router.include_router(unit.router)
router.include_router(cargo.router)
router.include_router(region.router)
router.include_router(locality.router)
router.include_router(rival.router)
router.include_router(org.router)
router.include_router(point.router)
router.include_router(boat.router)
router.include_router(storage.router)
