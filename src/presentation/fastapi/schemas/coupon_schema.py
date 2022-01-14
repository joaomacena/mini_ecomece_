from datetime import date
from pydantic import BaseModel

class CreateCouponSchema(BaseModel):
  code: str
  expire_at: date
  limit: int
  type: str
  value: float