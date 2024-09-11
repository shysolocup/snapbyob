from ....lib.typings.Point import Point

blockdata = {
    'name': 'goTo',
    'category': 'motion',
}

def callback(self, x:int = None, y:int = None, point:Point = None):
    print(x, y, point);