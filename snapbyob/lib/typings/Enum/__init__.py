class Enum:
    def __init__(self, proj, scene):
        self.project = proj;
        self.scene = scene;

        for n, c in self.constructors.items():
            typ = c(self);
    
            setattr(self, n, typ);
    


    def test(self):
        print(self);

    constructors = {};