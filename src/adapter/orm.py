from sqlalchemy import Table
from sqlalchemy.orm import mapper
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Boolean, Float, Integer, String
from src.adapter.database import Base
from src.domain.product.model import Product

metadata = Base.metadata

table_product = Table(
  'products', 
  metadata, 
  Column('id', Integer, primary_key=True, autoincrement=True),
  Column('description', String(100)),
  Column('technical_details', String(255)),
  Column('price', Float(10, 2)),
  Column('visible', Boolean),
)

def start_mapper():
  mapper(Product, table_product)