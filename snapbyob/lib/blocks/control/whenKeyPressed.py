from ....lib.typings.Keycode import Key;

blockdata = {
    'name': 'whenKeyPressed',
    'category': 'control',
}

def callback(self, key: Key):
    print(key);