from abc import ABC, abstractmethod

from src.product import Product
from src.exception import ZeroQuantityException


class BaseEntity(ABC):
    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def avg_price(self):
        pass


class Order(BaseEntity):
    def __init__(self, product: Product, quantity: int):
        if quantity < 1:
            raise ZeroQuantityException("Cannot create order with zero quantity")
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity
        print(f"{repr(self)} created")

    def avg_price(self):
        pass

    def __len__(self):
        return self.quantity

    def __str__(self):
        return f"{self.__class__.__name__}('{self.product.name}', {self.quantity}, {self.total_price})"
