from random import randint, random
from server.chat import Chat
from server.player import Player


# server side object
class ServerInstance:
    def __init__(self, player1name="Player", player2name="Computer 3",
                 player3name="Computer 2", player4name="Computer 1", settings=None):
        self.multiplayer = True
        self.GameObjects = [None, None, None, None]
        self.day_limit = 20
        self.day_timer = 25
        self.night_timer = 15
        self.disabled_events = []
        g1, g2, g3, g4 = randint(0, 7), randint(0, 7), randint(0, 7), randint(0, 7)
        while g2 == g1 or g2 == g3 or g2 == g4:
            g2 = randint(0, 7)
        while g3 == g1 or g3 == g2 or g3 == g4:
            g3 = randint(0, 7)
        while g4 == g1 or g4 == g2 or g4 == g3:
            g4 = randint(0, 7)
        for setting in settings:
            if setting[0] == 0:
                self.day_limit = setting[1]
            elif setting[0] == 1:
                self.day_timer = setting[1]
            elif setting[0] == 2:
                self.night_timer = setting[1]
            elif setting[0] == 3:
                self.disabled_events = setting[1]
            elif setting[0] == 4:
                g1, g2, g3, g4 = setting[1][0:3]
        self.day = 0
        self.prices = [[1.0], [1.0], [1.0], [1.0]]
        self.dayevent = []
        for de in range(0, self.day_limit + 1):
            if de > 0 and de % 3 == 0:
                evnt = randint(1, 9)
                while evnt in self.disabled_events:
                    evnt = randint(1, 9)
                self.dayevent.append(evnt)
                if evnt == 6:
                    modifier = 1.5
                elif evnt == 7:
                    modifier = 0.5
                else:
                    modifier = 1
            else:
                self.dayevent.append(0)
                modifier = 1
            for vg in range(4):
                self.prices[vg].append(
                    modifier * self.prices[vg][de] * (
                            1 + (0.2 - 0.4 * random()) + 0.05 * (1.2 - modifier * self.prices[vg][de])))
                if self.prices[vg][de + 1] > 2.8:
                    self.prices[vg][de + 1] = 2.8
        self.g1, self.g2, self.g3, self.g4 = g1, g2, g3, g4
        self.g = [g1, g2, g3, g4]
        self.balance = 100.00
        self.player1 = player1name
        self.player2 = player2name
        self.player3 = player3name
        self.player4 = player4name
        self.time = 60
        self.nighttime = True
        self.prediction_text = ""
        self.chat = Chat()
        self.players = [  # prediction vegetables will be based on g[rank - 1]
            {
                "name": self.player1,
                "net_worth": 100,
                "offer": [True, 0],
                "rank": 1
            },
            {
                "name": self.player2,
                "net_worth": 100.00,
                "offer": [True, 0],
                "rank": 2
            },
            {
                "name": self.player3,
                "net_worth": 100.00,
                "offer": [True, 0],
                "rank": 3
            },
            {
                "name": self.player4,
                "net_worth": 100.00,
                "offer": [True, 0],
                "rank": 4
            },
        ]
        self.vegetables = [
            {
                "id": 0,
                "name": "Potatoes",
                "cost": 0.50,
                "init_stock": 150,
                "count": 0,
                "stock": 100,

            },
            {
                "id": 1,
                "name": "Carrots",
                "cost": 0.75,
                "init_stock": 120,
                "count": 0,
                "stock": 120,
            },
            {
                "id": 2,
                "name": "Wheat",
                "cost": 1.00,
                "count": 0,
                "stock": 100,
                "init_stock": 100,
            },
            {
                "id": 3,
                "name": "Tomatoes",
                "cost": 2.00,
                "count": 0,
                "stock": 50,
                "init_stock": 50,
            },
            {
                "id": 4,
                "name": "Corn",
                "cost": 4.00,
                "init_stock": 30,
                "count": 0,
                "stock": 30,
            },
            {
                "id": 5,
                "name": "Cabbages",
                "cost": 6.00,
                "count": 0,
                "stock": 20,
                "init_stock": 20,
            },
            {
                "id": 6,
                "name": "Pumpkins",
                "cost": 8.00,
                "init_stock": 10,
                "count": 0,
                "stock": 10,
            },
            {
                "id": 7,
                "name": "Melons",
                "cost": 10.00,
                "init_stock": 10,
                "count": 0,
                "stock": 10,
            }
        ]

    def update_constant(self):
        if not self.multiplayer:
            self.time -= 1

    def update_daily(self):
        if not self.multiplayer:
            if self.day > 0:
                self.sort_four()
        else:
            # update rank variables from server
            pass

    def sort_four(self):
        if self.players[0]["net_worth"] < self.players[1]["net_worth"]:
            low1 = 0
            high1 = 1
        else:
            low1 = 1
            high1 = 0
        if self.players[2]["net_worth"] < self.players[3]["net_worth"]:
            low2 = 2
            high2 = 3
        else:
            low2 = 3
            high2 = 2
        if self.players[low1]["net_worth"] < self.players[low2]["net_worth"]:
            lowest = low1
            middle1 = low2
        else:
            lowest = low2
            middle1 = low1
        if self.players[high1]["net_worth"] > self.players[high2]["net_worth"]:
            highest = high1
            middle2 = high2
        else:
            highest = high2
            middle2 = high1
        if self.players[middle1]["net_worth"] <= self.players[middle2]["net_worth"]:
            wall = [lowest, middle1, middle2, highest]
        else:
            wall = [lowest, middle2, middle1, highest]
        ranks = 1
        for rank in reversed(wall):
            self.players[rank]["rank"] = ranks
            ranks += 1

    def next_day(self):
        if self.day < self.day_limit:
            self.time = self.day_timer
            self.nighttime = False
            self.day += 1
            return True
        else:
            return False

    def next_night(self):
        self.time = self.night_timer
        self.nighttime = True
        networth = self.balance
        for veggie in range(4):
            networth += self.vegetables[self.g[veggie]]["cost"] * self.vegetables[self.g[veggie]]["count"] * \
                        self.prices[veggie][
                            self.day + 1]
        self.players[0]["net_worth"] = networth
        self.update_daily()

    def send_message(self, msg):
        if not self.multiplayer:
            self.chat.append((self.player1, msg))
