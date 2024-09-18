import copy


class Children:
    def __init__(self, proj, scene, parent):
        self.parent = parent;
        self.scene = scene;
        self.project = proj;

    @property
    def keys(self):
        return list(self.list.keys());
        
    @property
    def values(self):
        return list(self.list.values());

    @property
    def list(self):
        l = copy.copy(self.__dict__);
    
        rem = [ 'parent', 'scene', 'project'];
        for r in rem:
            if l.get(r):
                del l[r];

        return l;

    @property
    def first(self):
        return self.list[1];

    @property
    def last(self):
        return self.list[-1];

    def getByName(self, k):
        for name, child in self.__dict__.items():
            name = name.split("_")[1]
            if name == k:
                return child;

    def getById(self, i):
        for name, child in self.__dict__.items():
            name = name.split("_")[2]
            if name == i:
                return child;

    def set(self, k, v):
        return exec('self.{0} = v'.format(k));

    def new(self, block):
        return self.set(block.name+"_"+block.id, block);
        