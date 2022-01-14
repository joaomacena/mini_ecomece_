from fastapi import APIRouter, status
from src.presentation.fastapi.schemas.supplier_schemas import CreateSupplierSchema
from src.domain.supplier.model import Supplier
from src.services.supplier_service import create_supplier
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(schema: CreateSupplierSchema):
  uow = SqlAlchemyUnitOfWork()
  dto = Supplier(**schema.dict())
  
  supplier = create_supplier(dto, uow=uow)

  return supplier