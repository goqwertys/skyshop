from src.product import Product, SmartPhone, LawnGrass


def test_mixin_product_repr(product):
    assert repr(product) == "Product: ('Apple', 'Fresh apple', 10.0, 5)"


def test_mixin_smartphone_repr(smartphone_1):
    assert repr(smartphone_1) == "SmartPhone: ('Smartphone', 'Description', 500.0, 2, 800, 'ModelX', 128, 'Black')"


def test_mixin_lawn_grass_repr(lawn_grass_1):
    assert repr(lawn_grass_1) == "LawnGrass: ('LawnGrass', 'Description', 20.0, 10, 'USA', 'Spring', 'Green')"
