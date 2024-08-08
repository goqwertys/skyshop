import pytest

from src.category import Category


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


def test_category_len(category, product):
    category.add_product(product)
    assert len(category) == 5


def test_category_str(category, product):
    category.add_product(product)
    # f"{self.name}, количество продуктов: {len(self)} шт."
    assert str(category) == "Fruits, количество продуктов: 5 шт."


def test_add_products(smartphone_1, smartphone_2, lawn_grass_1, lawn_grass_2):
    common_category = Category("Common", "Common category")
    common_category.add_product(smartphone_1)
    common_category.add_product(smartphone_2)
    common_category.add_product(lawn_grass_1)
    common_category.add_product(lawn_grass_2)
    assert smartphone_1 in common_category.products
    assert smartphone_2 in common_category.products
    assert lawn_grass_1 in common_category.products
    assert smartphone_2 in common_category.products


def test_try_add_int_type():
    with pytest.raises(TypeError):
        test_category = Category("Test", "description")
        test_category.add_product(1)


def test_try_add_str_type():
    with pytest.raises(TypeError):
        test_category = Category("Test", "description")
        test_category.add_product("Test string")


def test_try_other_class_object():
    with pytest.raises(TypeError):
        class TestClass:
            pass
        test_obj = TestClass()
        test_category = Category("Test", "description")
        test_category.add_product(test_obj)
