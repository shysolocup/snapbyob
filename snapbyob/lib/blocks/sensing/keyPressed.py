from ....lib.typings.Keycode import Key;

blockdata = {
    'name': '__',
    'category': 'sensing',
}

def callback(self, k: Key, b:bool=False):
    print(k);