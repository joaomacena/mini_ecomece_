from src.domain.orders.model import Order, OrderProducts, OrderStatus
from src.adapter.sqlalchemy_repository import SqlAlchemyRepository


class OrderRepository(SqlAlchemyRepository[Order]):
    pass


class OrderProductsRepository(SqlAlchemyRepository[OrderProducts]):
    pass


class OrderStatusRepository(SqlAlchemyRepository[OrderStatus]):
    pass