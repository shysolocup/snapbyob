from ....lib.typings.Point import Point

blockdata = {
    'name': '__',
    'category': 'motion',
}

def callback(self, x: int|float = None, y: int|float = None, point:Point = None):
    print(x, y, point);