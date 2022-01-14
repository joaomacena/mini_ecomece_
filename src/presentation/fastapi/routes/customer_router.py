from fastapi import APIRouter, status
from src.presentation.fastapi.schemas.customer_schemas import CreateCustomerSchema
from src.presentation.fastapi.schemas.address_schemas import CreateAddressSchema
from src.domain.customer.model import Customer
from src.domain.address.model import Address
from src.services.customer_service import create_address,create_customer
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(schema: CreateCustomerSchema):
  uow = SqlAlchemyUnitOfWork()
  #dto = Customer(**schema.dict())
  
  customer = create_customer(**schema.dict(), uow=uow)

  return customer


@router.post('/address', status_code=status.HTTP_201_CREATED)
def create_address(schema: CreateAddressSchema):
  uow = SqlAlchemyUnitOfWork()
  #dto = Address(**schema.dict())
  
  address = create_address(**schema.dict(), uow=uow)

  return address