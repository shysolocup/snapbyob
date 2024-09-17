from ..EnumItem import EnumItem;
from ..EnumBaby import EnumBaby;


class ThisContextItem(EnumBaby):
    pass;


class EnumThisContext(EnumItem):
    __enumname__ = "thisContext"
    __typeclass__ = ThisContextItem

    __items__ = [
        "script",
        "caller",
        "continuation",
        "inputs"
    ]

    '''def __propitems__(self):
        return self.enum.project.scenes.keys();'''
        

ThisContext = EnumThisContext();