import json;


class DataObject:

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


    def first(self, offset=0):
        return self.__data__[0+offset][1];

    def last(self, offset=0):
        return self.__data__[(self.length-1)-offset][1];


    def get(self, k):
        for e in self.__data__:
            if (type(e[1]) == DataObject and e[1].get("@name") and e[1].get("@name") == k) or (e[0] == k):
                return e[1];


    def set(self, k, v):
        for i, e in enumerate(self.__data__):
            if (type(e[1]) == DataObject and e[1].get("@name") and e[1].get("@name") == k) or (e[0] == k):

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
    

    def setDeep(self, ref, value):
        global thing
        thing = self;
        reflist = [ thing ];

        if type(ref) == str:
            refs = ref.split(".");
            for i, r in enumerate(refs):

                if i == len(refs)-1:
                    if type(thing) == DataObject:
                        old = thing.get(r);
                        thing = thing.set(r, value);
                        return old
                    else:
                        try:
                            old = thing[r];
                            thing[r] = value;
                            return old
                        except:
                            old = getattr(thing, r);
                            setattr(thing, r, value);
                            return old;
                else:
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
            for i, r in enumerate(refs):

                if i == len(refs)-1:
                    if type(thing) == DataObject:
                        old = thing.get(r);
                        thing = thing.set(r, value);
                        return old
                    else:
                        try:
                            old = thing[r];
                            thing[r] = value;
                            return old
                        except:
                            old = getattr(thing, r);
                            setattr(thing, r, value);
                            return old;
                else:
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

        passtypes = [
            str,
            int,
            float,
            complex,
            bool,
        ];


        def doesPass(v):
            for t in passtypes:
                if t == type(v):
                    return True;
            return False;


        formatted = {};


        @self.forEach
        def callback(k, v, c, i):
            try:
                getattr(formatted, k);

                numb = 1;
                while True:
                    s = f"{k}.{numb}";

                    try:
                        getattr(formatted, s);
                        numb += 1; 
                    except:
                        if doesPass(v):
                            if type(v) == str:
                                formatted[s] = f"{v}";
                            else:
                                formatted[s] = v;
                        else:
                            formatted[k] = f'*TYPE_START*{type(v).__name__}*TYPE_END*';
                        break;
             
            except:

                if doesPass(v):
                    if type(v) == str:
                        formatted[k] = f"{v}";
                    else:
                        formatted[k] = v;
                else:
                    formatted[k] = f'*TYPE_START*{type(v).__name__}*TYPE_END*';


        formattedStr = json.dumps(formatted, indent=4);

        formattedStr = formattedStr.replace('"*TYPE_START*', "");
        formattedStr = formattedStr.replace('*TYPE_END*"', "");

        if name:
            return f"[DataObject] \"{name}\" ({self.length}) {formattedStr}";  
        else:
            return f"[DataObject] ({self.length}) {formattedStr}";


    def tostring(self):
        return str(self);