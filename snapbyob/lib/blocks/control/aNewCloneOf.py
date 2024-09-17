from ....lib.typings.CloneContext import CloneContextItem;
from ....lib.typings.Sprite import Sprite;

blockdata = {
    'name': '__',
    'category': 'control',
}

def callback(self, ctx: CloneContextItem | Sprite ):
    print(ctx);