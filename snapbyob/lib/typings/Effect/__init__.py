from ..EnumItem import EnumItem;
from ..EnumBaby import EnumBaby;


class EffectItem(EnumBaby):
    pass;


class EnumEffect(EnumItem):
    __enumname__ = "effect"
    __typeclass__ = EffectItem

    __items__ = [
        "color",
        "saturation",
        "brightness",
        "ghost",
        "fisheye",
        "whirl",
        "pixelate",
        "mosaic",
        "negative"
    ]
        

Effect = EnumEffect();