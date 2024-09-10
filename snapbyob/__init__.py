import random;
import json;
import requests;
import asyncio;
import os;
import pathlib;


import xml.etree.ElementTree as ET;
import xmltodict as xml;


# print(requests.get('https://snap.berkeley.edu/api/v1/projects/adfs/test'));


dirstring = os.path.realpath(__file__).replace("__init__.py", "");
splitpath = os.path.splitroot(dirstring);
drive, sep, path = splitpath;

separated = path.split(sep);
separated.pop();


def formFiles(extensions):
    d = separated;

    for e in extensions:
        d.append(e);
    
    adir = '{drive}{sep}{path}'.format(drive=drive, sep=sep, path=sep.join(d));

    stuff = {};

    for file in os.listdir(adir):
        filename = os.fsdecode(file);

        if not filename.endswith(".py"):

            modstring = ".{0}.{1}".format('.'.join(extensions), filename);
            stuff[filename] = modstring;

    return stuff;


rawtypes = formFiles([ 'lib', 'typings' ]);

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