import pytest

from src.models import Category, Product


@pytest.fixture(autouse=True)
def reset_category_count():
    # Reset category count before each test
    Category.category_count = 0
    Category.product_count = 0
    yield
    # Optionally, you can add cleanup code here if needed


def test_product_initialization():
    product = Product("Laptop", "High-end laptop", 1000.0, 10)
    assert product.name == "Laptop"
    assert product.description == "High-end laptop"
    assert product.price == 1000.0
    assert product.count == 10


def test_category_initialization():
    category = Category("Electronics", "Electronic devices")
    assert category.name == "Electronics"
    assert category.description == "Electronic devices"
    assert category.products == []
    assert Category.category_count == 1


def test_add_product_to_category():
    category = Category("Electronics", "Electronic devices")
    product1 = Product("Laptop", "High-end laptop", 1000.0, 10)
    product2 = Product("Smartphone", "High-end smartphone", 800.0, 20)
    category.add_product(product1)
    category.add_product(product2)
    assert len(category.products) == 2
    assert Category.product_count == 2


def test_category_count():
    category1 = Category("Electronics", "Electronic devices")
    category2 = Category("Clothing", "Clothing items")
    assert Category.category_count == 2
