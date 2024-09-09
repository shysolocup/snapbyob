import random;
import json;
import requests;
import asyncio;


import xml.etree.ElementTree as ET;
import xmltodict as xml;


# print(requests.get('https://snap.berkeley.edu/api/v1/projects/adfs/test'));


# methods
from .lib.methods.id import id


# types
from .lib.typings.Event import Event
from .lib.typings.Project import Project


Typings = {
    "Event": Event,
    "Project": Project
}


# print(stuff);

# print(typings);


# Types = typings;
Instances = {};