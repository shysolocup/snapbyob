from ..Event import Event
from ..Block import Block
# from ..Scripts import Scripts;
from ..Stage import Stage;
from ..Costume import Costume;
from ..Enum import Enum;
from ..Sprite import Sprite;

from ....lib.methods.id import id
from ....lib.methods.pingtime import pingtime
from ....lib.methods.formFiles import formFiles;

import asyncio;
import time;
import copy;
import os;

dirstring = os.path.realpath(__file__).replace("__init__.py", "");
splitpath = os.path.splitroot(dirstring);
drive, sep, path = splitpath;

separated = path.split(sep);
separated.pop(); separated.pop(); separated.pop(); separated.pop();

ref = '.';
ext = [ 'lib', 'blocks' ];
d = copy.copy(separated);

for e in ext:
    d.append(e);

adir = '{drive}{sep}{path}'.format(drive=drive, sep=sep, path=sep.join(list(d)));

print(adir);


rawblocks = {};


def merge(x, y):
    z = copy.copy(x)   # start with keys and values of x
    z.update(y)    # modifies z with keys and values of y
    return z


for file in os.listdir(adir):
    if not file.startswith("__") and not file.endswith("__"):
        filename = os.fsdecode(file);

        ext2 = copy.copy(ext);
        ext2.insert(len(ext2), filename);

        stuff = formFiles(drive, sep, separated, ref, [ 'lib', 'blocks', filename ]);

        for k, v in stuff.items():
            rawblocks[k] = "..."+v;


rawblockdata = {};

for blockn, blockd in rawblocks.items():
    impstring = 'from {blockd} import blockdata, callback'.format(blockd=blockd);
    formstring = 'rawblockdata[blockn] = { "blockdata": blockdata, "callback": callback }';
    exec(impstring);
    exec(formstring)


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
            t = globals().get(t) or exec('Typings.{t}'.format(t));

        stuff = t(self, *args, **kwargs);
        await self.events['new'].Fire(self, stuff); # Project, Any
        return stuff
    


    def __init__(self, options=None):
        if not options:
            options = {};

        self.events = {};
        self.idcache = {};
        self.scenes = {};


        for k, data in rawblockdata.items():
            name = data["blockdata"].get("name");
            category = data["blockdata"].get("category");

            if not name or name == "__":
                name = k;

            if not category or category == "__":
                category = self.blocks["other"];

            self.BlockMaker(name=name, category=category)(data["callback"]);


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
        projName = options.get('name');

        if not projName:
            projName = self.id;
        
        projVer = options.get("version");

        if not projVer:
            projVer = 2;

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


    def blockCat(self, makerArgs):
            category = makerArgs.get("category")

            if type(category) == str and not self.blocks.get(category):
                self.blocks[category] = {};
                makerArgs["category"] = self.blocks[category];
        
            elif type(category) == str and self.blocks.get("category"):
                makerArgs["category"] = self.blocks[category];

        
    def blockName(self, makerArgs, callback):
        if not makerArgs.get("name"):
            makerArgs.__setitem__('name', callback.__name__);
        

    def BlockMaker(self, *args, **kwargs): return lambda callback: (
        self.blockCat(kwargs),
        self.blockName(kwargs, callback),
        kwargs.__setitem__("f", callback),
        self.discretenew(Block, args=args, kwargs=kwargs)
    );


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