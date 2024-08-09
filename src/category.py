from src.order import BaseEntity
from src.product import Product


class Category(BaseEntity):
    """Represents a category of products"""
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str):
        """ Initialization of a category """
        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1

    def add_product(self, product: Product):
        """ Add product to products list """
        if not issubclass(type(product), Product):
            raise TypeError
        if product not in self.__products:
            self.__products.append(product)
            Category.product_count += 1

    @property
    def products(self):
        return self.__products

    def print_products(self):
        for product in self.__products:
            print(product)

    def __len__(self):
        return sum(len(prod) for prod in self.__products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', category quant.: {self.category_count}, \
product quant.: {self.product_count})"


class CategoryIterator:
    def __init__(self, category: Category):
        self.__category = category

    def __iter__(self):
        self.__products = self.__category.products
        self.__index = -1
        return self

    def __next__(self):
        if self.__index >= len(self.__products) - 1:
            raise StopIteration
        else:
            self.__index += 1
            return self.__products[self.__index]
