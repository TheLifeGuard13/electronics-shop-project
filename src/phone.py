from src.item import Item


class Phone(Item):
    """
    Подкласс телефон Класса для представления товара в магазине.
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self) -> int:
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value: int) -> None:
        if value <= 0:
            print("Количество физических SIM-карт должно быть целым числом больше нуля")
            raise ValueError
        self.__number_of_sim = value

    def __repr__(self) -> str:
        super().__repr__()
        return f"{self.__class__.__name__}{self.name, self.price, self.quantity, self.number_of_sim}"
