blockdata = {
    'name': 'rotateCounterClockwise',
    'category': 'motion',
}

def callback(self, **kwargs):
    r = kwargs.get("r");
    print(r);