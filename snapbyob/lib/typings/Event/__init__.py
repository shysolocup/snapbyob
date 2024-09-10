from ....lib.methods.id import id


class Event:
    def __init__(self, proj, **kwargs):

        self.name = kwargs.get('name');
        self.parent = kwargs.get('parent');

        self.id = id(8);
        self.listeners = [];
        self.project = proj;

        if not self.name:
            self.name = self.id;
    
        if self.name and self.parent:
            if not self.parent.events:
                self.parent.events = { self.name: self };
        
            if not self.parent.events.get(self.name):
                self.parent.events[self.name] = self;


    def Listen(self, callback):
        # print('listening');
        self.listeners.append(callback);


    async def Fire(self, *args):
        # print('firing');
        for l in self.listeners:
            await l(*args);
    

    def FireSync(self, *args):
        for l in self.listeners:
            l(*args);


    def Destroy(self):
        print("destroyed but not done yet");