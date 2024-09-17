from ..EnumItem import EnumItem;
from ..EnumBaby import EnumBaby;


class CostumeContextItem(EnumBaby):
    pass;


class EnumCostumeContext(EnumItem):
    __enumname__ = "costumeContext"
    __typeclass__ = CostumeContextItem

    __items__ = [
        "current"
    ]

    def __propitems__(self):
        return self.enum.scene.costumes.keys();
        

CostumeContext = EnumCostumeContext();