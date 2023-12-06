import csv
import typing


class Item:
    """
    Класс для представления товара в магазине.
    """

    pay_rate = 1.0
    all: list = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        if not isinstance(name, str) or not isinstance(price, float | int) or not isinstance(quantity, int):
            raise ValueError("Некорректный формат входных данных")
        elif quantity < 0 or price < 0:
            raise ValueError("Некорректные значения числовых входных данных")

        self.__name = name
        self.price = price
        self.quantity = quantity
        # self.all = Item.all.append(self)

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
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if len(value) > 10:
            print("Длина наименования товара превышает 10 символов.")
        self.__name = value[:10]

    @classmethod
    def instantiate_from_csv(cls, file_name: typing.Any) -> None:
        """
        Создает экземпляры класса из файла csv.
        """
        with open(file_name, "r") as file:
            dict_reader = csv.DictReader(file, delimiter=",")
            for row in dict_reader:
                name = row["name"]
                price = Item.string_to_number(row["price"])
                quantity = Item.string_to_number(row["quantity"])
                Item.all.append(cls(name, price, quantity))

    @staticmethod
    def string_to_number(string: str) -> int:
        """
        Преобразование строки в число.
        """
        if string.isdigit():
            return int(string)
        return int(float(string))

    def __add__(self, other):
        """
        Сложение атрибутов классов.
        """
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        else:
            raise Exception

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{self.name, self.price, self.quantity}"
