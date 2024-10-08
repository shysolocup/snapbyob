from ..Children import Children;


class BlockHolder:
    async def place(self, ref, *args, **kwargs):
        from ....lib.methods.insertBlock import insertBlock
        block = await insertBlock(self, ref, args, kwargs);
        return block
    

    async def placeGroup(self, *myargs):
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

            if type(args) == tuple:
                args = list(args);

            if type(args) == dict:
                for k, v in args.items():
                    kwargs[k] = v;
                    args = tuple([]);
    
            if type(kwargs) == list or type(kwargs) == tuple:
                for i, v in enumerate(kwargs):
                    args.insert(i, v);
                    kwargs = {};

            if type(args) != list and type(args) != tuple:
                args = tuple([args]);
            
            if type(args) == list:
                args = tuple(args);

            kwargs["__data__"] = block;

            inst = await insertBlock(self, name, args, kwargs);
            
            stuff.insert(i, inst);

            if children:
                await inst.placeGroup(children);
        
        return stuff;

    @property
    def children(self):
        if not self.__dict__.get("__children__"):
            self.__children__ = self.scene.discretenew(Children, self);

        return self.__children__;