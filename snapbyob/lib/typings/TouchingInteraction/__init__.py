from ..EnumItem import EnumItem;
from ..EnumBaby import EnumBaby;

class TouchingInteractionItem(EnumBaby):
    pass


class EnumTouchingInteraction(EnumItem):
    __enumname__ = "touchingInteraction"
    __typeclass__ = TouchingInteractionItem

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

TouchingInteraction = EnumTouchingInteraction();