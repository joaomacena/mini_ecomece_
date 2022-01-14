from fastapi import APIRouter, status
from src.presentation.fastapi.schemas.categori_schemas import CreateCategorychema
from src.domain.category.model import Category
from src.services.category_service import create_category
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(schema: CreateCategorychema):
  uow = SqlAlchemyUnitOfWork()
  
  
  category = create_category(**schema.dict(), uow=uow)

  return category