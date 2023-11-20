import pytest

from src.item import Item


@pytest.fixture
def one_item():
    return Item("Изделие", 149.99, 2)


def test_calculate_total_price(one_item):
    assert one_item.calculate_total_price() == one_item.price * one_item.quantity


def test_apply_discount(one_item):
    one_item.apply_discount()
    assert one_item.price == 149.99 * one_item.pay_rate
