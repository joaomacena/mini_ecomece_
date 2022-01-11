from src.adapter.repositories.product_repository import ProductRepository
from src.domain.product.model import Product
from src.domain.category.model import Category
from src.domain.supplier.model import Supplier
from src.adapter.database import Session
from src.adapter.orm import start_mapper

start_mapper()

db = Session()

repository = ProductRepository(db)

category = Category(name='eletronico')
supplier = Supplier(name='HP23')

product = Product(description='descricao 22', price=10, technical_details='detalhes tecnicos', image='', visible=True,
                  category=category, supplier=supplier)

repository.add(product)

print(product.id)

print(product.description)

print(product.category.id)
