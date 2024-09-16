from ....lib.typings.TimeConv import TimeConv

blockdata = {
    'name': '__',
    'category': 'control',
}

def callback(self, t:str | TimeConv | int):
    print(t);