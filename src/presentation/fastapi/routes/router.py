from fastapi import APIRouter
from src.presentation.fastapi.routes.product_route import router as product_router
from src.presentation.fastapi.routes.coupon_route import router as coupon_route
from src.presentation.fastapi.routes.category_router import router as category_router
from src.presentation.fastapi.routes.supplier_route import router as supplier_route
from src.presentation.fastapi.routes.customer_router import router as customer_router
from src.presentation.fastapi.routes.payment_method_router import router as payment_method_router

router = APIRouter()

router.include_router(product_router, prefix='/products', tags=['product'])
router.include_router(coupon_route, prefix='/coupons', tags=['coupon'])
router.include_router(category_router, prefix='/categories', tags=['category'])
router.include_router(supplier_route, prefix='/suppliers', tags=['suppliers'])
router.include_router(customer_router, prefix='/customers',tags=['customer'])
router.include_router(payment_method_router, prefix='/payment_method', tags=['payment_method'])
