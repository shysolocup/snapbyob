from ..typings.BlockInstance import BlockInstance;

async def insertBlock(self, ref, args):
        global block
        block = self.project.blocks;
        reflist = [ block ];

        print(args);


        if type(ref) == str:
            refs = ref.split(".");
            for r in refs:
                try:
                    block = block[r];
                    reflist.append(block);
                except:
                    block = exec('block.{0}'.format(r));
                    reflist.append(block);
        

        elif type(ref) == list:
            refs = ref;
            for r in refs:
                try:
                    block = block[r];
                    reflist.append(block);
                except:
                    block = exec('block.{0}'.format(r));
                    reflist.append(block);
        
        block = reflist[-1];
        
        inst = await self.project.new(BlockInstance, block=block);
        inst.ref = reflist;
        inst.refstring = ref;

        return inst;