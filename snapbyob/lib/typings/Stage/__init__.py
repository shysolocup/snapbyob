from ..BlockHolder import BlockHolder;
from ..Background import Background, BackgroundItem;
from ..Color3 import Color3;

from ....lib.methods.id import id;


class Stage(BlockHolder):
    def __init__(self, proj, scene, options=None):
        if not options:
            options = {};

        self.project = proj;
        self.scene = scene;

        self.id = id(8, self.project.idcache);

        self.name = options.get('name') or self.id;
        self.width = options.get('width') or 480;
        self.height = options.get('height') or 360;
        self.costume = options.get('costume') or 0;
        self.color = options.get('color') or Color3();

        # setattr(self.scene.stages, name, self);

    background: BackgroundItem = Background.blank