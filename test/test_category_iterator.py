from src.category import Category, CategoryIterator
from src.product import Product


def test_category_iterator_returns_all_products(cars):
    pr1 = Product("Ford T", "American classic", 100000.0, 5)
    pr2 = Product("Volkswagen Juke", "GOAT", 150000.0, 2)
    cars = Category("Cars", "Classic")
    cars.add_product(pr1)
    cars.add_product(pr2)
    iterator = CategoryIterator(cars)
    assert list(iterator) == [pr1, pr2]
