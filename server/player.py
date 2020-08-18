# player object


class Player(object):
    
    def __init__(self, ip, name):
        self.ip = ip
        self.name = name
        self.balance = 100
        self.stock = [0, 0, 0, 0, 0, 0, 0, 0]

    def update_balance(self, x):
        self.balance += x

    def transaction(self, guess):

        pass

    def disconnect(self):
        pass

    def get_score(self):
        return self.score

    def get_name(self):
        return self.name

    def get_ip(self):
        return self.ip
