import json
import logging
import os

from src.category import Category
from src.config import LOG_LEVEL
from src.paths import get_project_root
from src.product import Product

# Logger init
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)
log_path = os.path.join(get_project_root(), 'logs', f'{__name__}.log')
fh = logging.FileHandler(log_path, mode='w')
formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


def load_categories_from_json(filepath) -> list[Category] | list[None]:
    """ Loads categories and products from a JSON file """
    logger.info(f"Loading categories from JSON file: {filepath}")
    try:
        with open(filepath, 'r', encoding="utf-8") as f:
            data = json.load(f)

        categories = []
        for category_data in data:
            logger.info(f"Creating category: {category_data['name']}")
            category = Category(category_data["name"], category_data["description"])
            for product_data in category_data["products"]:
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
