blockdata = {
    'name': 'rotateClockwise',
    'category': 'motion',
}

def callback(self, **kwargs):
    r = kwargs.get("r");
    print(r);