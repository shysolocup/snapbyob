class BlockHolder:
    async def insert(self, ref, *args, **kwargs):
        from ....lib.methods.insertBlock import insertBlock
        block = await insertBlock(self, ref, args, kwargs);
        await self.project.events["blockPlaced"].Fire(self, block);
        return block

    children = {}