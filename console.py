from src.adapter.repositories.product_repository import ProductRepository
from src.domain.product.model import Product
from src.adapter.database import Session
from src.adapter.orm import start_mapper


start_mapper()

db = Session()

repository = ProductRepository(db)
product = Product(description='descricao 2', price=10, technical_details='detalhes tecnicos', image='', visible=True)



repository.add(product)

print(product.id)
print(product.description)
