class BlockHolder:
    async def insert(self, ref, **args):
        from ....lib.methods.insertBlock import insertBlock
        block = await insertBlock(self, ref, args);
        await self.project.events["blockPlaced"].Fire(self, block);
        return block