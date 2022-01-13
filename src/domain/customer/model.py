from typing import List
from src.domain.address.model import Address

class Customer:
    def __init__(self,fist_name,last_name,phone_number,genre,
            document_id,birth_date):
        self.fist_name = fist_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.genre = genre
        self.document_id = document_id
        self.birth_date = birth_date
        self.list_address: List[Address] = []


    def add_address(self, address:Address):
        if len(self.list_address)>0:
            has_address_primary:Address = list(filter(lambda x:x.primary == True , self.list_address))[0]

        if address.primary == True :
            has_address_primary.primary = False
                

        self.list_address.append(address)