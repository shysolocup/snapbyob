from ....lib.typings.MouseInteraction import MouseInteractionItem;

blockdata = {
    'name': 'whenIAm',
    'category': 'control',
}

def callback(self, i: MouseInteractionItem):
    print(i);