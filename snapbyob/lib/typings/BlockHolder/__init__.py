class BlockHolder:
    async def insert(self, ref, **kwargs):
        from ....lib.methods.insertBlock import insertBlock
        block = await insertBlock(self, ref, kwargs);
        await self.project.events["blockPlaced"].Fire(self, block);
        return block