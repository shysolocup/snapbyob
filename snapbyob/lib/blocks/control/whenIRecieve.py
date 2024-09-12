from ....lib.typings.Message import MessageItem;

blockdata = {
    'name': 'whenIRecieve',
    'category': 'control',
}

def callback(self, msg: MessageItem):
    print(msg);