class EnumKeycode:
    pass

Keycode = EnumKeycode();

class Key:
    def __init__(self, value, id):
        self.id = id;
        self.value = value;

keys = [
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
];

for i, k in enumerate(keys):
    key = Key(k, i);

    exec("Keycode.{0} = key".format(k));