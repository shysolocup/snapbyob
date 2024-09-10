from ....lib.methods.id import id

from ..BlockHolder import BlockHolder


class Block(BlockHolder):

    def __init__(self, proj, kwargs):

        self.project = proj;
        self.children = {};
        self.id = id(8);

        self.name = kwargs.get("name");
        self.category = kwargs.get("category");
        self.callback = kwargs.get("f");
        self.parent = kwargs.get("p");

        self.id = id(8);

        self.category[self.name] = self;
        
        if not self.name:
            self.name = self.id;
    
        if self.name and self.parent:
            if not self.parent.blocks:
                self.parent.blocks = { self.name: self };
            
            if not self.parent.events.get(self.category):
                self.parent.events[self.category] = {};
        
            if not self.parent.events.get(self.name):
                self.parent.events[self.name] = self;