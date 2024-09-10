from ..Event import Event
from ..Block import Block
from ..Scripts import Scripts;

from ....lib.methods.id import id
from ....lib.methods.pingtime import pingtime
from ....lib.methods.formFiles import formFiles;

import asyncio;
import time;
import os;

dirstring = os.path.realpath(__file__).replace("__init__.py", "");
splitpath = os.path.splitroot(dirstring);
drive, sep, path = splitpath;

separated = path.split(sep);
separated.pop(); separated.pop(); separated.pop(); separated.pop();

rawblocks = formFiles(drive, sep, separated, '....', [ 'lib', 'blocks' ]);
rawblockdata = {};

for n, d in rawblocks.items():
    impstring = 'from {d} import blockdata, callback'.format(d=d, n=n);
    formstring = 'rawblockdata[n] = { "blockdata": blockdata, "callback": callback }';
    exec(impstring);
    exec(formstring)


class Project:

    @property
    def name(self):
        return self.data["project"]["@name"]

    @name.setter
    def name(self, v):
        asyncio.run(self.events["projectNameChanged"].Fire(self, self.data["project"]["@name"], v)); # Project, oldName, newName
        self.data["project"]["@name"] = v


    async def ping(self):
        await self.events['ping'].Fire(self, pingtime()); # Project, pingtime


    def discretenew(self, t, *args, **kwargs):

        if type(t) == str:
            t = globals()[t];
        
        arglen = len(args);
        kwarglen = len(kwargs);

        if arglen > 0 and kwarglen > 0:
            return t(self, *args, **kwargs);
    
        elif arglen > 0 and kwarglen <= 0:
            return t(self, *args);
    
        elif arglen <= 0 and kwarglen > 0:
            return t(self, **kwargs);



    async def new(self, t, *args, **kwargs):
        if type(t) == str:
            t = globals()[t];

        arglen = len(args);
        kwarglen = len(kwargs);
        
        if arglen > 0 and kwarglen > 0:
            stuff = t(self, *args, **kwargs);
            await self.events['new'].Fire(self, stuff); # Project, Any
            return stuff
        
        elif arglen > 0 and kwarglen <= 0:
            stuff = t(self, *args);
            await self.events['new'].Fire(self, stuff); # Project, Any
            return stuff
        
        elif arglen <= 0 and kwarglen > 0:
            stuff = t(self, **kwargs);
            await self.events['new'].Fire(self, stuff); # Project, Any
            return stuff


    def __init__(self, *args):

        options = args[0];

        self.events = {};
        self.scripts = Scripts(self);


        self.blocks = {};


        def blockCat(makerArgs):
            category = makerArgs.get("category")

            if type(category) == str and not self.blocks.get("category"):
                self.blocks[category] = {};
                makerArgs["category"] = self.blocks[category];
        
            elif type(category) == str and self.blocks.get("category"):
                makerArgs["category"] = self.blocks[category];

        
        def blockName(makerArgs, callback):
            if not makerArgs.get("name"):
                makerArgs.__setitem__('name', callback.__name__);
            

        def BlockMaker(*args, **kwargs): return lambda callback: (
            blockCat(kwargs),
            blockName(kwargs, callback),
            kwargs.__setitem__("f", callback),
            self.discretenew(Block, kwargs=kwargs, args=args)
        );
    
        self.BlockMaker = BlockMaker;


        for k, data in rawblockdata.items():
            BlockMaker(name=data["blockdata"]["name"], category=data["blockdata"]["category"])(data["callback"]);


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

        def EventHandle(event):
            return lambda callback : self.events[event].Listen(callback);
        
        self.EventHandle = EventHandle;
        self.on = EventHandle;

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