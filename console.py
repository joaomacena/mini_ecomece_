from datetime import datetime
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork
from src.services.category_service import create_category
from src.services.supplier_service import create_supplier
from src.services.product.product_service import create_product, create_discount
from src.services.payment_method_service import create_payment_method
from src.services.product_discount_service import create_product_discount
from src.services.customer_service import create_customer, create_address


from src.adapter.database import Session
from src.adapter.orm import start_mapper


start_mapper()

db = Session()

uow = SqlAlchemyUnitOfWork(db)

#create_customer(fist_name='joa',last_name='ped',phone_number='123',genre='h',document_id='12345',birth_date=datetime.now(),uow=uow)
#create_address('tes1','sp','sp','123','44','sao',True,1, uow)
create_category('cat 9', uow)

create_supplier('sup 9', uow)
#create_payment_method('dinheiro', True, uow)

#create_product(description='23123fafafa',price=10.0,technical_details='da',image='daf',visible=True,category_id=1,supplier_id=1,uow=uow)

#create_discount('value', 100, 1,1, uow)

# prod.add_discount(discount = des)


# with uow:
#   pm = PaymentMethod(name='pix', enabled=True, id=1)
#   uow.payment_method_repository.add(pm)


#   c = Category(name='eletronico')
#   uow.category_repository.add(c)
#   s = Supplier(name='HP')
#   uow.supplier_repository.add(s)


#   p = Product(description='descricao 2', price=10, technical_details='detalhes tecnicos', image='', visible=True, category=c, supplier=s)
#   pd = ProductDiscount(mode='value', value=100, payment_method=pm)
#   p.add_discount(pd)

#   uow.product_repository.add(p)

#   print(len(p.discounts))

#   pm2 = PaymentMethod(name='boleto', enabled=True, id=2)
#   uow.payment_method_repository.add(pm2)

#   # pd2 = ProductDiscount(mode='percetage', value=100, payment_method=pm2)
#   # p.add_discount(pd2)


# payment_method_repository = PaymentMethodRepository(db, PaymentMethod)
# category_repository = CategoryRepository(db, Category)
# supplier_repository = SupplierRepository(db, Supplier)
# product_repository = ProductRepository(db, Product)


# ================= 
# Populando o banco de dados





# Adicionando um novo desconto

# p = db.query(Product).filter_by(id=1).first()

# # pm = db.query(PaymentMethod).filter_by(id=1).first()
# pm = PaymentMethod('cartão de crédito', enabled=True, id=3)

# pd = ProductDiscount(mode='value', value=100, payment_method=pm)

# print(len(p.discounts))


# p.add_discount(pd)

# print(p.id)
# db.commit()
# db.close()


# Buscando um desconto no banco de dados

# pd = db.query(ProductDiscount).filter_by(id=1).first()

# print(pd.value)
# print(pd.payment_method.name)


