import random;
import json;
import requests;
import asyncio;


import xml.etree.ElementTree as ET;
import xmltodict as xml;


# print(requests.get('https://snap.berkeley.edu/api/v1/projects/adfs/test'));


from .lib import *

print(stuff);

# print(typings);


# Types = typings;
Instances = {};


def id(length):
    random.seed(length);
    thing = random.random();

    for i in range(length):
        thing = thing*10;

    return str(round(thing));

class Event:
    def __init__(self, *args):

        name = None;
        parent = None;

        if len(args) >= 1:
            name = args[0];
        
        if len(args) >= 2:
            parent = args[1];

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


class Project:

    def ping(self):
        self.events['ping'].Fire(self);

    def __init__(self, *args):

        options = args[0];

        self.events = {}

        self.events = {
            'ping': Event(),
            'eventCreated': Event(),
        }

        class ProjectOn:
            def __init__(onSelf, event):
                onSelf.event = event;
                
            def __call__(onSelf, callback):
                self.events[onSelf.event].append(callback);

        self.on = ProjectOn;

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