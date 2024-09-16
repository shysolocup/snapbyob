from ..EnumItem import EnumItem;
from ..EnumBaby import EnumBaby;


class RelContextItem(EnumBaby):
    pass;


class EnumRelContext(EnumItem):
    __enumname__ = "relContext"
    __typeclass__ = RelContextItem

    __items__ = [
        "all",
        "allScenes",
        "thisScript",
        "thisBlock",
        "allButThisScript",
        "otherScriptsInSprite"
    ]

RelContext = EnumRelContext();