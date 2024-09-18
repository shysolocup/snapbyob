from .pingtime import pingtime;
import random

def id(length, cache):
    def gen():
        random.seed(pingtime());
        thing = random.random();
        
        for i in range(length):
            thing = thing*10;
    
        return str(round(thing));

    g = gen();

    while cache.get(g):
        g = gen();
    
        if not cache.get(g):
            cache[len(cache)] = g;
            return g;

    cache[g] = 0;

    return g;