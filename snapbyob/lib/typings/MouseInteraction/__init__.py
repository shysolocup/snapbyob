from ..EnumItem import EnumItem;


class MouseInteractionItem:
    def __init__(self, value, id):
        self.id = id;
        self.value = value;


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