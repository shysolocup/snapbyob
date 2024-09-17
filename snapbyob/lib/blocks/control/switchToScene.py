from ....lib.typings.SceneContext import SceneContextItem;
from ....lib.typings.Scene import Scene;

blockdata = {
    'name': '__',
    'category': 'control',
}

def callback(self, ctx: SceneContextItem | Scene ):
    print(ctx);