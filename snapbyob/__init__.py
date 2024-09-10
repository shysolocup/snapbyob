import os;


import xml.etree.ElementTree as ET;
import xmltodict as xml;


from .lib.methods.formFiles import formFiles


# print(requests.get('https://snap.berkeley.edu/api/v1/projects/adfs/test'));


dirstring = os.path.realpath(__file__).replace("__init__.py", "");
splitpath = os.path.splitroot(dirstring);
drive, sep, path = splitpath;

separated = path.split(sep);
separated.pop();

rawtypes = formFiles(drive, sep, separated, '.', [ 'lib', 'typings' ]);

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