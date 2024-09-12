from ....lib.typings.Context import ContextItem


blockdata = {
    'name': 'stop',
    'category': 'control',
}

def callback(self, ci:ContextItem):
    print(ci);