from ..BlockHolder import BlockHolder;


class BlockInstance(BlockHolder):
    def __init__(self, proj, block):
        self.project = proj;
        self.children = {};
        self.block = block;
        
        self.id = id(8);