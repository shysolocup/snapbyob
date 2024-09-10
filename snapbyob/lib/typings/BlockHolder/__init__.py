from ..Children import Children;


class BlockHolder:
    async def insert(self, ref, *args, **kwargs):
        from ....lib.methods.insertBlock import insertBlock
        block = await insertBlock(self, ref, args, kwargs);
        await self.project.events["blockPlaced"].Fire(self, block);
        return block

    @property
    def children(self):
        if not self.__dict__.get("__children__"):
            self.__children__ = self.project.discretenew(Children, self);

        return self.__children__;