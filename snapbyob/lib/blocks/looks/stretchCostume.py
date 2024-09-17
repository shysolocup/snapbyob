from ....lib.typings.CostumeContext import CostumeContextItem;
from ....lib.typings.Costume import Costume;

blockdata = {
    'name': '__',
    'category': 'looks',
}

def callback(self, c: Costume | CostumeContextItem, x: int|float, y: int|float ):
    print(c, x, y);