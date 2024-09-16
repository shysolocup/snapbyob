from ....lib.typings.Message import MessageItem;

blockdata = {
    'name': '__',
    'category': 'control',
}

def callback(self, msg: MessageItem):
    print(msg);