from ..EnumItem import EnumItem;
from ..EnumBaby import EnumBaby;


class BackgroundItem(EnumBaby):
    pass;


class EnumBackground(EnumItem):
    __enumname__ = "background"
    __typeclass__ = BackgroundItem

    __items__ = [
        "blank"
    ]
        

Background = EnumBackground();