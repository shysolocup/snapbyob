from ..EnumItem import EnumItem;
from ..EnumBaby import EnumBaby;


class LayerItem(EnumBaby):
    pass;


class EnumLayer(EnumItem):
    __enumname__ = "layer"
    __typeclass__ = LayerItem

    __items__ = [
        "front",
        "back"
    ]
        

Layer = EnumLayer();