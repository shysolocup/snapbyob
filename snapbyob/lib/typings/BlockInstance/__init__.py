from ..BlockHolder import BlockHolder;


class BlockInstance(BlockHolder):
    def __init__(self, proj, block, args):
        self.project = proj;
        self.children = {};
        self.block = block;
        self.args = args;
        
        self.id = id(8);