import os;
from .lib.methods.formFiles import formFiles


# print(requests.get('https://snap.berkeley.edu/api/v1/projects/adfs/test'));


dirstring = os.path.realpath(__file__).replace("__init__.py", "");
splitpath = os.path.splitroot(dirstring);
drive, sep, path = splitpath;

separated = path.split(sep);
separated.pop();

rawtypes = formFiles(drive, sep, separated, '.', [ 'lib', 'typings' ]);

class NewTypings:
    def get(self, t):
        return self.__dict__.get(t);


Typings = NewTypings();

for n, d in rawtypes.items():
    ex = 'from {d} import {n}'.format(d=d, n=n)
    exec(ex);
    exec('Typings.{n} = {n}'.format(d=d, n=n));