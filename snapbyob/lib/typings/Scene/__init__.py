from ..Block import Block
from ..Stage import Stage;
from ..Costume import Costume;
from ..Enum import Enum;
from ..Sprite import Sprite;

from ....lib.methods.id import id
from ....lib.methods.formFiles import formFiles;

import asyncio;
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


class Scene:
    def discretenew(self, t, *args, **kwargs):
        if type(t) == str:
            from ....__init__ import Typings;
            t = globals().get(t) or exec('Typings.{t}'.format(t));

        return t(self.project, self, *args, **kwargs);


    async def new(self, t, *args, **kwargs):
        if type(t) == str:
            from ....__init__ import Typings;
            t = globals().get(t) or Typings.get(t);

        stuff = t(self.project, self, *args, **kwargs);
        await self.project.events['new'].Fire(self.project, stuff); # Project, Any
        return stuff

    @property
    def name(self):
        return self.project.data["project"]["scenes"]["@name"]

    @name.setter
    def name(self, v):
        asyncio.run(self.project.events["scene"]["renamed"].Fire(self.project, self, self.project.data["project"]["@name"], v)); # Project, Scene, oldName, newName
        self.project.data["project"]["@name"] = v

    def __init__(self, proj, options=None):
        if not options:
            options = {};

        self.project = proj;

        self.id = id(8, self.project.idcache);
        name = options.get('name') or self.id;

        self.stages = {
            'stage': self.discretenew(Stage)
        };

        self.enum = self.discretenew(Enum);

        self.costumes = {
            'turtle': self.discretenew(Costume)
        };

        self.sprites = {
            'sprite': self.discretenew(Sprite, self.getCostume("turtle"))
        }

        self.blocks = {
            "other": {}
        };


        for k, data in rawblockdata.items():
            name = data["blockdata"].get("name");
            category = data["blockdata"].get("category");
            mods = data["blockdata"].get('mods');

            if not name or name == "__":
                name = k;

            if not category or category == "__":
                category = self.blocks["other"];

            self.BlockMaker(name=name, category=category, mods=mods)(data["callback"]);


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


    def getStage(self, n):
        return self.stages[n];

    def getCostume(self, n):
        return self.costumes[n];

    def getSprite(self, n):
        return self.sprites[n];

    def getBlock(self, n):
        return self.blocks[n];