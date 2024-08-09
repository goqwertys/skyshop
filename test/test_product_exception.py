import pytest

from src.product import Product, SmartPhone, LawnGrass
from src.exception import ZeroQuantityException


def test_product_construct_exception():
    with pytest.raises(ZeroQuantityException):
        _ = Product("Gun", "We don't have them", 1500.0, 0)


def test_smartphone_construct_zero_quantity():
    with pytest.raises(ZeroQuantityException):
        _ = SmartPhone(
            "Nokia",
            "Old but gold",
            20.0,
            0,
            8,
            "Brick",
            16,
            "black"
        )


def test_lawn_grass_zero_quantity():
    with (pytest.raises(ZeroQuantityException)):
        _ = LawnGrass(
            "Magic Soil",
            "Doesn't exist",
            500.0,
            0,
            "Narnia",
            "Always",
            "Orange"
        )
