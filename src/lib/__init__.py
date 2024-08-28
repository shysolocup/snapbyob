import os;
stuff = {};

dir = os.path.realpath(__file__).replace("__init__.py", "")

__path__ = __import__('pkgutil').extend_path(dir, __name__)

for file in os.listdir(dir):
    filename = os.fsdecode(file);

    if not filename.endswith(".py"):

        modstring = "{0}".format(filename);
        dirstring = "{0}/{1}/__init__.py".format(dir, filename);

        # print(modstring);

        # print(os.path.isfile(dirstring))

        if os.path.isfile(dirstring):

            # module = __import__(modstring);
            exec("from {0}{1} import *".format(".", filename));
            # print(module)

            # stuff[filename] = module;

        # exec('typings[' + filename + '] = ' + filename);