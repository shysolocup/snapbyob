import os;
import pathlib;


def formFiles(drive, sep, separated, ref, extensions):
    d = separated;

    for e in extensions:
        d.append(e);
    
    adir = '{drive}{sep}{path}'.format(drive=drive, sep=sep, path=sep.join(d));

    stuff = {};

    for file in os.listdir(adir):
        if not file.startswith("__") and not file.endswith("__"):
            filename = os.fsdecode(file);

            modstring = "{0}{1}.{2}".format(ref, '.'.join(extensions), filename.replace('.py', ''));
            stuff[filename.replace('.py', '')] = modstring;

    return stuff;