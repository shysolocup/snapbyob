from ....lib.methods.actions import actions;
from ....lib.typings.BlockInstance import BlockInstance;
from ....lib.typings.Block import Block;


blockdata = {
    'name': '__',
    'category': 'control',
    'mods': [
        actions
    ]
}

def callback(self, *args):
    actions = self.actions.list;
    args = list(self.args);

    print(actions.values);
    print(args);