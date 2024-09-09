class BlockInstance:

    def __init__(self, proj, block):
        self.project = proj;
        self.children = {};
        self.block = block;
        
        self.id = id(8);

    async def insert(*args):
        from ....lib.methods.insertBlock import insertBlock
        return await insertBlock(args);