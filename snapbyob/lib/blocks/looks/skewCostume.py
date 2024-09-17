from ....lib.typings.CostumeContext import CostumeContextItem;
from ....lib.typings.Costume import Costume;

blockdata = {
    'name': '__',
    'category': 'looks',
}

def callback(self, c: Costume | CostumeContextItem, r: int|float ):
    print(c, r);