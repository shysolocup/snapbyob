from ..EnumItem import EnumItem;
from ..EnumBaby import EnumBaby;

class Key(EnumBaby):
    pass


class EnumKeycode(EnumItem):
    __enumname__ = "keycode"
    __typeclass__ = Key

    __items__ = [
        "num0",
        "num1",
        "num2",
        "num3",
        "num4",
        "num5",
        "num6",
        "num7",
        "num8",
        "num9",
        "num0",
        "anyKey",
        "upArrow",
        "downArrow",
        "rightArrow",
        "leftArrow",
        "enter",
        "space",
        "plus",
        "minus",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z"
    ]

Keycode = EnumKeycode();