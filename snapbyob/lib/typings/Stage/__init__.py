from ..Background import Background, BackgroundItem;
from ..LineType import LineTypeItem, LineType;
from ..Color3 import Color3;
from ..Costume import Costume;
from ..Sprite import Sprite;

from ..DataHolder import DataHolder;
from ..BlockHolder import BlockHolder;
from ..SubclassHolder import SubclassHolder;

from ....lib.methods.id import id;
import asyncio


class Stage(BlockHolder, DataHolder, SubclassHolder):
    @property
    def parents(self):
        return [ self.project, self.scene ];


    @property
    def name(self):
        return self.project.data["project"]["scenes"]["@name"]

    @name.setter
    def name(self, v):
        asyncio.run(self.project.events["scene"]["renamed"].Fire(self.project, self, self.project.data["project"]["@name"], v)); # Project, Scene, oldName, newName
        self.project.data["project"]["@name"] = v

    def __init__(self, proj, scene, options=None):
        if not options:
            options = {};

        self.project = proj;
        self.scene = scene;

        self.id = id(8, self.project.idcache);

        # strings
        name: str = options.get('name') or self.id;
        
        # ints & floats
        width: int | float = options.get('width') or 480;
        height: int | float = options.get('height') or 360;
        tempo: int | float = options.get('tempo') or 60;
        volume: int | float = options.get('volume') or 100;
        pan: int | float = options.get('pan') or 0;
        lines: LineTypeItem = options.get('lines') or LineType.round;


        # booleans
        hyperops: bool = options.get('hyperops') or True;
        inheritance: bool = options.get('inheritance') or True;

        threadsafe: bool = options.get('threadsafe') or False;
        penlog: bool = options.get('penlog') or False;
        ternary: bool = options.get('ternary') or False;
        codify: bool = options.get('codify') or False;
        sublistIds: bool = options.get('sublistIds') or False;


        # types
        color: Color3 = options.get('color') or Color3();
        background: BackgroundItem = options.get('background') or Background.blank;

        self.costumes = {
            'turtle': self.discretenew(Costume)
        };

        self.sprites = {
            'sprite': self.discretenew(Sprite, self.getCostume("turtle"))
        }

        # print(self.scene.data);

        '''self.data = self.scene.newDataItem('project.scenes.scene', [
            
        ])'''

        # setattr(self.scene.stages, name, self);


    def getCostume(self, n):
        return self.costumes[n];

    def getSprite(self, n):
        return self.sprites[n];