from ..EnumItem import EnumItem;
from ..EnumBaby import EnumBaby;


class LineTypeItem(EnumBaby):
    pass;


class EnumLineType(EnumItem):
    __enumname__ = "lineType"
    __typeclass__ = LineTypeItem

    __items__ = [
        "round",
    ]
        

LineType = EnumLineType();