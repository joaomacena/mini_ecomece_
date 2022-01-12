from typing import List
from src.domain.address.model import Address

class Customer:
    def __init__(self,fist_name,last_name,phone_number,genre,
            document_id,birth_Date):
        self.fist_name = fist_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.genre = genre
        self.document_id = document_id
        self.birth_Date = birth_Date
        self.list_address: List[Address] = []


    def add_address(self, address:Address):
        
        if len(self.list_address)>0:
            has_address_primary:Address = (filter(lambda x:x.primary == True , self.list_address))

        if address.primary == True :
            if has_address_primary:
                has_address_primary.primary = False
                self.list_address[has_address_primary.id] = has_address_primary

        self.list_address.append(address)