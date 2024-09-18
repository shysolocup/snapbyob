from ....lib.methods.id import id

from ..BlockHolder import BlockHolder


class Block(BlockHolder):

    def __init__(self, proj, scene, args, kwargs):

        self.project = proj;
        self.scene = scene;
        self.id = id(8, proj.idcache);

        self.args = args;
        self.kwargs = kwargs;

        self.name = kwargs.get("name");
        self.category = kwargs.get("category");
        self.callback = kwargs.get("f");
        self.mods = kwargs.get('mods') or [];
        self.parent = kwargs.get("p");

        if type(self.category) == str:
            self.category = self.scene.blocks[self.category];

        self.category[self.name] = self;
        
        if not self.name:
            self.name = self.id;
    
        if self.name and self.parent:
            if not self.parent.blocks:
                self.parent.blocks = { self.name: self };
            
            if not self.parent.blocks.get(self.category):
                self.parent.blocks[self.category] = {};
        
            if not self.parent.blocks.get(self.name):
                self.parent.blocks[self.name] = self;