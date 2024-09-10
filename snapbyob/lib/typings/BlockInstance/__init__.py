from ..BlockHolder import BlockHolder;


class BlockInstance(BlockHolder):
    def __init__(self, proj, block, args, kwargs):
        self.project = proj;
        self.block = block;

        self.kwargs = kwargs;
        self.args = args;
        
        self.id = id(8);