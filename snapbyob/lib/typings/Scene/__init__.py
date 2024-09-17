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


class Scene:
    def discretenew(self, t, *args, **kwargs):
        if type(t) == str:
            t = globals()[t];

        return t(self.project, self, *args, **kwargs);

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

        self.id = id(8, self.idcache);
        projName = options.get('name');

        if not projName:
            projName = self.id;

        self.stages = {};

        self.enum = self.discretenew(Enum);


        self.blocks = {
            "other": {}
        };


        self.costumes = {
            'turtle': self.discretenew(Costume)
        };


        self.sprites = {
            'sprite': self.discretenew(Sprite, self.costumes["turtle"])
        }


    def getStage(self, n):
        return self.stages[n];

    def getCostume(self, n):
        return self.costumes[n];

    def getBlock(self, n):
        return self.blocks[n];