import json
import logging
import os

from src.config import LOG_LEVEL
from src.paths import get_project_root

# Logger init
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)
log_path = os.path.join(get_project_root(), 'logs', f'{__name__}.log')
fh = logging.FileHandler(log_path, mode='w')
formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


class Product:
    """ Represents a product """

    def __init__(self, name: str, description: str, price: float, count: int):
        """ Initialization of a new product """
        self.name = name
        self.description = description
        self.price = price
        self.count = count


class Category:
    """Represents a category of products"""
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str):
        """ Initialization of a category """
        self.name = name
        self.description = description
        self.products = []
        Category.category_count += 1

    def add_product(self, product: Product):
        """ Add product to products list """
        if product not in self.products:
            self.products.append(product)
            Category.product_count += 1


def load_categories_from_json(filepath) -> list[Category] | list[None]:
    """ Load categories and products from a JSON file """
    logger.info(f"Loading categories from JSON file: {filepath}")
    try:
        with open(filepath, 'r', encoding="utf-8") as f:
            data = json.load(f)

        categories = []
        for category_data in data:
            logger.info(f"Creating category: {category_data['name']}")
            category = Category(category_data["name"], category_data["description"])
            for product_data in category_data:
                logger.info(f"Creating product: {product_data['name']} for category: {category.name}")
                product = Product(
                    product_data["name"],
                    product_data["description"],
                    product_data["price"],
                    product_data["quantity"]
                )
                category.add_product(product)
            categories.append(category)
        logger.info(f"Loaded {len(categories)} categories and {Category.product_count} products")
        return categories

    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
        return []
    except json.JSONDecodeError:
        logger.error(f"JSON decode error in file: {filepath}")
        return []

    except Exception as e:
        logger.error(f"An error has occurred: {e}")
        return []
