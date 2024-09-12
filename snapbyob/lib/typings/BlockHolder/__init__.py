from ..Children import Children;


class BlockHolder:
    async def insert(self, ref, *args, **kwargs):
        from ....lib.methods.insertBlock import insertBlock
        block = await insertBlock(self, ref, args, kwargs);
        await self.project.events["block"]["placed"].Fire(self, block);
        return block
    
    async def insertGroup(self, *myargs):
        from ....lib.methods.insertBlock import insertBlock
        
        global table;
        table = myargs if len(myargs) > 1 else myargs[0];

        stuff = [];

        for i, block in enumerate(table):
            name = block.get("name");
            args = block.get("args");
            kwargs = block.get('kwargs');
            children = block.get("children");

            args = args if args else [];
            kwargs = kwargs if kwargs else {};

            if type(args) == dict:
                for k, v in args.items():
                    kwargs[k] = v;
    
            if type(kwargs) == list or type(args) == tuple:
                for i, v in enumerate(kwargs):
                    args.insert(i, v);

            if type(args) != list and type(args) != tuple:
                args = [args];

            inst = await insertBlock(self, name, args, kwargs);
            await self.project.events["block"]["placed"].Fire(self, inst);
            stuff.insert(i, inst);

            if children:
                await inst.insertGroup(children);
        
        return stuff;

    @property
    def children(self):
        if not self.__dict__.get("__children__"):
            self.__children__ = self.project.discretenew(Children, self);

        return self.__children__;