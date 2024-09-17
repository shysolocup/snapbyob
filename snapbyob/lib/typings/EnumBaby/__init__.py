from ..EnumItem import EnumItem;

class EnumBaby:
    def __init__(self, value, id, enumitem, enum=None):
        self.id = id;
        self.value = value;
        self.enum = enum;
        self.enumitem = enumitem;

    def isA(self, ei: EnumItem):
        return self.enumitem == ei;
        

baseeq = EnumBaby.__eq__;
basene = EnumBaby.__ne__;

def testCom(com):
    try:
        return not com.masked;
    except:
        return False;

EnumBaby.__eq__ = lambda self, com : self.enumitem == com if testCom(com) else baseeq(self, com);
EnumBaby.__ne__ = lambda self, com : self.enumitem != com if testCom(com) else basene(self, com);