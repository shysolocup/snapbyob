import json;


class DataObject:

    @property
    def first(self):
        return self.__data__[1];


    @property
    def last(self):
        return self.__data__[-1];


    @property
    def length(self):
        return len(self.__data__);
        

    def __init__(self, data : list = None):
        if not data:
            data = [];
        
        self.__data__ = data;

        '''
            [
                [ 'project', [
                    [ '@app',  "Snap! 10, https://snap.berkeley.edu" ],
                    [ '@name', projName ],
                    [ '@version', projVer ],
                    [ 'notes', [] ],
                    [ 'scenes', [
                        [ '@select', 1 ]
                    ]] 
                ]]
            ];
        '''


    def get(self, k):
        for e in self.__data__:
            if (type(e[1]) == DataObject and e[1].get("@name") and e[1].get("@name") == k) or (e[0] == k):
                return e[1];


    def set(self, k, v):
        for i, e in enumerate(self.__data__):
            if (type(e[1]) == DataObject and e[1].get("@name") and e[1].get("@name") == k) or (e[0] == k):
                
                print(k, e, v)

                if (type(e[1]) == DataObject and e[1].get("@name")) and (type(v) == DataObject and not v.get("@name")):
                    v.set("@name", e[1].get("@name"));

                self.__data__[i] = [ e[0], v ];
                return e[1];

        self.__data__.append([ k, v ]);


    def getFirstOfClass(self, c):
        for e in self.__data__:
            if e[0] == c:
                return e[1];

    
    def setFirstOfClass(self, c, v):
        for i, e in enumerate(self.__data__):
            if e[0] == c:

                if (type(e[1]) == DataObject and e[1].get("@name")) and (type(v) == DataObject and not v.get("@name")):
                    v.set("@name", e[1].get("@name"));

                self.__data__[i] = [ e[0], v ];
                return e[1];

        self.__data__.append([ c, v ]);

    
    def forEach(self, callback):
        for i, e in enumerate(self.__data__):

            name = e[0];

            if type(e[1]) == DataObject:
                name = e[1].get("@name");

            callback(name, e[1], e[0], i);


    def __len__(self):
        return len(self.__data__);


    def tostring(self):
        return str(self);