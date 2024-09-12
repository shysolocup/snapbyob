from ....lib.typings.Message import MessageItem;

blockdata = {
    'name': 'broadcastAndWait',
    'category': 'control',
}

def callback(self, msg: MessageItem):
    print(msg);