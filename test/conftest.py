import pytest

from src.category import Category
from src.product import Product, SmartPhone, LawnGrass


@pytest.fixture
def product():
    return Product(
        "Apple",
        "Fresh apple",
        10.0,
        5
    )


@pytest.fixture
def other_product():
    return Product(
        "Bananas",
        "Yellow",
        5.0,
        10
    )


@pytest.fixture
def category():
    return Category("Fruits", "Fresh fruits")


@pytest.fixture(autouse=True)
def reset_counters():
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def cars():
    pr1 = Product("Ford T", "American classic", 100000.0, 5)
    pr2 = Product("Volkswagen Juke", "GOAT", 150000.0, 2)
    cars = Category("Cars", "Classic")
    cars.add_product(pr1)
    cars.add_product(pr2)
    return cars


@pytest.fixture
def smartphone_1():
    return SmartPhone(
        "Smartphone",
        "Description",
        500.0,
        2,
        800,
        "ModelX",
        128,
        "Black"
    )


@pytest.fixture
def smartphone_2():
    return SmartPhone(
        "Smartphone2",
        "Description2",
        600.0,
        1,
        900,
        "ModelY",
        256,
        "White")


@pytest.fixture
def lawn_grass_1():
    return LawnGrass(
        "LawnGrass",
        "Description",
        20.0,
        10,
        "USA",
        "Spring",
        "Green"
    )


@pytest.fixture
def lawn_grass_2():
    return LawnGrass(
        "LawnGrass_2",
        "Description_2",
        10.0,
        20,
        "Canada",
        "Summer",
        "Brown"
    )
