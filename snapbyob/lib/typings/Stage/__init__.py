from ..BlockHolder import BlockHolder;
from ..Background import Background, BackgroundItem;


class Stage(BlockHolder):
    def __init__(self, proj, scene):
        self.project = proj;
        self.scene = scene;

    background: BackgroundItem = Background.blank