blockdata = {
    'name': 'move',
    'category': 'motion',
}

def callback(self, **kwargs):
    x = kwargs.get("x");
    y = kwargs.get("y");

    print(x, y);