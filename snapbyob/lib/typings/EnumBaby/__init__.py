from ..EnumItem import EnumItem;

class EnumBaby:
    def __init__(self, value, id, enum):
        self.id = id;
        self.value = value;
        self.enum = enum;

    def isA(self, ei: EnumItem):
        return self.enum == ei;
        

baseeq = EnumBaby.__eq__;
basene = EnumBaby.__ne__;

def testCom(com):
    try:
        return not com.masked;
    except:
        return False;

EnumBaby.__eq__ = lambda self, com : self.enum == com if testCom(com) else baseeq(self, com);
EnumBaby.__ne__ = lambda self, com : self.enum != com if testCom(com) else basene(self, com);