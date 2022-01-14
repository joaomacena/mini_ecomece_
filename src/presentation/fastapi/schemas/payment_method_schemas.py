from pydantic import BaseModel


class CreatePatmentMethodSchema(BaseModel):
    name:str
    enabled: bool