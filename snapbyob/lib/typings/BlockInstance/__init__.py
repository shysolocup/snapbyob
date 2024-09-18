from ..BlockHolder import BlockHolder;
from ..Children import Children;

from ....lib.methods.id import id;


class BlockInstance(BlockHolder):
    def __init__(self, proj, scene, block, args, kwargs):
        self.project = proj;
        self.scene = scene;
        self.block = block;
        self.data = kwargs.get("__data__");

        if self.data:
            del kwargs["__data__"];

        extendees = [
            "name",
            "category",
            "callback",
            "parent"
        ];

        self.kwargs = kwargs or {};
        self.args = args or tuple([]);
        
        self.id = id(8, proj.idcache);
        self.blockId = self.block.id

        for e in extendees:
            exec('self.{0} = self.block.{0}'.format(e));