import pytest

from src.keyboard import Keyboard


def test_keybord():
    kb_1 = Keyboard("Asus df400", 1500, 5)
    assert str(kb_1) == "Asus df400"
    assert str(kb_1.language) == "EN"
    kb_1.change_lang()
    assert str(kb_1.language) == "RU"
    kb_1.change_lang()
    assert str(kb_1.language) == "EN"
    with pytest.raises(AttributeError):
        kb_1.language = "CH"
