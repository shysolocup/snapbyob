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

            if type(e[1]) == DataObject and e[1].get("@name"):
                name = e[1].get("@name");

            callback(name, e[1], e[0], i);
    

    def getDeep(self, ref):
        global thing
        thing = self;
        reflist = [ thing ];

        if type(ref) == str:
            refs = ref.split(".");
            for r in refs:
                if type(thing) == DataObject:
                    thing = thing.get(r);
                    reflist.append(thing);
                else:
                    try:
                        thing = thing[r];
                        reflist.append(thing);
                    except:
                        thing = getattr(thing, r);
                        reflist.append(thing);
        

        elif type(ref) == list:
            refs = ref;
            for r in refs:
                if type(thing) == DataObject:
                    thing = thing.get(r);
                    reflist.append(thing);
                else:
                    try:
                        thing = thing[r];
                        reflist.append(thing);
                    except:
                        thing = getattr(thing, r);
                        reflist.append(thing);
        
        thing = reflist[-1];

        return thing;


    def __len__(self):
        return len(self.__data__);


    def __str__(self):
        name = self.get("@name");

        formatypes = [
            str,
            int,
            float,
            dict,
            list,
            tuple
        ]

        formatted = {};

        if name:
            return f"<DataObject \"{name}\" ({self.length})>";  
        else:
            return f"<DataObject] ({self.length})>";


    def tostring(self):
        return str(self);