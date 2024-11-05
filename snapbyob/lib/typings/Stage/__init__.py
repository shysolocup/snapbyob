from ..Background import Background, BackgroundItem;
from ..LineType import LineTypeItem, LineType;
from ..Color3 import Color3;
from ..Costume import Costume;
from ..Sprite import Sprite;
from ..Space2 import Space2;

from ..XmlDict import XmlDict;

from ..BlockHolder import BlockHolder;
from ..SubclassHolder import SubclassHolder;

from ....lib.methods.id import id;
import asyncio


class Stage(BlockHolder, SubclassHolder):
    @property
    def parents(self):
        return [ self.project, self.scene ];


    def __init__(self, proj, scene, options=None):
        if not options:
            options = {};

        self.project = proj;
        self.scene = scene;

        self.id = id(8, self.project.idcache);

        # strings
        name: str = options.get('name') or self.id;
        

        # space
        size: Space2 = options.get("size") or Space2(480, 360);


        # ints & floats
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
        sublistIDs: bool = options.get('sublistIds') or False;


        # types
        color: Color3 = options.get('color') or Color3();
        background: BackgroundItem = options.get('background') or Background.blank;


        self.xmldata = self.scene.xmldata.setDeep('stage', XmlDict("stage", [
            [ '@name', name ],
            [ '@width', str(size.x) ],
            [ '@height', str(size.y) ],
            [ '@costume', "0" ],
            [ '@color', color.tostring() ],
            [ '@tempo', str(tempo) ],
            [ '@threadsafe', str(threadsafe).lower() ],
            [ '@penlog', str(penlog).lower() ],
            [ '@volume', str(volume) ],
            [ '@pan', str(pan) ],
            [ '@ternary', str(ternary).lower() ],
            [ '@hyperops', str(hyperops).lower() ],
            [ '@codify', str(codify).lower() ],
            [ '@inheritance', str(inheritance).lower() ],
            [ '@sublistIDs', str(sublistIDs).lower() ],

            [ 'pentrails', None ],
            
            [ 'costumes', XmlDict("costumes") ],
            [ 'sounds', XmlDict("sounds") ],
            [ 'variables', XmlDict("variables") ],
            [ 'blocks', XmlDict("blocks") ],
            [ 'scripts', XmlDict("scripts") ],
            [ 'sprites', XmlDict("sprites") ],
        ]));

        self.costumes = {
            'turtle': self.discretenew(Costume)
        };

        self.sprites = {
            'sprite': self.discretenew(Sprite, {
                "name": "sprite",
                "costume": self.getCostume("turtle")
            })
        }

        # print(self.scene.data);

        '''self.data = self.scene.newDataItem('project.scenes.scene', [
            
        ])'''

        # setattr(self.scene.stages, name, self);


    def getCostume(self, n):
        return self.costumes[n];

    def getSprite(self, n):
        return self.sprites[n];


    @property
    def name(self):
        return self.xmldata.getDeep('@name');

    @name.setter
    def name(self, v):
        oldname = self.xmldata.getDeep('@name');
        self.xmldata.setDeep('@name', str(v));
        # asyncio.run(self.project.events["stage"]["renamed"].Fire(self, oldname, v)); # Stage, oldName, newName


    @property
    def size(self):
        return Space2(self.xmldata.getDeep('@width'), self.xmldata.getDeep('@height'));


    @size.setter
    def size(self, v):
        old = self.size;

        self.xmldata.setDeep('@width', v.x);
        self.xmldata.setDeep('@height', v.y);

        new = self.size;

        # asyncio.run(self.project.events["stage"]["resized"].Fire(self, old, new)); # Stage, old, new



    @property
    def width(self):
        return self.xmldata.getDeep('@width');

    @width.setter
    def width(self, v):
        old = self.size;
        
        self.xmldata.setDeep('@width', str(v));
        
        new = self.size;

        # asyncio.run(self.project.events["stage"]["resized"].Fire(self, old, new)); # Stage, old, new


    
    @property
    def height(self):
        return self.xmldata.getDeep('@height');

    @height.setter
    def height(self, v):
        old = self.size;
        
        self.xmldata.setDeep('@height', str(v));
        
        new = self.size;

        # asyncio.run(self.project.events["stage"]["resized"].Fire(self, old, new)); # Stage, old, new
