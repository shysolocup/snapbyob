import random;
import json;
import requests;
import asyncio;


import xml.etree.ElementTree as ET;
import xmltodict as xml;


# print(requests.get('https://snap.berkeley.edu/api/v1/projects/adfs/test'));


rawtypes = {
    'Event': '.lib.typings.Event',
    'Project': '.lib.typings.Project',
    'BlockInstance': '.lib.typings.BlockInstance',
    'Block': '.lib.typings.Block',
    'Scripts': '.lib.typings.Scripts',
    'BlockHolder': '.lib.typings.BlockHolder'
};


class NewTypings:
    pass


Typings = NewTypings();


for n, d in rawtypes.items():
    exec('from {d} import {n}'.format(d=d, n=n));
    exec('Typings.{n} = {n}'.format(d=d, n=n));
    


# print(stuff);

# print(typings);


# Types = typings;
Instances = {};