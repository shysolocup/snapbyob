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
    actions = self.actions.values;
    args = list(self.args);

    statements = [];

    for i, c in enumerate(args):
        a = actions[i];
        statements.append({ 'condition': c, 'action': a});

    print(statements);