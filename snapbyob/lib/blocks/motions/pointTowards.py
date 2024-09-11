from ....lib.typings.Point import Point;

blockdata = {
    'name': 'pointTowards',
    'category': 'motion',
}

def callback(self, point: Point):
    print(point);