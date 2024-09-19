from ..Event import Event

from ....lib.methods.id import id
from ....lib.methods.pingtime import pingtime

import asyncio;


class Project:

    @property
    def name(self):
        return self.getDataItem('project.@name');

    @name.setter
    def name(self, v):
        oldname = self.getDataItem('project.@name');
        self.setDataItem('project.@name', v);
        asyncio.run(self.events["project"]["renamed"].Fire(self, oldname, v)); # Project, oldName, newName


    @property
    def version(self):
        return self.getDataItem('project.@version')

    @version.setter
    def version(self, v):
        oldver = self.getDataItem('project.@version');
        self.setDataItem('project.@version', v);
        asyncio.run(self.events["project"]["reversioned"].Fire(self, oldver, v)); # Project, oldVer, newVer


    async def ping(self, *args, **kwargs):
        await self.events['ping'].Fire(self, pingtime(), *args, **kwargs); # Project, pingtime, ...


    def discretenew(self, t, *args, **kwargs):
        if type(t) == str:
            from ....__init__ import Typings;
            t = globals().get(t) or exec('Typings.{t}'.format(t));

        return t(self, *args, **kwargs);


    async def new(self, t, *args, **kwargs):
        if type(t) == str:
            from ....__init__ import Typings;
            t = globals().get(t) or Typings.get(t);

        stuff = t(self, *args, **kwargs);
        await self.events['new'].Fire(self, stuff); # Project, Any
        return stuff
    

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


    def setDataItem(self, ref, value):
        reflist = [ self.data ];

        def doit(refs):
            global thing;
            thing = self.data;

            for i, r in enumerate(refs):
                for i2, d in enumerate(thing):

                    if d[0] == r:
                        thing = d[1];

                        if i == len(refs)-1:
                            d[1] = value;

                        reflist.append(thing);
                    
                    elif d[0] != r and i2 == len(thing)-1:
                        thing.append([ r, value ]);
        
                    else:
                        for d2 in d[1]:
                            if d2[0] == "name" and d2[1] == r:
                                thing = d[1];
                                reflist.append(thing);

        if type(ref) == str:
            refs = ref.split(".");
            doit(refs);
        
        elif type(ref) == list:
            doit(ref);
        

        thing = reflist[-1];
    
        return thing;


    def newDataItem(self, ref, value):
        reflist = [ self.data ];

        def doit(refs):
            global thing;
            thing = self.data;

            for i, r in enumerate(refs):
                for i2, d in enumerate(thing):
                    if len(thing)-1:
                        thing.append([ r, value ]);

        if type(ref) == str:
            refs = ref.split(".");
            doit(refs);
        
        elif type(ref) == list:
            doit(ref);
        

        thing = reflist[-1];
    
        return thing;


    def getDataItem(self, ref):
        reflist = [ self.data ];

        def doit(refs):
            global thing;
            thing = self.data;

            for r in refs:
                if type(thing) == list:
                    for d in thing:
                        if d[0] == r:
                            thing = d[1];
                            reflist.append(thing);
                        else:
                            for d2 in d[1]:
                                if d2[0] == "name" and d2[1] == r:
                                    thing = d[1];
                                    reflist.append(thing);
                elif type(thing) == dict:
                    for k, v in thing.items():
                        if k == r:
                            thing = v;
                            reflist.append(thing);

        if type(ref) == str:
            refs = ref.split(".");
            doit(refs);
        
        elif type(ref) == list:
            doit(ref);
        
        thing = reflist[-1];
    
        return thing;

    
    async def compileToFile(self, filename, *args, **kwargs):
        print(filename);

        '''with open(filename, 'w') as file:
            print(filename);'''


    def __init__(self, options=None):
        if not options:
            options = {};

        self.events = {};
        self.idcache = {};
        self.scenes = {};


        self.events = {
            # misc
            'ping': self.discretenew(Event, category=""),
            'new': self.discretenew(Event, category=""),

            # project
            'project': {
                'renamed': self.discretenew(Event, category="project"),
                'reversioned': self.discretenew(Event, category="project"),
                'updated': self.discretenew(Event, category="project"),
            },


            # scenes
            'scene': {
                'renamed': self.discretenew(Event, category="scene"),
                'created': self.discretenew(Event, category="scene"),
                'destroyed': self.discretenew(Event, category="scene"),
                'updated': self.discretenew(Event, category="scene")
            },

            
            # events
            'event': {
                'created': self.discretenew(Event, category="event"),
                'destroyed': self.discretenew(Event, category="event"),
                'updated': self.discretenew(Event, category="event"),
            },

            # blocks
            'block': {
                'placed': self.discretenew(Event, category="block"),
                'created': self.discretenew(Event, category="block"),
                'destroyed': self.discretenew(Event, category="block"),
                'updated': self.discretenew(Event, category="block"),
            },
        }

        def EventHandle(event):
            return lambda callback : self.actuallyDoEventStuff(event, callback)
        
        self.EventHandle = EventHandle;
        self.on = EventHandle;


        if not options:
            options = {};


        self.id = id(8, self.idcache);
        projName = options.get('name') or self.id;
        projVer = options.get("version") or 2;

        self.data = [
            [ 'project', [
                [ '@app',  "Snap! 10, https://snap.berkeley.edu" ],
                [ '@name', projName ],
                [ '@version', projVer ],
                [ 'notes', None ],
                [ 'scenes', [
                    [ '@select', 1 ]
                ]] 
            ]]
        ];



        '''with open(projName+".xml", "w") as file:
            file.write("");
            self.file = file;'''


    def actuallyDoEventStuff(self, ref, callback):
        global event
        event = self.events;
        reflist = [ event ];

        if type(ref) == str:
            refs = ref.split(".");
            for r in refs:
                # print(event, r);
                try:
                    event = event[r];
                    reflist.append(event);
                except:
                    event = exec('event.{0}'.format(r));
                    reflist.append(event);
        

        elif type(ref) == list:
            refs = ref;
            for r in refs:
                try:
                    event = event[r];
                    reflist.append(event);
                except:
                    e = exec('event.{0}'.format(r));
                    reflist.append(event);
        
        event = reflist[-1];
        event.Listen(callback);