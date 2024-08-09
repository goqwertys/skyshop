import logging
import os
from abc import ABC, abstractmethod

from src.config import LOG_LEVEL
from src.logging_mixin import LoggingMixin
from src.paths import get_project_root
from src.exception import ZeroQuantityException

# Logger init
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)
log_path = os.path.join(get_project_root(), 'logs', f'{__name__}.log')
fh = logging.FileHandler(log_path, mode='w')
formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


class BaseProduct(ABC):
    @classmethod
    @abstractmethod
    def create_product(cls, *args, **kwargs):
        pass


class Product(LoggingMixin, BaseProduct):
    """ Represents a product """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """ Initialization of a new product """
        if quantity < 1:
            raise ZeroQuantityException("Cannot create product with zero quantity")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        print(f"{repr(self)} created")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            print("Некорректная цена")
            return
        if price < self.__price:
            confirmation = input(f"""Вы действительно хотите изменить цену товару {self.name}
            ({self.__price})р. --> ({price})р. (y/n)""")
            if confirmation == "y":
                self.__price = price
        else:
            self.__price = price

    @classmethod
    def create_product(
            cls,
            name: str,
            description: str,
            price: float,
            quantity: int,
            product_list: list
    ):
        """ Creates a product by checking if the same one is already in the list.\
Updates the price and description in the existing one, adds if the product is not in the list"""
        for product in product_list:
            if product.name == name:
                product.quantity += quantity
                if product.price < price:
                    product.price = price
                product.description = description
                return product

        new_product = cls(name, description, price, quantity)
        product_list.append(new_product)
        return new_product

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __len__(self):
        return self.quantity

    def __add__(self, other):
        if isinstance(other, type(self)):
            return self.__price * self.quantity + other.__price * other.quantity
        if isinstance(other, (int, float)):
            return self.__price * self.quantity + other
        raise TypeError("You can only apply add function to products of the same class.")


class SmartPhone(Product, LoggingMixin):
    """ Represents a smartphone. <- Product """
    def __init__(
            self, name: str,
            description: str,
            price: float,
            quantity: int,
            performance: int,
            model: str,
            memory: int,
            color: str
    ):
        """ SmartPhone constructor """
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product, LoggingMixin):
    """ Represents a lawn grass. <- Product """
    def __init__(
            self, name: str,
            description: str,
            price: float,
            quantity: int,
            manufacturer_country: str,
            germination_period: str,
            color: str
    ):
        """ Lawn grass constructor """
        super().__init__(name, description, price, quantity)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
        self.color = color
