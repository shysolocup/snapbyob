from ....lib.methods.conditional import conditional;

blockdata = {
    'name': '__',
    'category': 'control',
    'mods': {
        'conditions': conditional
    }
}

callback = [];

def ifX(self, v:bool=None):
    print(v);

def ifElse(self):
    print("else");

callback.append(ifX);
callback.append(ifElse);