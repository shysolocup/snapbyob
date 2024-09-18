from ....lib.typings.TouchingInteraction import TouchingInteractionItem;

blockdata = {
    'name': '__',
    'category': 'sensing',
}

def callback(self, i: TouchingInteractionItem, b:bool=False):
    print(i, b);