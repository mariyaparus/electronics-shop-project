from src.item import Item


class KeyboardLangMixin:
    languages = ('EN', 'RU')

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language):
        if language in self.languages:
            self.__language = language
        else:
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self

    def __str__(self):
        return self.__language


class Keyboard(KeyboardLangMixin, Item):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.__language = 'EN'

    def __str__(self):
        return self.name
