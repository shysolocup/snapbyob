class TimeConv:
    def __init__(self, *args, **kwargs):
        self.value = self.format(*args, **kwargs);

    def format(self, x:str = None):
        if type(self) == str and not x:
            x = self;

        conv = {
            "s": 1,
            "m": 60,
            "h": 60^2
        };

        for u, c in conv.items():
            if u in x:
                n = (float(x.replace(u, ""))) * c;
                return n;
                