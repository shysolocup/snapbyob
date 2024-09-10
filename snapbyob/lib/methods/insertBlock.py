from ..typings.BlockInstance import BlockInstance;

async def insertBlock(self, ref, args):
        global block;
        block = self.project.blocks;
        reflist = [
            block
        ];

        if type(ref) == str:

            refs = ref.split(".");

            for r in refs:
                block = block[r];
                reflist.append(block);

        elif type(ref) == list:

            for r in refs:
                block = block[r];
                reflist.append(block);

        inst = await self.project.new(BlockInstance, block=block);
        inst.ref = reflist;
        inst.refstring = ref;

        return inst;