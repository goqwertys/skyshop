import pytest

from src.models import Product


@pytest.fixture
def product():
    return Product(
        "Apple",
        "Fresh apple",
        10.0,
        5
    )
