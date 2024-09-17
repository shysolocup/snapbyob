from ..EnumItem import EnumItem;
from ..EnumBaby import EnumBaby;


class SceneContextItem(EnumBaby):
    pass;


class EnumSceneContext(EnumItem):
    __enumname__ = "sceneContext"
    __typeclass__ = SceneContextItem

    __items__ = [
        "next",
        "previous",
        "random"
    ]

    def __propitems__(self):
        return self.enum.project.scenes.keys();
        

SceneContext = EnumSceneContext();