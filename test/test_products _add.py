import pytest


def test_add_two_products_same_class(product, other_product):
    assert product + other_product == 100.0


def test_add_product_smartphone(smartphone_1, smartphone_2):
    assert smartphone_1 + smartphone_2 == 1600


def test_add_product_lawn_grass(lawn_grass_1, lawn_grass_2):
    assert lawn_grass_1 + lawn_grass_2 == 400


def test_add_two_different_products(smartphone_1, lawn_grass_2):
    with pytest.raises(TypeError, match="You can only apply add function to products of the same class."):
        result = smartphone_1 + lawn_grass_2
