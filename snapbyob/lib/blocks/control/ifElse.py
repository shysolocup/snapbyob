blockdata = {
    'name': 'ifElse',
    'category': 'control',
}

callback = [];

def ifX(self, v:bool=None):
    print(v);

def ifElse(self):
    print("else");

callback.append(ifX);
callback.append(ifElse);