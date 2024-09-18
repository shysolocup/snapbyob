from ..EnumItem import EnumItem;
from ..EnumBaby import EnumBaby;


class MyContextItem(EnumBaby):
    pass;


class EnumMyContext(EnumItem):
    __enumname__ = "myContext"
    __typeclass__ = MyContextItem

    __items__ = [
        "neighbors",
        "self",
        "otherSprites",
        "clones",
        "otherClones",
        "parts",
        "anchor",
        "stage",
        "children",
        "parent",
        "temporary",
        "name",
        "scripts",
        "solutions",
        "costumes",
        "sounds",
        "blocks",
        "categories",
        "dangling",
        "draggable",
        "width",
        "height",
        "left",
        "right",
        "top",
        "bottom",
        "rotationStyle",
        "rotationX",
        "rotationY",
        "centerX",
        "centerY"
    ]
        

MyContext = EnumMyContext();