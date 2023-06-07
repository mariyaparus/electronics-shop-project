"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item


@pytest.fixture
def item():
    item = Item("test item", 10.0, 5)
    yield item
    Item.all = []


def test_init(item):
    assert item.name == "test item"
    assert item.price == 10.0
    assert item.quantity == 5
    assert len(Item.all) == 1


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


# Тест на чтение данных из CSV-файла
def test_instantiate_from_csv():

    # Проверяем, что данные были успешно считаны из файла
    Item.instantiate_from_csv()
    assert Item.all[0].name == 'Смартфон'
    assert Item.all[0].price == 100
    assert Item.all[0].quantity == 1


# Тест на преобразование строки в число
def test_string_to_number():
    assert Item.string_to_number('2') == 2
    assert Item.string_to_number('3.5') == 3
