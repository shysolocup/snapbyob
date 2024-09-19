class SubclassHolder:
    parents = [];

    def get(self, ref):
        global thing
        thing = self;
        reflist = [ thing ];

        if type(ref) == str:
            refs = ref.split(".");
            for r in refs:
                try:
                    thing = thing[r];
                    reflist.append(thing);
                except:
                    thing = getattr(thing, r);
                    reflist.append(thing);
        

        elif type(ref) == list:
            refs = ref;
            for r in refs:
                try:
                    thing = thing[r];
                    reflist.append(thing);
                except:
                    thing = getattr(thing, r);
                    reflist.append(thing);
        
        thing = reflist[-1];
    
        return thing;

    def discretenew(self, t, *args, **kwargs):
        if type(t) == str:
            from ....__init__ import Typings;
            t = globals().get(t) or exec('Typings.{t}'.format(t));

        return t(*self.parents, self, *args, **kwargs);


    async def new(self, t, *args, **kwargs):
        if type(t) == str:
            from ....__init__ import Typings;
            t = globals().get(t) or Typings.get(t);

        stuff = t(*self.parents, self, *args, **kwargs);

        if self.project == self:
            await self.events['new'].Fire(self, stuff); # Project, Any
        else:
            await self.project.events['new'].Fire(self.project, self, stuff); # Project, SubclassHolder, Any
        
        return stuff