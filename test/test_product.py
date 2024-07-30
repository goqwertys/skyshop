from src.models import Product


def test_initialization(product):
    assert product.name == "Apple"
    assert product.description == "Fresh apple"
    assert product.price == 10.0
    assert product.count == 5


def test_price_setter_invalid_price(capsys, product):
    product.price = -5.0
    captured = capsys.readouterr()
    assert "Некорректная цена" in captured.out
    assert product.price == 10.0


def test_price_setter_lowe_price_without_confirmation(monkeypatch, product):
    monkeypatch.setattr('builtins.input', lambda _: 'n')
    product.price = 7.0
    assert product.price == 10.0


def test_price_setter_higher_price_with_confirmation(product):
    product.price = 15.0
    assert product.price == 15.0


def test_create_product_new(product):
    product_list = []
    new_product = Product.create_product("Banana", "Fresh banana", 15.0, 3, product_list)
    assert new_product.name == "Banana"
    assert new_product.description == "Fresh banana"
    assert new_product.price == 15.0
    assert new_product.count == 3
    assert len(product_list) == 1


def test_create_product_existing(monkeypatch, product):
    product_list = [product]
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    existing_product = Product.create_product("Apple", "Updated apple", 10.0, 2, product_list)
    assert existing_product.name == "Apple"
    assert existing_product.description == "Updated apple"
    assert existing_product.price == 10.0
    assert existing_product.count == 7
    assert len(product_list) == 1


def test_product_len(product):
    assert len(product) == 5


def test_product_str(product):
    assert str(product) == "Apple, 10.0 руб. Остаток: 5 шт."
