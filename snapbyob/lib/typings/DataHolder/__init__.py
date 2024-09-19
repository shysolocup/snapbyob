class DataHolder:
    data = []

    def setDataItem(self, ref, value):
        reflist = [ self.data ];

        def doit(refs):
            for i, r in enumerate(refs):
                thing = reflist[-1];
                for i2, d in enumerate(thing):
                    for d2 in d[1]:
                        pass;
                    

        if type(ref) == str:
            refs = ref.split(".");
            doit(refs);
        
        elif type(ref) == list:
            doit(ref);
        

        thing = reflist[-1];
    
        return thing;


    def newDataItem(self, ref, value):
        reflist = [ self.data ];

        def doit(refs):
            for i, r in enumerate(refs):
                thing = reflist[-1];

                for i2, d in enumerate(thing):
                    pass;

        if type(ref) == str:
            refs = ref.split(".");
            doit(refs);
        
        elif type(ref) == list:
            doit(ref);
        

        thing = reflist[-1];
    
        return thing;



    def getDataItem(self, ref):
        reflist = [ getattr(self, "data") ];


        def doit(refs):
            for r in refs:
                thing = reflist[-1];

                if type(thing) == list:

                    for first in thing:
                        key = first[0];
                        item = first[1];

                        # if it has a "name" or "@name" key and the name matches up with the ref

                        if type(item) == list:
                            for inner in item:
                                
                                innerkey = inner[0];
                                inneritem = inner[1];

                                if (innerkey == "name" or innerkey == "@name") and inneritem == r:
                                    reflist.append(item);


                        # if the key of the element matches up with the ref

                                elif key == r:
                                    reflist.append(item);

                        elif key == r:
                            reflist.append(item);



        # doits
        if type(ref) == str:
            refs = ref.split(".");
            doit(refs);
        

        elif type(ref) == list:
            doit(ref);
        

        thing = reflist[-1];
        return thing;