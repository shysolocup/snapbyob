class Children:
    def __init__(self, proj, parent):
        self.parent = parent;
        self.project = proj

    @property
    def list(self):
        return self.__dict__;

    @property
    def first(self):
        return list(self.__dict__.items())[1];

    @property
    def last(self):
        return list(self.__dict__.items())[-1];

    def getByName(self, k):
        return exec('self.{0}'.format(k));

    def getById(self, i):
        return exec('self.{0}'.format(i));

    def set(self, k, v):
        return exec('self.{0} = v'.format(k));

    def new(self, block):
        return self.set(block.name+"_"+block.id, block);
        