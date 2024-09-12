from ..EnumItem import EnumItem;
from ..EnumBaby import EnumBaby;

class MessageItem(EnumBaby):
    pass;


class EnumMessage(EnumItem):
    __enumname__ = "message"
    __typeclass__ = MessageItem

    __items__ = [
        "flag"
    ]

Message = EnumMessage();