from ....lib.typings.BlockInstance import BlockInstance;
from ....lib.typings.Block import Block;

blockdata = {
    'name': '__',
    'category': 'control',
}

def callback(self, cond1: bool | BlockInstance | Block | dict = None, cond2 : bool | BlockInstance | Block | dict = None):
    print(cond1, cond2);