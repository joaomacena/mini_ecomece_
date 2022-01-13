from src.domain.customer.model import Customer
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork
from src.domain.address.model import Address

def create_customer(fist_name,last_name,phone_number,genre,
            document_id,birth_date, uow: SqlAlchemyUnitOfWork):
  with uow:
        uow.customer_repository.add(Customer(fist_name=fist_name,
                    last_name=last_name, phone_number=phone_number,
                    genre=genre, document_id=document_id, birth_date=birth_date))

        uow.commit()


def create_address(address,city,state,number,zipcode,
                    neighbourhood,primary,customer_id:int, uow: SqlAlchemyUnitOfWork):
  with uow:
        customer = uow.customer_repository.get(id=customer_id)

        if not customer:
            raise Exception('Customer not found')

        addre = Address(address=address, city=city,
                    state=state, number=number, zipcode=zipcode,
                    neighbourhood=neighbourhood, primary=primary, customer=customer)
        
        customer.add_address(addre)

        uow.commit()