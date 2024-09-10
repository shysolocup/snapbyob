from ..BlockHolder import BlockHolder;


class BlockInstance(BlockHolder):
    def __init__(self, proj, block, kwargs):
        self.project = proj;
        self.children = {};
        self.block = block;
        self.args = kwargs;
        
        self.id = id(8);