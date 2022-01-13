from src.domain.product_discount.model import ProductDiscount
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork


def create_product_discount(mode,value,payment_method, uow: SqlAlchemyUnitOfWork):
    with uow:
        uow.product_discont_repository.add(ProductDiscount(
            mode = mode, 
            value = value, 
            payment_method = payment_method
            ))
        uow.commit()
        
        