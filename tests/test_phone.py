from src.item import Item
from src.phone import Phone
import pytest


@pytest.fixture
def phone():
    phone = Phone("test phone", 10, 5, 2)
    yield phone
    Phone.all = []


def test_init(phone):
    assert phone.name == "test phone"
    assert phone.price == 10.0
    assert phone.quantity == 5
    assert phone.number_of_sim == 2
    assert len(Phone.all) == 0


def test_str(phone):
    assert str(phone) == "test phone"


def test_repr(phone):
    assert repr(phone) == "Phone('test phone', 10, 5, 2)"


def test_number_of_sim_setter(phone):
    phone.number_of_sim = 1
    assert phone.number_of_sim == 1

    with pytest.raises(ValueError):
        phone.number_of_sim = 0
