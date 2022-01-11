from sqlalchemy import Table
from sqlalchemy.orm import mapper, relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, Float, Integer, String, DATETIME
from src.adapter.database import Base
from src.domain.product.model import Product
from src.domain.category.model import Category
from src.domain.supplier.model import Supplier
from src.domain.coupon.model import Coupon

metadata = Base.metadata

table_supplier = Table(
    'suppliers',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(50))
)

table_category = Table(
    'categories',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(50))
)

table_product = Table(
    'products',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('description', String(100)),
    Column('technical_details', String(255)),
    Column('price', Float(10, 2)),
    Column('visible', Boolean),
    Column('category_id', ForeignKey('categories.id')),
    Column('supplier_id', ForeignKey('suppliers.id'))
)


table_coupon = Table(
    'coupons',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('code', String(50), unique=True),
    Column('expire_at', DATETIME),
    Column('limit', Integer),
    Column('type', String(10)),
    Column('value', Float(10, 2))
)


table_method_repository = Table(
    'payment_methods',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(45)),
    Column('enabled', Boolean, default=True)
)

table_product_discount = Table(
    'product_discounts',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),

)


def start_mapper():
    category_mapper = mapper(Category, table_category)
    supplier_mapper = mapper(Supplier, table_supplier)

    mapper(Product, table_product, properties={
        'category': relationship(category_mapper),
        'supplier': relationship(supplier_mapper)
    })

    mapper(Coupon, table_coupon)
    mapper(Coupon, table_coupon)