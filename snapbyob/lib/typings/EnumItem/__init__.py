from ..Enum import Enum


class EnumItem:
    masked = False

    def __init__(self):
        for i, k in enumerate(self.__items__):
            if self.__class__.__dict__.get("__typeclass__"):
                t = self.__typeclass__(k, i, self);
                exec("self.{0} = t".format(k));
            else:
                exec("self.{0} = i".format(k));

        exec('Enum.{0} = self'.format(self.__enumname__));