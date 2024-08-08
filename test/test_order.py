from src.order import Order


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
