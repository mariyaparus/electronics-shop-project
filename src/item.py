import csv
import os


class InstantiateCSVError(Exception):
    """Класс исключение для отлова ошибок чтения CSV файла"""

    def __init__(self, message):
        self.message = message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        else:
            raise TypeError("Невозможно сложить с экземплярами не классов Phone и Item")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self.__name = value
        else:
            raise ValueError("Длина наименования товара превышает 10 символов")

    @classmethod
    def instantiate_from_csv(cls, filename='items.csv'):
        cls.all.clear()
        op_file = os.path.join(os.path.dirname(__file__), filename)
        try:
            with open(op_file, newline='', encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    name = row['name']
                    price = cls.string_to_number(row['price'])
                    quantity = int(row['quantity'])
                    cls(name, price, quantity)
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')
        except (KeyError, ValueError):
            raise InstantiateCSVError('Файл item.csv поврежден')


    @staticmethod
    def string_to_number(s):
        # return float(s) if '.' in s else int(s)
        return int(float(s))
