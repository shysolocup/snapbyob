from ....lib.typings.Message import MessageItem;

blockdata = {
    'name': 'broadcast',
    'category': 'control',
}

def callback(self, msg: MessageItem):
    print(msg);