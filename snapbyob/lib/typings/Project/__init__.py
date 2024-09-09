from ..Event import Event
from ..Block import Block
from ..Scripts import Scripts;
from ....lib.methods.id import id
import asyncio;


class Project:

    @property
    def name(self):
        return self.data["project"]["@name"]

    @name.setter
    def name(self, v):
        asyncio.run(self.events["projectNameChanged"].Fire());
        self.data["project"]["@name"] = v

    def ping(self):
        self.events['ping'].Fire(self);


    def discretenew(self, t, **args):
        if type(t) == str:
            t = globals()[t];
        
        return t(self, args);


    async def new(self, t, **args):

        if type(t) == str:
            t = globals()[t];
        
        stuff = t(self, args);
        await self.events['new'].Fire(self, stuff);
        return stuff


    def __init__(self, *args):

        options = args[0];

        self.events = {};
        self.blocks = {};

        self.scripts = Scripts(self);

        self.blocks = {
            'motion': {
                'move': self.discretenew(Block, f=lambda x, y : (
                    print(x),
                    print(y)
                ))
            }
        };

        self.events = {
            # misc
            'ping': self.discretenew(Event),
            'new': self.discretenew(Event),

            # project
            'projectNameChanged': self.discretenew(Event),
            'projectUpdated': self.discretenew(Event),
            
            # events
            'eventCreated': self.discretenew(Event),
            'eventDestroyed': self.discretenew(Event),
            'eventUpdated': self.discretenew(Event),

            # blocks
            'blockPlaced': self.discretenew(Event),
            'blockCreated': self.discretenew(Event),
            'blockDestroyed': self.discretenew(Event),
            'blockUpdated': self.discretenew(Event)
        }

        class EventHandler:
            def __init__(onSelf, event):
                onSelf.event = event;
                
            def __call__(onSelf, callback):
                self.events[onSelf.event].append(callback);
        
        self.EventHandler = EventHandler
        self.on = EventHandler;

        if not options:
            options = {};

        projId = id(8);
        projName = options.get('name');

        if not projName:
            projName = projId;
        
        projVer = options.get("version");

        if not projVer:
            self.projVer = 2;

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