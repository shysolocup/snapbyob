from ....lib.methods.id import id

from ..BlockHolder import BlockHolder


class Block(BlockHolder):

    def __init__(self, proj, args):
        self.project = proj;
        self.children = {};
        self.id = id(8);

        self.name = args.get("name");
        self.category = args.get("category");
        self.function = args.get("f");
        self.parent = args.get("p");

        self.id = id(8);
        
        if not self.name:
            self.name = self.id;
    
        if self.name and self.parent:
            if not self.parent.blocks:
                self.parent.blocks = { self.name: self };
            
            if not self.parent.events.get(self.category):
                self.parent.events[self.category] = {};
        
            if not self.parent.events.get(self.name):
                self.parent.events[self.name] = self;