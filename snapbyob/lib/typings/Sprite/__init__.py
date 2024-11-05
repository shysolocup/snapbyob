from ..BlockHolder import BlockHolder;
from ..SubclassHolder import SubclassHolder;

from ..Costume import Costume;

from ..XmlDict import XmlDict;
from ..Space2 import Space2;
from ..Color3 import Color3;

from ....lib.methods.id import id;


class Sprite(BlockHolder, SubclassHolder):
    def __init__(self, proj, scene, stage, options=None):
        if not options:
            options = {};

        self.project = proj;
        self.scene = scene;
        self.stage = stage;5
        self.id = id(8, self.project.idcache);


        self.costumes = {};
        self.sounds = {};
        self.blocks = {};
        self.variables = {};
        self.scripts = {};


        # strings
        name: str = options.get('name') or self.id;
        
        # ints & floats
        heading: int | float = options.get('heading') or 90;
        scale: int | float = options.get('scale') or 1;
        volume: int | float = options.get('volume') or 100;
        pan: int | float = options.get('pan') or 0;

        # booleans
        draggable: bool = options.get('draggable') or True;
        pan: int | float = options.get('pan') or 0;

        # others
        position: Space2 = options.get('position') or Space2(480, 360);
        costume: Costume = options.get('Costume') or self.stage.getCostume("turtle");
        color: Color3 = options.get('color') or Color3();



        self.xmldata = self.stage.xmldata.setDeep('stage', XmlDict("sprite", [
            [ '@name', name ],
            [ '@x', str(position.x) ],
            [ '@y', str(position.y) ],
            [ '@costume', costume ],
            [ '@color', color.tostring() ],
            [ '@volume', str(volume) ],
            [ '@pan', str(pan) ],
            
            [ 'costumes', XmlDict("costumes") ],
            [ 'sounds', XmlDict("sounds") ],
            [ 'variables', XmlDict("variables") ],
            [ 'blocks', XmlDict("blocks") ],
            [ 'scripts', XmlDict("scripts") ],
        ]));
    
    costume: Costume