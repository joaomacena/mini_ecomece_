from typing import List
from src.domain.address.model import Address

class Order:
    def __init__(self,number,status,customer_id,created_at,
            address_id,value,payment_form_id,total_discount):
        self.number = number
        self.status = status
        self.customer_id = customer_id
        self.created_at = created_at
        self.address_id = address_id
        self.value = value
        self.payment_form_id = payment_form_id
        self.total_discount = total_discount


class OrderStatus:
    def __init__(self,status,created_at,order_id):
        self.status = status
        self.created_at = created_at
        self.order_id = order_id


class OrderProducts:
    def __init__(self,order_id,product_id,quantity):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity

