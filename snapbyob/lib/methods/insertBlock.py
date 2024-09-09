from ..typings.BlockInstance import BlockInstance;

async def insertBlock(self, args):
        ref = args[0];

        global block;
        block = self.project.blocks;

        if type(ref) == str:

            refs = ref.split(".");
            for r in refs:
                block = block[r];

        elif type(ref) == list:

            for r in refs:
                block = block[r];

        inst = await self.project.new(BlockInstance, block=block)

        return inst;