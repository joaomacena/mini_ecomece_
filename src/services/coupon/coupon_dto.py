from dataclasses import dataclass
from datetime import date


@dataclass
class CouponDTO:
  code: str
  expire_at: date
  limit: int
  type: str
  value: float
  