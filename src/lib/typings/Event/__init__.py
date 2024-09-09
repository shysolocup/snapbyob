from ....lib.methods.id import id


class Event:
    def __init__(self, *args):

        name = None;
        parent = None;

        if len(args) >= 1:
            name = args[0];
        
        if len(args) >= 2:
            parent = args[1];

        self.id = id(8);
        self.listeners = [];
        self.parent = parent;
        self.name = name;
    
        if name and parent:
            if not parent.events:
                parent.events = { name: self };
        
            if not parent.events.get(name):
                parent.events[name] = self;

    def Listen(self, callback):
        self.listeners.append(callback);

    def Fire(self, *args):
        for l in self.listeners:
            l(args);

    def Destroy(self):
        print("destroyed but not done yet");