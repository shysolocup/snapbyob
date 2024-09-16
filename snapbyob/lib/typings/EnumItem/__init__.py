from ..Enum import Enum


def getstuff(a, b):
    try:
        return a[b];
    except:
        return exec('a.{b}'.format(b=b));

    


class EnumItem:
    masked = False

    def __getattr__(self, k):
        stuff = {};
        
        for i, k in enumerate(self.__propitems__()):
            if self.__class__.__dict__.get("__typeclass__"):
                t = self.__typeclass__(k, i, self);
                stuff[k] = t;
            else:
                stuff[k] = i;
        
        return stuff[k];

    def __init__(self):
        if self.__class__.__dict__.get("__propitems__"):
            pass
            # self.__get__ = lambda self, k : print('a'); # self.__dict__[k] or get(self.__propitems__(), k);
            
        if self.__class__.__dict__.get("__items__"):
            for i, k in enumerate(self.__items__):
                if self.__class__.__dict__.get("__typeclass__"):
                    t = self.__typeclass__(k, i, self);
                    exec("self.{0} = t".format(k));
                else:
                    exec("self.{0} = i".format(k));

        exec('Enum.{0} = self'.format(self.__enumname__));