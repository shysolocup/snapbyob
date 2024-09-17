from ..Event import Event

from ....lib.methods.id import id
from ....lib.methods.pingtime import pingtime

import asyncio;


class Project:

    @property
    def name(self):
        return self.data["project"]["@name"]

    @name.setter
    def name(self, v):
        asyncio.run(self.events["project"]["renamed"].Fire(self, self.data["project"]["@name"], v)); # Project, oldName, newName
        self.data["project"]["@name"] = v


    @property
    def version(self):
        return self.data["project"]["@version"]

    @version.setter
    def version(self, v):
        asyncio.run(self.events["project"]["reversioned"].Fire(self, self.data["project"]["@version"], v)); # Project, oldVer, newVer
        self.data["project"]["@version"] = v


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


        self.data = {
            "project": {

                "@app": "Snap! 10, https://snap.berkeley.edu",
                "@name": projName,
                "@version": projVer,
                "notes": None,

                "scenes": {
                    "@select": "1",
                }
            }
        };



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