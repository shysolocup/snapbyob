from ..Event import Event
from ..SubclassHolder import SubclassHolder;
from ..XmlDict import XmlDict;

from ....lib.methods.id import id
from ....lib.methods.pingtime import pingtime

import asyncio;


class Project(SubclassHolder):

    @property
    def name(self):
        return self.xmldata.getDeep('project.@name');

    @name.setter
    def name(self, v):
        oldname = self.xmldata.getDeep('project.@name');
        self.xmldata.setDeep('project.@name', str(v));
        # asyncio.run(self.events["project"]["renamed"].Fire(self, oldname, v)); # Project, oldName, newName


    @property
    def version(self):
        return self.xmldata.getDeep('project.@version');

    @version.setter
    def version(self, v):
        oldver = self.xmldata.getDeep('project.@version');
        self.xmldata.setDeep('project.@version', str(v));
        asyncio.run(self.events["project"]["reversioned"].Fire(self, oldver, v)); # Project, oldVer, newVer


    async def ping(self, *args, **kwargs):
        await self.events['ping'].Fire(self, pingtime(), *args, **kwargs); # Project, pingtime, ...

    
    async def compileToFile(self, filename, *args, **kwargs):
        print(filename);

        '''with open(filename, 'w') as file:
            print(filename);'''


    def __init__(self, options=None):
        if not options:
            options = {};

        self.project = self;

        self.events = {};
        self.idcache = {};
        self.scenes = {};


        self.events = {
            # misc
            'ping': self.discretenew(Event, category=""),
            'new': self.discretenew(Event, category=""),

            # project
            'project': {
                'renamed': self.discretenew(Event, category="project"),
                'reversioned': self.discretenew(Event, category="project"),
                'updated': self.discretenew(Event, category="project"),
            },


            # scenes
            'scene': {
                'renamed': self.discretenew(Event, category="scene"),
                'created': self.discretenew(Event, category="scene"),
                'destroyed': self.discretenew(Event, category="scene"),
                'updated': self.discretenew(Event, category="scene")
            },


            # stages
            'stage': {
                'renamed': self.discretenew(Event, category="stage"),
                'created': self.discretenew(Event, category="stage"),
                'destroyed': self.discretenew(Event, category="stage"),
                'updated': self.discretenew(Event, category="stage"),
                'resized': self.discretenew(Event, category="stage")
            },

            
            # events
            'event': {
                'created': self.discretenew(Event, category="event"),
                'destroyed': self.discretenew(Event, category="event"),
                'updated': self.discretenew(Event, category="event"),
            },

            # blocks
            'block': {
                'placed': self.discretenew(Event, category="block"),
                'created': self.discretenew(Event, category="block"),
                'destroyed': self.discretenew(Event, category="block"),
                'updated': self.discretenew(Event, category="block"),
            },
        }

        def EventHandle(event):
            return lambda callback : self.actuallyDoEventStuff(event, callback)
        
        self.EventHandle = EventHandle;
        self.on = EventHandle;


        if not options:
            options = {};


        self.id = id(8, self.idcache);
        projName = options.get('name') or self.id;
        projVer = options.get("version") or 2;

        self.xmldata = XmlDict("__file__", [
            [ 'project', XmlDict("project", [
                [ '@app',  "Snap! 10, https://snap.berkeley.edu" ],
                [ '@name', projName ],
                [ '@version', str(projVer) ],
                [ 'notes', XmlDict("notes") ],
                [ 'scenes', XmlDict("scenes", [
                    [ '@select', str(1) ]
                ])] 
            ])]
        ]);



        '''with open(projName+".xml", "w") as file:
            file.write("");
            self.file = file;'''


    def actuallyDoEventStuff(self, ref, callback):
        global event
        event = self.events;
        reflist = [ event ];

        if type(ref) == str:
            refs = ref.split(".");
            for r in refs:
                # print(event, r);
                try:
                    event = event[r];
                    reflist.append(event);
                except:
                    event = exec('event.{0}'.format(r));
                    reflist.append(event);
        

        elif type(ref) == list:
            refs = ref;
            for r in refs:
                try:
                    event = event[r];
                    reflist.append(event);
                except:
                    e = exec('event.{0}'.format(r));
                    reflist.append(event);
        
        event = reflist[-1];
        event.Listen(callback);