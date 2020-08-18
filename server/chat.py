

class Chat(object):

    def __init__(self):
        self.content = [("System", "New messages appear from the top.")]

    def update_chat(self, msg):
        self.content.append(msg)

    def get_chat(self):
        return self.content

    def __len__(self):
        return len(self.content)

    def append(self, msg):
        self.content.append(msg)

    def __repr__(self):
        return str(self)
