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
