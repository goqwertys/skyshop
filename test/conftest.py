import pytest

from src.models import Product, Category


@pytest.fixture
def product():
    return Product(
        "Apple",
        "Fresh apple",
        10.0,
        5
    )


@pytest.fixture
def category():
    return Category("Fruits", "Fresh fruits")


@pytest.fixture(autouse=True)
def reset_counters():
    Category.category_count = 0
    Category.product_count = 0
