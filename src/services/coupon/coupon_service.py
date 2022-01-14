from src.domain.coupon.model import Coupon
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork
from src.services.coupon.coupon_dto import CouponDTO

def create_coupon(coupon_dto:CouponDTO, uow: SqlAlchemyUnitOfWork):
  with uow:
    coupon_code = uow.coupon_repository.get(code=coupon_dto.code)

    if coupon_code:
      raise Exception('has code in coupon')

    uow.coupon_repository.add(Coupon(
      code=coupon_dto.code,
      expire_at=coupon_dto.expire_at,
      limit=coupon_dto.limit,
      type=coupon_dto.type,
      value=coupon_dto.value
    ))
    uow.commit()