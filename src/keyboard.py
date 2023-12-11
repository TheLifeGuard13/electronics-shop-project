from src.item import Item


class MixinFeature:
    """
    Подкласс миксин, который добавляет функционал смены языка RU/EN.
    """

    def __init__(self) -> None:
        self.__language = "EN"

    @property
    def language(self) -> str:
        return self.__language

    def change_lang(self) -> None:
        """
        Меняет язык RU-EN и наоборот
        """
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"


class Keyboard(MixinFeature, Item):
    """
    Подкласс клавиатура Класса для представления товара в магазине.
    """

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__()
        Item.__init__(self, name, price, quantity)
