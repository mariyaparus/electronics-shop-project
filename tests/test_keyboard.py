from src.keyboard import Keyboard
import pytest


@pytest.fixture
def keyboard():
    keyboard = Keyboard("test keyboard", 10, 5)
    yield keyboard


def test_init(keyboard):
    assert keyboard.name == "test keyboard"
    assert keyboard.price == 10.0
    assert keyboard.quantity == 5
    assert keyboard.language == "EN"


def test_str(keyboard):
    assert str(keyboard) == "test keyboard"
    # assert str(keyboard.language) == "EN"


def test_change_language(keyboard):

    assert keyboard.language == "EN"

    keyboard.change_lang()
    assert keyboard.language == "RU"

    keyboard.change_lang()
    assert keyboard.language == "EN"


# def test_setter(keyboard):
#
#     assert keyboard.language == "EN"
#
#     keyboard.language = "RU"
#     assert keyboard.language == "RU"
#
#     with pytest.raises(AttributeError):
#         keyboard.language = "CH"
