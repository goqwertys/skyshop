import pytest

from src.order import Order
from src.exception import ZeroQuantityException


def test_order_init(smartphone_1):
    """ Test creation of order object """
    order_object = Order(smartphone_1, 3)
    assert order_object.quantity == 3
    assert order_object.total_price == 1500.0


def test_order_len(smartphone_1):
    order_obj = Order(smartphone_1, 3)
    assert len(order_obj) == 3


def test_order_str(smartphone_1):
    order_obj = Order(smartphone_1, 3)
    assert str(order_obj) == "Order('Smartphone', 3, 1500.0)"


def test_order_zero_exception(smartphone_1):
    with pytest.raises(ZeroQuantityException, match="Cannot create order with zero quantity"):
        _ = Order(smartphone_1, 0)
