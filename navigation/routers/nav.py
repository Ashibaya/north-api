from fastapi import APIRouter
from navigation.routers.nav_routers import customer,supplier,owner,carrier,bid,bid_confirm,bid_delivery, bid_delivery_confirm, bid_owner_confirm


router = APIRouter(
    prefix="/navi",
    tags=['Navigation']
)

# Unit

router.include_router(customer.router)
router.include_router(supplier.router)
router.include_router(owner.router)
router.include_router(carrier.router)
router.include_router(bid.router)
router.include_router(bid_confirm.router)
router.include_router(bid_delivery.router)
router.include_router(bid_delivery_confirm.router)
router.include_router(bid_owner_confirm.router)