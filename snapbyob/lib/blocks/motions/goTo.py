blockdata = {
    'name': 'goTo',
    'category': 'motion',
}

def callback(self, **kwargs):
    x = kwargs.get("x");
    y = kwargs.get("y");
    point = kwargs.get("point");

    print(x, y, point);