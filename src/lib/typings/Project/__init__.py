from ..Event import Event
from ..Scripts import Scripts;
from ....lib.methods.id import id


class Project:

    def ping(self):
        self.events['ping'].Fire(self);

    def __init__(self, *args):

        options = args[0];

        self.events = {}
        
        self.scripts = Scripts(self);

        self.events = {
            'ping': Event(),
            
            # events
            'eventCreated': Event(),
            'eventDestroyed': Event(),
            'eventUpdated': Event(),

            # blocks
            'blockPlaced': Event(),
            'blockCreated': Event(),
            'blockDestroyed': Event(),
            'blockUpdated': Event()
        }

        class EventHandle:
            def __init__(onSelf, event):
                onSelf.event = event;
                
            def __call__(onSelf, callback):
                self.events[onSelf.event].append(callback);

        self.on = EventHandle;

        if not options:
            options = {};

        projId = id(8);
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

        ## properties
        @property
        def name(self):
            return self.Data["@name"]

        @name.setter
        def name(self, v):
            self.Data["@name"] = v



        '''with open(projName+".xml", "w") as file:
            file.write("");
            self.file = file;'''