# import json
# import logging
# import os
#
# from src.config import LOG_LEVEL
# from src.paths import get_project_root
#
# # Logger init
# logger = logging.getLogger(__name__)
# logger.setLevel(LOG_LEVEL)
# log_path = os.path.join(get_project_root(), 'logs', f'{__name__}.log')
# fh = logging.FileHandler(log_path, mode='w')
# formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s')
# fh.setFormatter(formatter)
# logger.addHandler(fh)
#
#
# class Product:
#     """ Represents a product """
#
#     def __init__(self, name: str, description: str, price: float, count: int):
#         """ Initialization of a new product """
#         self.name = name
#         self.description = description
#         self.__price = price
#         self.count = count
#
#     @property
#     def price(self):
#         return self.__price
#
#     @price.setter
#     def price(self, price):
#         if price < 0:
#             print("Некорректная цена")
#             return
#         if price < self.__price:
#             confirmation = input(f"""Вы действительно хотите изменить цену товару {self.name}
#             ({self.__price})р. --> ({price})р. (y/n)""")
#             if confirmation == "y":
#                 self.__price = price
#         else:
#             self.__price = price
#
#     @classmethod
#     def create_product(
#             cls,
#             name: str,
#             description: str,
#             price: float,
#             count: int,
#             product_list: list
#     ):
#         """ Creates a product by checking if the same one is already in the list.
#         Updates the price and description in the existing one, adds if the product is not in the list"""
#         for product in product_list:
#             if product.name == name:
#                 product.count += count
#                 if product.price < price:
#                     product.price = price
#                 product.description = description
#                 return product
#
#         new_product = cls(name, description, price, count)
#         product_list.append(new_product)
#         return new_product
#
#     def __str__(self):
#         return f"{self.name}, {self.__price} руб. Остаток: {self.count} шт."
#
#     def __len__(self):
#         return self.count
#
#     def __add__(self, other):
#         if isinstance(other, Product):
#             return self.__price * self.count + other.__price * other.count
#
#
# class Category:
#     """Represents a category of products"""
#     category_count = 0
#     product_count = 0
#
#     def __init__(self, name: str, description: str):
#         """ Initialization of a category """
#         self.name = name
#         self.description = description
#         self.__products = []
#         Category.category_count += 1
#
#     def add_product(self, product: Product):
#         """ Add product to products list """
#         if product not in self.__products:
#             self.__products.append(product)
#             Category.product_count += 1
#
#     @property
#     def products(self):
#         return self.__products
#
#     def print_products(self):
#         for product in self.__products:
#             print(product)
#
#     def __len__(self):
#         return sum(len(prod) for prod in self.__products)
#
#     def __str__(self):
#         return f"{self.name}, количество продуктов: {len(self)} шт."
#
#
# class CategoryIterator:
#     def __init__(self, category: Category):
#         self.__category = category
#
#     def __iter__(self):
#         self.__products = self.__category.products
#         self.__index = -1
#         return self
#
#     def __next__(self):
#         if self.__index >= len(self.__products) - 1:
#             raise StopIteration
#         else:
#             self.__index += 1
#             return self.__products[self.__index]
#
#
# def load_categories_from_json(filepath) -> list[Category] | list[None]:
#     """ Loads categories and products from a JSON file """
#     logger.info(f"Loading categories from JSON file: {filepath}")
#     try:
#         with open(filepath, 'r', encoding="utf-8") as f:
#             data = json.load(f)
#
#         categories = []
#         for category_data in data:
#             logger.info(f"Creating category: {category_data['name']}")
#             category = Category(category_data["name"], category_data["description"])
#             for product_data in category_data["products"]:
#                 logger.info(f"Creating product: {product_data['name']} for category: {category.name}")
#                 product = Product(
#                     product_data["name"],
#                     product_data["description"],
#                     product_data["price"],
#                     product_data["quantity"]
#                 )
#                 category.add_product(product)
#             categories.append(category)
#         logger.info(f"Loaded {len(categories)} categories and {Category.product_count} products")
#         return categories
#
#     except FileNotFoundError:
#         logger.error(f"File not found: {filepath}")
#         return []
#     except json.JSONDecodeError:
#         logger.error(f"JSON decode error in file: {filepath}")
#         return []
#
#     except Exception as e:
#         logger.error(f"An error has occurred: {e}")
#         return []
#
#
# class SmartPhone(Product):
#     """ Represents a smartphone. <- Product """
#     def __init__(
#             self, name: str,
#             description: str,
#             price: float,
#             count: int,
#             performance: int,
#             model: str,
#             memory: int,
#             color: int
#     ):
#         super().__init__(name, description, price, count)
#         self.performance = performance
#         self.model = model
#         self.memory = memory,
#         self.color = color
#
#
# class LawnGrass(Product):
#     """ Represents a lown grass. <- Product """
#     def __init__(
#             self, name: str,
#             description: str,
#             price: float,
#             count: int,
#             manufacturer_country: str,
#             germination_period: str,
#             color: str
#     ):
#         super().__init__(name, description, price, count)
#         self.manufacturer_country = manufacturer_country
#         self.germination_period = germination_period
#         self.color = color
