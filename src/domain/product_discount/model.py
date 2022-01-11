from src.domain.payment_method.model import PaymentMethod
from src.domain.product.model import Product


class ProductDiscount:
    def __init__(self, mode, value: float, product: Product, paymentmethod: PaymentMethod):
        self.mode = mode
        self.value = value
        self.product = product
        self.paymentmethod = paymentmethod
        