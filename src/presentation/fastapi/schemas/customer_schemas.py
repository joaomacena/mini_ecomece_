from datetime import date
from pydantic import BaseModel

class CreateCustomerSchema(BaseModel):
  fist_name: str
  last_name: str
  phone_number: str
  genre: str
  document_id: str
  birth_date: date