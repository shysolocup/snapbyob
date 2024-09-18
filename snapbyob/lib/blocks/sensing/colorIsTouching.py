from ....lib.typings.Color3 import Color3;

blockdata = {
    'name': '__',
    'category': 'sensing',
}

def callback(self, c1:Color3, c2: Color3, b:bool=False):
    print(c1, c2, b);