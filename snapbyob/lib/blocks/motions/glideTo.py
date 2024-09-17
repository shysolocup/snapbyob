from ....lib.typings.TimeConv import TimeConv;

blockdata = {
    'name': '__',
    'category': 'motion',
}

def callback(self, s: int|float|str|TimeConv = None, x: int|float = None, y:int|float = None):
    print(s, x, y);