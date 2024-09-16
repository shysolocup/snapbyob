from ..EnumItem import EnumItem;
from ..EnumBaby import EnumBaby;


class CloneContextItem(EnumBaby):
    pass;


class EnumCloneContext(EnumItem):
    __enumname__ = "cloneContext"
    __typeclass__ = CloneContextItem

    __items__ = [
        "myself"
    ]

    def __propitems__(self):
        return [ "Sprite" ];
        

CloneContext = EnumCloneContext();