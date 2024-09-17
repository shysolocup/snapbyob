from ..BlockHolder import BlockHolder;
from ....lib.methods.id import id;

class BlockInstance(BlockHolder):
    def __init__(self, proj, scene, block, args, kwargs):
        self.project = proj;
        self.scene = scene;
        self.block = block;

        extendees = [
            "name",
            "category",
            "callback",
            "parent"
        ];

        for e in extendees:
            exec('self.{0} = self.block.{0}'.format(e));

        self.kwargs = kwargs;
        self.args = args;
        
        self.id = id(8, proj.idcache);
        self.blockId = self.block.id