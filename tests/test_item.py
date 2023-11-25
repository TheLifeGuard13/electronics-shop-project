from pathlib import Path

import pytest

from src.item import Item

DATA_PATH = Path(__file__).parent.parent.joinpath("src", "items.csv")
DATA_PATH_EMPTY = Path(__file__).parent.parent.joinpath("tests", "tests_data", "empty.csv")
DATA_PATH_WRONG = Path(__file__).parent.parent.joinpath("tests", "tests_data", "wrong.csv")
DATA_PATH_WRONG_NAME = Path(__file__).parent.parent.joinpath("tests", "tests_data", "wrong_name.csv")


@pytest.fixture
def one_item():
    return Item("Изделие", 149.99, 2)


def test_calculate_total_price(one_item):
    assert one_item.calculate_total_price() == one_item.price * one_item.quantity


def test_apply_discount(one_item):
    one_item.apply_discount()
    assert one_item.price == 149.99 * one_item.pay_rate


def test_name(one_item):
    one_item.name = "Ноутбук"
    assert one_item.name == "Ноутбук"
    one_item.name = "Ультраноутбук"
    assert one_item.name == "Ультраноут"


def test_instantiate_from_csv():
    Item.instantiate_from_csv(DATA_PATH)
    assert len(Item.all) == 5
    item_one = Item.all[0]
    assert item_one.name == "Смартфон"
    with pytest.raises(FileNotFoundError):
        assert Item.instantiate_from_csv("file.csv")
    with pytest.raises(AssertionError):
        assert Item.instantiate_from_csv(DATA_PATH_EMPTY)
    with pytest.raises(ValueError):
        assert Item.instantiate_from_csv(DATA_PATH_WRONG)
    with pytest.raises(ValueError):
        assert Item.instantiate_from_csv(DATA_PATH_WRONG_NAME)


def test_string_to_number():
    assert Item.string_to_number("3") == 3
    assert Item.string_to_number("3.25") == 3
    assert Item.string_to_number("3.5674") == 3
