from ..EnumItem import EnumItem;
from ..EnumBaby import EnumBaby;

class MouseInteractionItem(EnumBaby):
    pass


class EnumMouseInteraction(EnumItem):
    __enumname__ = "mouseInteraction"
    __typeclass__ = MouseInteractionItem

    __items__ = [
        "clicked",
        "pressed",
        "dropped",
        "mouseEntered",
        "mouseDeparted",
        "scrolledUp",
        "scrolledDown",
        "stopped"
    ]

MouseInteraction = EnumMouseInteraction();