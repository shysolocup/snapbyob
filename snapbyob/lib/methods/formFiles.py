import os;
import copy

def formFiles(drive, sep, separated, ref, extensions, adir=None, bdir=None):
    d = copy.copy(separated)
    ext = copy.copy(extensions);

    for e in extensions:
        d.append(e);

    if not adir:
        adir = '{drive}{sep}{path}'.format(drive=drive, sep=sep, path=sep.join(d));

    stuff = {};

    if bdir:
        for file in os.listdir(bdir):
            if not file.startswith("__") and not file.endswith("__"):
                filename = os.fsdecode(file);

                modstring = "{1}{0}{1}{2}".format('.'.join(ext), ref, filename.replace('.py', ''));
                stuff[filename.replace('.py', '')] = modstring;
    
    else:
        for file in os.listdir(adir):
            if not file.startswith("__") and not file.endswith("__"):
                filename = os.fsdecode(file);

                modstring = "{1}{0}{1}{2}".format('.'.join(ext), ref, filename.replace('.py', ''));
                stuff[filename.replace('.py', '')] = modstring;

    return stuff;