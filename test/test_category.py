from src.models import Category


def test_initialization(category):
    assert category.name == "Fruits"
    assert category.description == "Fresh fruits"
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_add_product(category, product):
    category.add_product(product)
    assert len(category.products) == 1
    assert category.products[0] == product
    assert Category.product_count == 1


def test_add_duplicate_product(category, product):
    category.add_product(product)
    category.add_product(product)
    assert len(category.products) == 1
    assert Category.product_count == 1


def test_print_products(capsys, category, product):
    category.add_product(product)
    category.print_products()
    captured = capsys.readouterr()
    assert "Apple, 10.0 руб. Остаток: 5 шт." in captured.out
