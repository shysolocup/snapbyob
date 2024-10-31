class Color3:
    @property
    def red(self): return self.r
    
    @property
    def green(self): return self.g
    
    @property
    def blue(self): return self.b
    
    @property
    def transparency(self): return self.t
    @property
    def opacity(self): return self.t


    def toRGB(self):
        return self.r, self.g, self.b, self.t;

    def fromRGB(self, r=255, g=255, b=255, t=1):
        return self.__init__(r/255, g/255, b/255, t)
    

    def __str__(self):
        r, g, b, t = self.toRGB();
        return f"{r},{g},{b},{t}"; 
    tostring = lambda self : str(self)


    def __init__(self, r=1, g=1, b=1, t=1):
        self.r = r;
        self.g = g;
        self.b = b;
        self.t = t;