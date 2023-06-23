"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone
import os


@pytest.fixture
def item():
    item = Item("test item", 10.0, 5)
    yield item
    Item.all = []


@pytest.fixture
def phone():
    phone = Phone("test phone", 10, 5, 2)
    yield phone
    Phone.all = []


def test_init(item):
    assert item.name == "test item"
    assert item.price == 10.0
    assert item.quantity == 5
    assert len(Item.all) == 1


def test_repr(item):
    assert repr(item) == "Item('test item', 10.0, 5)"


def test_str(item):
    assert str(item) == 'test item'


def test_add(item, phone):
    assert item + phone == 10
    assert phone + phone == 10

    # with pytest.raises(TypeError):


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 50.0


def test_apply_discount(item):
    item.pay_rate = 0.9
    item.apply_discount()
    assert item.price == 9.0


def test_item_name_setter(item):
    item.name = 'newname'
    assert item.name == 'newname'

    with pytest.raises(ValueError):
        item.name = 'nameislongerthanten'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert Item.all[0].name == 'Смартфон'
    assert Item.all[0].price == 100
    assert Item.all[0].quantity == 1

    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(filename='test.csv')

    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(filename='error_test.csv')


def test_string_to_number():
    assert Item.string_to_number('2') == 2
    assert Item.string_to_number('3.5') == 3
