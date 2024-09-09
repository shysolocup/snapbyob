import random

def id(length):
    random.seed(length);
    thing = random.random();

    for i in range(length):
        thing = thing*10;

    return str(round(thing));