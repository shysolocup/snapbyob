from ..EnumItem import EnumItem;
from ..EnumBaby import EnumBaby;


class ContextItem(EnumBaby):
    pass;


class EnumContext(EnumItem):
    __enumname__ = "context"
    __typeclass__ = ContextItem

    __items__ = [
        "all",
        "allScenes",
        "thisScript",
        "thisBlock",
        "allButThisScript",
        "otherScriptsInSprite"
    ]

Context = EnumContext();