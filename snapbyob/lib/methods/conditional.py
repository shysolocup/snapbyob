from ..typings.Children import Children;


async def conditional(self):
    self.conditions = self.scene.discretenew(Children, self);

    if getattr(self, "data") and self.data.get("conditions"):
        from ..typings.BlockInstance import BlockInstance;

        cond = self.data.get('conditions');

        for i, bl in enumerate(cond):
            name = bl.get("name");
            args = bl.get("args");
            kwargs = bl.get('kwargs');
            children = bl.get("children");

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

            kwargs["__data__"] = bl;

            global block
            block = self.scene.blocks;
            reflist = [ block ];

            if type(name) == str:
                refs = name.split(".");
                for r in refs:
                    try:
                        block = block[r];
                        reflist.append(block);
                    except:
                        block = getattr(block, r);
                        reflist.append(block);
        

            elif type(name) == list:
                refs = name;
                for r in refs:
                    try:
                        block = block[r];
                        reflist.append(block);
                    except:
                        block = getattr(block, r);
                        reflist.append(block);

            inst = await self.scene.new(BlockInstance, block=block, args=args, kwargs=kwargs);
            inst.ref = reflist;
            inst.refstring = name;
            
            self.conditions.new(inst);

            await self.project.events["block"]["placed"].Fire(self, inst);
        
            if children:
                await inst.placeGroup(children);