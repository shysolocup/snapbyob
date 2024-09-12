from ..Event import Event
from ..Block import Block
from ..Scripts import Scripts;

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
        asyncio.run(self.events["project"]["nameChanged"].Fire(self, self.data["project"]["@name"], v)); # Project, oldName, newName
        self.data["project"]["@name"] = v


    async def ping(self, *args, **kwargs):
        await self.events['ping'].Fire(self, pingtime(), *args, **kwargs); # Project, pingtime, ...


    def discretenew(self, t, *args, **kwargs):

        if type(t) == str:
            t = globals()[t];
        
        arglen = len(args);
        kwarglen = len(kwargs);

        return t(self, *args, **kwargs);



    async def new(self, t, *args, **kwargs):
        if type(t) == str:
            t = globals()[t];

        arglen = len(args);
        kwarglen = len(kwargs);

        stuff = t(self, *args, **kwargs);
        await self.events['new'].Fire(self, stuff); # Project, Any
        return stuff


    def __init__(self, *args):

        options = args[0];

        self.events = {};
        self.scripts = Scripts(self);

        self.idcache = {};

        self.blocks = {};


        def blockCat(makerArgs):
            category = makerArgs.get("category")

            if type(category) == str and not self.blocks.get(category):
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
            self.discretenew(Block, args=args, kwargs=kwargs)
        );
    
        self.BlockMaker = BlockMaker;


        for k, data in rawblockdata.items():
            BlockMaker(name=data["blockdata"]["name"], category=data["blockdata"]["category"])(data["callback"]);


        self.events = {
            # misc
            'ping': self.discretenew(Event, category=""),
            'new': self.discretenew(Event, category=""),

            # project
            'project': {
                'renamed': self.discretenew(Event, category="project"),
                'updated': self.discretenew(Event, category="project")
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


        def actuallyDoEventStuff(ref, callback):
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

        def EventHandle(event):
            return lambda callback : actuallyDoEventStuff(event, callback)
        
        self.EventHandle = EventHandle;
        self.on = EventHandle;

        if not options:
            options = {};

        projId = id(8, self.idcache);
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