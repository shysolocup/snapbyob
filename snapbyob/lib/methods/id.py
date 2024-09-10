import random

def id(length, cache):
    def gen():
        random.seed(length);
        thing = random.random();
        
        for i in range(length):
            thing = thing*10;
    
        return str(round(thing));

    g = gen();

    while cache.get(g):
        g = gen();
    
        if not cache.get(g):
            return g;

    return g;