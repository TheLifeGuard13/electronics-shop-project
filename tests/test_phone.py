import pytest

from src.item import Item
from src.phone import Phone


def test_add_phone():
    phone2 = Phone("iPhone 15 Ultra", 999_999, 1, 25)
    phone3 = Phone("iPhone 16 Ultra", 999, 2, 2)
    item7 = Item("Товар", 50, 11)
    phone3.number_of_sim = 1
    assert phone2 + phone3 == 3
    assert item7 + phone2 == 12
    with pytest.raises(Exception):
        assert phone3 + 1000
    assert phone3.__repr__() == "Phone('iPhone 16 Ultra', 999, 2, 1)"
    with pytest.raises(ValueError):
        phone3.number_of_sim = 0
