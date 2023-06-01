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
