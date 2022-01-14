from fastapi import APIRouter, status
from src.presentation.fastapi.schemas.payment_method_schemas import CreatePatmentMethodSchema
from src.domain.supplier.model import Supplier
from src.services.payment_method_service import create_payment_method
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(schema: CreatePatmentMethodSchema):
  uow = SqlAlchemyUnitOfWork()
  #dto = Supplier(**schema.dict())
  
  payment_method = create_payment_method(**schema.dict(), uow=uow)

  return payment_method