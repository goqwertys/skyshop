import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product():
    return Product(
        "Apple",
        "Fresh apple",
        10.0,
        5
    )


@pytest.fixture
def other_product():
    return Product(
        "Bananas",
        "Yellow",
        5.0,
        10
    )


@pytest.fixture
def category():
    return Category("Fruits", "Fresh fruits")


@pytest.fixture(autouse=True)
def reset_counters():
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def cars():
    pr1 = Product("Ford T", "American classic", 100000.0, 5)
    pr2 = Product("Volkswagen Juke", "GOAT", 150000.0, 2)
    cars = Category("Cars", "Classic")
    cars.add_product(pr1)
    cars.add_product(pr2)
    return cars
