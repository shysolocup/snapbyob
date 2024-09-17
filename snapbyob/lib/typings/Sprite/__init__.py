from ..BlockHolder import BlockHolder;
from ..Costume import Costume;

class Sprite(BlockHolder):
    def __init__(self, proj, scene, costume=None):
        self.project = proj;
        self.scene = scene;
        self.costume = costume or scene.costumes.turtle;
    
    costume: Costume