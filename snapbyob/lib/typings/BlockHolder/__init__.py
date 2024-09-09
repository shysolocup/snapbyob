from ....lib.methods.insertBlock import insertBlock

class BlockHolder:
    async def insert(self, *args):
        await self.project.events["blockPlaced"].Fire();

        return await insertBlock(self, args);