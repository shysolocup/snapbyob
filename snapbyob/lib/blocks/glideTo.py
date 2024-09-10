blockdata = {
    'name': 'glideTo',
    'category': 'motion',
}

def callback(self, **kwargs):
    s = kwargs.get("s");
    x = kwargs.get("x");
    y = kwargs.get("y");
    
    print(s, x, y);