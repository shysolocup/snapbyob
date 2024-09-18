from ....lib.methods.conditional import conditional;


blockdata = {
    'name': '__',
    'category': 'control',
    'mods': {
        'conditions': conditional
    }
}

def callback(self, b:bool=None):
    print(self.conditions.list);