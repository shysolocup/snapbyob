from ..BlockHolder import BlockHolder;
from ..Costume import Costume;

class Sprite(BlockHolder):
    def __init__(self, proj, scene, stage, costume=None):
        self.project = proj;
        self.scene = scene;
        self.stage = stage;
        self.costume = costume or scene.costumes.turtle;
    
    costume: Costume