from random import random, randint

import pygame

from client.pygame_functions.roundedrect import AAfilledRoundedRect

pygame.init()


# hover = what button to hover over, main = main menu buttons (0 = none, 1 = play, 2 = help, 3 = credits, 4 = quit)
# type = game mode (1 = single-player, 2 = multi-player, 3 = back), exit = when 1 will set all others to 0)


# ------------------------------------------------


def make_dollars(dollars):
    dollars = str(round(dollars, 2))
    if dollars[-2:-1] == ".":
        dollars += "0"
    return dollars


class ClientInstance:

    def __init__(self):
        self.GameObject = None
        self.WIDTH = 1080
        self.HEIGHT = 720
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.icon = pygame.image.load("images/Icon.png")
        self.icon.set_colorkey((0, 255, 255))
        pygame.display.set_icon(self.icon)
        self.last_next_item = 0
        self.last_keyboard_choose = 0
        self.title_background = pygame.transform.scale2x(pygame.image.load("images/scrolling_ground2.png"))
        self.game_background = pygame.image.load("images/back.png")
        self.night_background = pygame.image.load("images/NightHills.png")
        self.clouds = pygame.image.load("images/Sky.png").convert()
        self.nightclouds = pygame.image.load("images/Night.png").convert()
        self.title = pygame.image.load("images/title.png")
        self.carrot = pygame.image.load("images/Carrot.png")
        self.potato = pygame.image.load("images/Potato.png")
        self.wheat = pygame.image.load("images/Wheat.png")
        self.tomato = pygame.image.load("images/Tomato.png")
        self.corn = pygame.image.load("images/Corn.png")
        self.cabbage = pygame.image.load("images/Cabbage.png")
        self.pumpkin = pygame.image.load("images/Pumpkin.png")
        self.melon = pygame.image.load("images/Melon.png")
        pygame.mixer.music.load("music/SlushHike.mp3")
        self.valid_chars = "`1234567890-= qwertyuiop[]\\asdfghjkl;'zxcvbnm,./" + '~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'
        self.valid_nums = "1234567890"
        self.inventory_open = False
        self.loading = False
        self.run = True
        self.menu = True
        self.game = False
        self.chatbox = False
        self.quantitybox = False
        self.settings = False
        self.market = False
        self.exchange = False
        self.over_box_limit = False
        self.offerbox_txt = "0"
        self.offer = True
        self.offerbox = False
        self.box_filled_color_title = (120 - 16, 150, 80 - 16)
        self.background_color = (120 - 16, 160, 80 - 16)
        self.sky_blue = (135, 206, 235)
        self.bright_green_title = self.box_filled_color_title
        self.green_title = (120, 180, 80)
        self.white = (253, 245, 232)
        self.dark_white = (253 - 25, 245 - 25, 232 - 25)
        self.beige = (198, 198, 178)
        self.beige2 = (188, 188, 168)
        self.beige3 = (168, 168, 148)
        self.brown = (153, 102, 51)
        self.light_brown = (204, 153, 0)
        self.black = (0, 0, 0)
        self.yellow = (120 - 16, 140, 80 - 16)
        self.X = 0
        self.Y = 0
        self.x, self.y = pygame.mouse.get_pos()
        self.Y_increment = 0.2
        self.RGB = 20
        self.RGB_increment = 3
        self.inventory_percentage = 0.3
        self.cloud_x = 1500
        self.market_selection = 1
        pygame.font.init()
        self.font2 = pygame.font.Font("fonts/orange_juice.ttf", 60)
        self.font3 = pygame.font.SysFont("freesansbold.ttf", 22)
        self.font1 = pygame.font.SysFont("Arial", 30)
        self.font4 = pygame.font.SysFont("Segoe UI", 30)
        self.font5 = pygame.font.Font("fonts/orange_juice.ttf", 35)
        self.newspaperfont = pygame.font.SysFont("Monotype Corsiva", 60)
        self.newspaperfont2 = pygame.font.SysFont("Monotype Corsiva", 30)
        pygame.display.set_caption("The Farmer's Market")
        pygame.mixer.music.play(-1)
        self.menu_gui = {"hover": 1, "main": 0, "type": 0}
        # self.delta1, self.delta2, self.delta3, self.delta4 = 1, 1, 1, 1
        self.e = [self.potato, self.carrot, self.wheat, self.tomato, self.corn, self.cabbage, self.pumpkin, self.melon]
        # self.d = [self.delta1, self.delta2, self.delta3, self.delta4]
        self.chat_gui = False
        self.leaderboard = False
        self.chatbox_msg = "Enter message"
        self.quantitybox_txt = "Custom"
        self.prediction_text = "NONE"
        self.quantity = 1
        self.night = 0
        self.loading_X = 0
        # self.daily_message = "Vegetables in stock this season: " + self.GameObject.vegetables[self.GameObject.g1][
        #    "name"] + ": $" + self.make_dollars(
        #    self.GameObject.vegetables[self.GameObject.g1]["cost"] * self.GameObject.prices[0][self.day]) + ", with " + str(
        #    self.GameObject.vegetables[self.GameObject.g1]["stock"]) + " in stock. " + \
        #                     self.GameObject.vegetables[self.GameObject.g2][
        #                         "name"] + ": $" + self.make_dollars(
        #    self.GameObject.vegetables[self.GameObject.g2]["cost"] * self.GameObject.prices[1][self.day]) + ", with " + str(
        #    self.GameObject.vegetables[self.GameObject.g2]["stock"]) + " in stock. " + self.GameObject.vegetables[self.GameObject.g3]["name"] + ": $" + self.make_dollars(
        #    self.GameObject.vegetables[self.GameObject.g3]["cost"] * self.GameObject.prices[2][self.day]) + ", with " + str(
        #    self.GameObject.vegetables[self.GameObject.g3]["stock"]) + " in stock. " + \
        #                     self.GameObject.vegetables[self.GameObject.g4][
        #                         "name"] + ": $" + self.make_dollars(
        #    self.GameObject.vegetables[self.GameObject.g4]["cost"] * self.GameObject.prices[3][self.day]) + ", with " + str(
        #    self.GameObject.vegetables[self.GameObject.g4]["stock"]) + " in stock. " + "High demand this season! " + "Here for " + str(
        #    self.GameObject.day_limit) + " days only!"
        # print(self.GameObject.dayevent)
        # print(self.GameObject.prices)
        self.Clock = pygame.time.Clock()
        self.inventory_position = -60 + self.inventory_percentage * 150
        self.title_height = self.font5.get_height() / 2 - 3
        self.bright_green = (183, 214, 143 - 10)
        self.green = (160, 200, 104)
        self.background_filled_color = (183, 221, 176 - 25)
        self.news = True
        self.dark_green = (92, 158, 64)
        self.inv1color, self.inv2color, self.inv3color, self.inv4color = self.bright_green, self.bright_green, self.bright_green, self.bright_green

    def make_text(self, text, font, color, center_x, center_y):
        text_surface = font.render(text, True, color)
        text_box = text_surface.get_rect()
        text_box.center = (center_x, center_y)
        self.window.blit(text_surface, text_box)

    def check_mouse_hover(self, click=False):
        self.x, self.y = pygame.mouse.get_pos()
        x, y = self.x, self.y
        if self.menu:
            if self.WIDTH * 0.25 <= x <= self.WIDTH * 0.75 and self.HEIGHT * 0.39 <= y <= self.HEIGHT * 0.49:
                self.menu_gui["hover"] = 1
                if click:
                    self.keyboard_choose()
            elif self.WIDTH * 0.25 <= x <= self.WIDTH * 0.75 and self.HEIGHT * 0.54 <= y <= self.HEIGHT * 0.64:
                self.menu_gui["hover"] = 2
                if click:
                    self.keyboard_choose()
            elif self.WIDTH * 0.25 <= x <= self.WIDTH * 0.75 and self.HEIGHT * 0.69 <= y <= self.HEIGHT * 0.79:
                self.menu_gui["hover"] = 3
                if click:
                    self.keyboard_choose()
            elif self.WIDTH * 0.25 <= x <= self.WIDTH * 0.75 and self.HEIGHT * 0.84 <= y <= self.HEIGHT * 0.94 and \
                    self.menu_gui["main"] == 0:
                self.menu_gui["hover"] = 4
                if click:
                    self.keyboard_choose()

    def mouse_choose(self):
        self.check_mouse_hover(True)

    def next_item(self, increment):
        if pygame.time.get_ticks() > self.last_next_item + 100:
            # goes to the next item in the gui
            self.menu_gui["hover"] += increment
            if self.menu_gui["main"] == 0 and self.menu_gui["hover"] > 4:
                self.menu_gui["hover"] = 1
            elif not self.menu_gui["main"] == 0 and self.menu_gui["type"] == 0 and self.menu_gui["hover"] > 3:
                self.menu_gui["hover"] = 1
            elif self.menu_gui["hover"] < 1 and self.menu_gui["main"] == 0:
                self.menu_gui["hover"] = 4
            elif self.menu_gui["hover"] < 1 and self.menu_gui["type"] == 0:
                self.menu_gui["hover"] = 3
            # elif menu_gui["exit"] == 0 and menu_gui["hover"] > 1:
            #    menu_gui["hover"] = 0
        self.last_next_item = pygame.time.get_ticks()

    def keyboard_choose(self):
        # presses the button that's hovered
        if pygame.time.get_ticks() > self.last_keyboard_choose + 100:
            if self.menu_gui["main"] == 0:
                if self.menu_gui["hover"] == 4:
                    self.run = False
                else:
                    self.menu_gui["main"] = self.menu_gui["hover"]
                    self.menu_gui["hover"] = 1
            elif self.menu_gui["type"] == 0:
                if self.menu_gui["hover"] == 3:
                    self.menu_gui["main"] = 0
                    self.menu_gui["hover"] = 1
                elif self.menu_gui["hover"] == 1 and self.menu_gui["main"] == 1:
                    self.menu = False
                    self.loading = True
                    self.load(mp=False)
                    self.game = True
                else:
                    self.menu_gui["type"] = self.menu_gui["hover"]
                    self.menu_gui["hover"] = 1
        self.last_keyboard_choose = pygame.time.get_ticks()

    def blit_text(self, max_width, max_height, text, pos, font, color=(153, 102, 51), extra_padding=0):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The self.WIDTH of a space.
        pos_x, pos_y = pos
        for line in words:
            word_height = 0
            for word in line:
                word_surface = font.render(word, True, color)
                word_width, word_height = word_surface.get_width(), word_surface.get_height() + extra_padding
                if pos_x + word_width >= pos[0] + max_width:
                    pos_x = pos[0]  # Reset the x.
                    pos_y += word_height  # Start on new row.
                if pos_y >= pos[1] + max_height - word_height:
                    return pos_y
                self.window.blit(word_surface, (pos_x, pos_y))
                pos_x += word_width + space
            pos_x = pos[0]  # Reset the x.
            pos_y += word_height  # Start on new row.
        return pos_y

    def send_message(self, msg):
        #    print(msg)
        self.GameObject.send_message(msg)
        self.over_box_limit = False
        return msg

    def generate_prediction(self):
        prices = self.GameObject.prices
        pred_veg = self.GameObject.players[self.GameObject.playerid]["rank"]
        # print("Prediction: " + str(prices[pred_veg][self.GameObject.day + 1]) + " vs " + str(prices[pred_veg][self.day]))
        if self.GameObject.day < self.GameObject.day_limit and prices[pred_veg][self.GameObject.day + 1] > prices[pred_veg][self.GameObject.day]:
            self.prediction_text = "UP"
        elif self.GameObject.day < self.GameObject.day_limit and prices[pred_veg][self.GameObject.day + 1] < prices[pred_veg][self.GameObject.day]:
            self.prediction_text = "DOWN"
        else:
            self.prediction_text = "NONE"
        return pred_veg

    def execute_event(self, event_number):
        self.daily_message = ""
        if self.GameObject.day <= 0:
            self.daily_title = "Farmers Markets Opens!"
            self.daily_message = "First time in the markets? Buy low and sell high to become the most profitable. Watch out for events every third day. "
        elif event_number == 0:
            self.daily_title = "Farmer's Market is Open!"
            self.daily_message = "Normal day today in the market. "
            for v in range(0, 4):
                self.GameObject.vegetables[self.GameObject.g[v]]["stock"] += round(0.2 * self.GameObject.vegetables[self.GameObject.g[v]]["init_stock"])
        elif event_number == 1:
            self.daily_title = "Stock Shortage!"
            self.daily_message = "A surge in demand has caused a shortage of produce. "
            for v in range(0, 4):
                self.GameObject.vegetables[self.GameObject.g[v]]["stock"] = round(0.5 * self.GameObject.vegetables[self.GameObject.g[v]]["stock"])
        elif event_number == 2:
            self.daily_title = "Stock surplus!"
            self.daily_message = "Demand has plummeted, causing the available stock to rise. "
            for v in range(0, 4):
                self.GameObject.vegetables[self.GameObject.g[v]]["stock"] += self.GameObject.vegetables[self.GameObject.g[v]]["init_stock"]
        elif event_number == 3:
            self.daily_message = "A disaster at the market has ruined all of the stocked produce. "
            self.daily_title = "Complete Stock Shortage!"
            for v in range(0, 4):
                self.GameObject.vegetables[self.GameObject.g[v]]["stock"] = 0
        elif event_number == 4:
            self.daily_title = "1/4 of Vegetables Rot!"
            self.daily_message = "Bad weather has caused about 1/4 of all inventory produce to go bad overnight. "
            for v in range(0, 4):
                self.GameObject.vegetables[self.GameObject.g[v]]["count"] = round(0.75 * self.GameObject.vegetables[self.GameObject.g[v]]["count"])
        elif event_number == 5:
            rotten_vegetable = randint(0, 3)
            self.daily_title = "1/2 of " + self.GameObject.vegetables[self.GameObject.g[rotten_vegetable]]["name"] + " Rotten!"
            self.daily_message = "Infestations have caused 1/2 of all of this inventoried vegetable to go bad. "
            for v in range(0, 4):
                self.GameObject.vegetables[self.GameObject.g[v]]["count"] = round(0.5 * self.GameObject.vegetables[self.GameObject.g[v]]["count"])
        elif event_number == 6:
            self.daily_title = "Prices at Record Highs!"
            self.daily_message = "Hyper-inflation has caused market prices to skyrocket. "

        elif event_number == 7:
            self.daily_title = "Prices at Record Lows!"
            self.daily_message = "Economic depression has caused market prices to plummet. "

        elif event_number == 8:
            self.daily_title = "Balances Cut in Half!"
            self.daily_message = "Economic recession has caused all savings to be slashed by 50%. "
            self.GameObject.balance *= 0.5
        elif event_number == 9:
            self.daily_title = "Everyone Taxed at 25%!"
            self.daily_message = "New taxes cause all balances to be reduced by 25%. "
            self.GameObject.balance *= 0.75

        self.daily_message += "Vegetables available now: " + self.GameObject.vegetables[self.GameObject.g1][
            "name"] + ": $" + make_dollars(
            self.GameObject.vegetables[self.GameObject.g1]["cost"] * self.GameObject.prices[0][self.GameObject.day + 1]) + ", with " + str(
            self.GameObject.vegetables[self.GameObject.g1]["stock"]) + " in stock. " + \
                              self.GameObject.vegetables[self.GameObject.g2][
                                  "name"] + ": $" + make_dollars(
            self.GameObject.vegetables[self.GameObject.g2]["cost"] * self.GameObject.prices[1][self.GameObject.day + 1]) + ", with " + str(
            self.GameObject.vegetables[self.GameObject.g2]["stock"]) + " in stock. " + self.GameObject.vegetables[self.GameObject.g3][
                                  "name"] + ": $" + make_dollars(
            self.GameObject.vegetables[self.GameObject.g3]["cost"] * self.GameObject.prices[2][self.GameObject.day + 1]) + ", with " + str(
            self.GameObject.vegetables[self.GameObject.g3]["stock"]) + " in stock. " + \
                              self.GameObject.vegetables[self.GameObject.g4][
                                  "name"] + ": $" + make_dollars(
            self.GameObject.vegetables[self.GameObject.g4]["cost"] * self.GameObject.prices[3][self.GameObject.day + 1]) + ", with " + str(
            self.GameObject.vegetables[self.GameObject.g4]["stock"]) + " in stock. " + "High demand this season! " + "Here for " + str(
            self.GameObject.day_limit - self.GameObject.day) + " more days!"

    def next_night(self):
        self.news = True
        self.leaderboard = True
        self.market = False
        self.exchange = False
        self.night = self.GameObject.day + 1
        self.GameObject.next_night()
        self.execute_event(self.GameObject.dayevent[self.GameObject.day])


    def run_menu(self):
        pygame.time.delay(3)
        self.check_mouse_hover()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_choose()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_UP]:
            self.next_item(-1)
        if keys[pygame.K_RIGHT] or keys[pygame.K_DOWN]:
            self.next_item(1)
        if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
            self.keyboard_choose()
        self.window.fill(self.background_color)
        if self.RGB >= 38:
            self.RGB_increment *= -1
        elif self.RGB <= 2:
            self.RGB_increment *= -1
        self.RGB += self.RGB_increment
        pygame.draw.rect(self.window, (0, 0, 0), (self.WIDTH * 0, self.HEIGHT * 0, self.WIDTH, 245))
        pygame.draw.rect(self.window, self.sky_blue, (self.WIDTH * 0, self.HEIGHT * 0, self.WIDTH, 240))
        pygame.draw.rect(self.window, (0, 0, 0), (self.WIDTH * 0, self.HEIGHT - 6, self.WIDTH, 10))
        self.window.blit(self.title_background, (self.X, 0))
        self.window.blit(self.title_background, (self.X - 1080, 0))
        self.window.blit(self.title_background, (self.X + 1080, 0))
        self.window.blit(self.title, (0, self.Y))
        self.X += 0.55
        if self.X > 1080:
            self.X = 0
        if self.Y > 10 or self.Y < -10:
            self.Y_increment *= -1
        self.Y += self.Y_increment
        if self.menu_gui["hover"] == 1:
            pygame.draw.rect(self.window, self.box_filled_color_title,
                             (self.WIDTH * 0.25, self.HEIGHT * 0.39, self.WIDTH * 0.5, self.HEIGHT * 0.1))
        else:
            pygame.draw.rect(self.window, self.green_title,
                             (self.WIDTH * 0.25, self.HEIGHT * 0.39, self.WIDTH * 0.5, self.HEIGHT * 0.1))
        pygame.draw.rect(self.window, (0, 0, 0),
                         (self.WIDTH * 0.25, self.HEIGHT * 0.39, self.WIDTH * 0.5, self.HEIGHT * 0.1), 3)
        if self.menu_gui["hover"] == 2:
            pygame.draw.rect(self.window, self.box_filled_color_title,
                             (self.WIDTH * 0.25, self.HEIGHT * 0.54, self.WIDTH * 0.5, self.HEIGHT * 0.1))
        else:
            pygame.draw.rect(self.window, self.green_title,
                             (self.WIDTH * 0.25, self.HEIGHT * 0.54, self.WIDTH * 0.5, self.HEIGHT * 0.1))
        pygame.draw.rect(self.window, (0, 0, 0),
                         (self.WIDTH * 0.25, self.HEIGHT * 0.54, self.WIDTH * 0.5, self.HEIGHT * 0.1), 3)
        if self.menu_gui["hover"] == 3:
            pygame.draw.rect(self.window, self.box_filled_color_title,
                             (self.WIDTH * 0.25, self.HEIGHT * 0.69, self.WIDTH * 0.5, self.HEIGHT * 0.1))
        else:
            pygame.draw.rect(self.window, self.green_title,
                             (self.WIDTH * 0.25, self.HEIGHT * 0.69, self.WIDTH * 0.5, self.HEIGHT * 0.1))
        pygame.draw.rect(self.window, (0, 0, 0),
                         (self.WIDTH * 0.25, self.HEIGHT * 0.69, self.WIDTH * 0.5, self.HEIGHT * 0.1), 3)
        if self.menu_gui["main"] == 0:
            self.make_text("Play", self.font2, self.black, self.WIDTH * 0.5, self.HEIGHT * 0.44 + 5)
            self.make_text("Settings", self.font2, self.black, self.WIDTH * 0.5, self.HEIGHT * 0.59 + 5)
            self.make_text("Credits", self.font2, self.black, self.WIDTH * 0.5, self.HEIGHT * 0.74 + 5)
            if self.menu_gui["hover"] == 4:
                pygame.draw.rect(self.window, self.box_filled_color_title,
                                 (self.WIDTH * 0.25, self.HEIGHT * 0.84, self.WIDTH * 0.5, self.HEIGHT * 0.1))
            else:
                pygame.draw.rect(self.window, self.green_title,
                                 (self.WIDTH * 0.25, self.HEIGHT * 0.84, self.WIDTH * 0.5, self.HEIGHT * 0.1))
            self.make_text("Quit", self.font2, self.black, self.WIDTH * 0.5, self.HEIGHT * 0.89 + 5)
            pygame.draw.rect(self.window, (0, 0, 0),
                             (self.WIDTH * 0.25, self.HEIGHT * 0.84, self.WIDTH * 0.5, self.HEIGHT * 0.1), 3)
        elif self.menu_gui["main"] == 1:
            self.make_text("Single-player", self.font2, self.black, self.WIDTH * 0.5, self.HEIGHT * 0.44 + 5)
            self.make_text("Multi-player", self.font2, self.black, self.WIDTH * 0.5, self.HEIGHT * 0.59 + 5)
            self.make_text("Back", self.font2, self.black, self.WIDTH * 0.5, self.HEIGHT * 0.74 + 5)
        pygame.display.update()
        # self.HEIGHT = window.get_height()
        # self.WIDTH = window.get_self.WIDTH()

    def run_loading(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
        self.window.fill(self.box_filled_color_title)
        self.make_text("Loading...", self.font5, self.white, self.WIDTH * 0.5, self.HEIGHT * 0.4)
        pygame.draw.rect(self.window, self.white,
                         (self.WIDTH * 0.3, self.HEIGHT * 0.45, self.WIDTH * 0.4, self.HEIGHT * 0.1), 5)
        for bars in range(self.loading_X):
            pygame.draw.rect(self.window, self.green,
                             (self.WIDTH * 0.3 + bars * 10 + 3, self.HEIGHT * 0.45 + 3, 6, self.HEIGHT * 0.1 - 6))
        pygame.display.update()
        pygame.time.delay(35)

        self.loading_X += 1

        if self.loading_X >= (self.WIDTH * 0.4 - 6)/10:
            self.loading = False

    def load(self, mp):
        pygame.mixer_music.stop()
        self.loading = True
        self.GameObject = GameInstance(multiplayer=mp)
        pygame.mixer_music.load("music/guitar_music.mp3")
        pygame.mixer.music.play(-1)
        self.chatbox = False
        self.settings = False
        pygame.time.set_timer(pygame.USEREVENT + 2, 1000)
        self.next_night()

    def run_game(self):
        self.Clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.MOUSEMOTION:
                (self.x, self.y) = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # settings button
                if 0.01 * self.WIDTH <= self.x <= 0.17 * self.WIDTH and 0.925 * self.HEIGHT <= self.y <= 0.99 * self.HEIGHT:
                    self.settings = True
                    self.news = False
                    self.market = False
                    self.exchange = False
                    self.chatbox = False
                    self.chat_gui = False
                    self.leaderboard = False
                    self.chatbox_msg = "Enter message"
                # news button
                elif 0.2 * self.WIDTH <= self.x <= 0.36 * self.WIDTH and 0.925 * self.HEIGHT <= self.y <= 0.99 * self.HEIGHT:
                    self.settings = False
                    self.news = True
                    self.market = False
                    self.exchange = False
                    self.chatbox = False
                    self.leaderboard = True
                # market button
                elif 0.39 * self.WIDTH <= self.x <= 0.55 * self.WIDTH and 0.925 * self.HEIGHT <= self.y <= 0.99 * self.HEIGHT:
                    self.settings = False
                    self.exchange = False
                    self.news = False
                    self.market = True
                    self.chat_gui = False
                    self.leaderboard = False
                    self.chatbox = False
                    self.chatbox_msg = "Enter message"
                    self.quantitybox_txt = "Custom"
                    self.quantitybox = False
                    self.quantity = 1
                # exchange button
                elif 0.58 * self.WIDTH <= self.x <= 0.74 * self.WIDTH and 0.925 * self.HEIGHT <= self.y <= 0.99 * self.HEIGHT:
                    self.settings = False
                    self.market = False
                    self.news = False
                    self.exchange = True
                    self.chatbox = False
                    self.leaderboard = True
                # market veg buttons (inventory_position - 60, -40 + 0.25 * self.HEIGHT + 31, 50, 50)
                elif self.inventory_position - 60 <= self.x <= self.inventory_position - 10 and 171 <= self.y <= 221:
                    self.market_selection = 1
                elif self.inventory_position - 60 <= self.x <= self.inventory_position - 10 and 171 + 60 <= self.y <= 221 + 60:
                    self.market_selection = 2
                elif self.inventory_position - 60 <= self.x <= self.inventory_position - 10 and 171 + 120 <= self.y <= 221 + 120:
                    self.market_selection = 3
                elif self.inventory_position - 60 <= self.x <= self.inventory_position - 10 and 171 + 180 <= self.y <= 221 + 180:
                    self.market_selection = 4
                # quantity buttons (820 + 44, 430, 45, 45)
                elif self.market and 815 <= self.x <= 860 and 410 <= self.y <= 455:
                    self.quantity = 1
                    self.quantitybox = False
                    self.quantitybox_txt = "Custom"
                elif self.market and 864 <= self.x <= 864 + 45 and 410 <= self.y <= 455:
                    self.quantitybox = False
                    self.quantitybox_txt = "Custom"
                    self.quantity = 5
                elif self.market and 903 <= self.x <= 948 and 410 <= self.y <= 455:
                    self.quantitybox = False
                    self.quantitybox_txt = "Custom"
                    self.quantity = 10
                elif self.market and 815 <= self.x <= 948 and 455 <= self.y <= 500:
                    self.quantitybox = True
                    self.quantitybox_txt = ""
                # buy button
                elif self.market and 680 <= self.x <= 790 and 390 <= self.y <= 390 + self.HEIGHT * 0.06 + 2 and not self.GameObject.nighttime:
                    inv_item = self.GameObject.g[self.market_selection - 1]
                    item_cost = self.GameObject.vegetables[inv_item]["cost"] * self.GameObject.prices[self.market_selection - 1][self.GameObject.day]
                    if self.GameObject.balance >= item_cost * self.quantity and self.GameObject.vegetables[self.GameObject.g[self.market_selection - 1]][
                        "stock"] >= self.quantity:
                        self.GameObject.vegetables[self.GameObject.g[self.market_selection - 1]]["stock"] -= self.quantity
                        self.GameObject.vegetables[inv_item]["count"] += self.quantity
                        self.GameObject.balance -= item_cost * self.quantity
                    else:
                        tempquantity = self.quantity
                        if tempquantity >= self.GameObject.vegetables[self.GameObject.g[self.market_selection - 1]]["stock"]:
                            tempquantity = self.GameObject.vegetables[self.GameObject.g[self.market_selection - 1]]["stock"]
                        if item_cost * tempquantity >= self.GameObject.balance:
                            tempquantity = int(self.GameObject.balance / item_cost)
                        self.GameObject.vegetables[self.GameObject.g[self.market_selection - 1]]["stock"] -= tempquantity
                        self.GameObject.vegetables[inv_item]["count"] += tempquantity
                        self.GameObject.balance -= item_cost * tempquantity

                # sell button
                elif self.market and 680 <= self.x <= 790 and 470 <= self.y <= 470 + self.HEIGHT * 0.06 + 2 and not self.GameObject.nighttime:
                    inv_item = self.GameObject.g[self.market_selection - 1]
                    item_cost = self.GameObject.vegetables[inv_item]["cost"] * self.GameObject.prices[self.market_selection - 1][self.GameObject.day]
                    if self.GameObject.vegetables[inv_item]["count"] >= self.quantity:
                        self.GameObject.vegetables[inv_item]["count"] -= self.quantity
                        self.GameObject.vegetables[self.GameObject.g[self.market_selection - 1]]["stock"] += self.quantity
                        self.GameObject.balance += item_cost * self.quantity
                    else:
                        amt = self.GameObject.vegetables[inv_item]["count"]
                        self.GameObject.vegetables[inv_item]["count"] -= amt
                        self.GameObject.vegetables[self.GameObject.g[self.market_selection - 1]]["stock"] += amt
                        self.GameObject.balance += item_cost * amt
                # chatbox chat box selection
                elif 830 <= self.x <= 1055 and 660 <= self.y <= 715:
                    self.market = False
                    self.chat_gui = True
                    self.chatbox = True
                    self.chatbox_msg = ""
                # close market or exchange or news (0.2 * self.WIDTH, 90, self.WIDTH * 0.7, 500)
                elif self.market and (
                        (
                                0 <= self.x <= self.inventory_position + 100 or 0.2 * self.WIDTH <= self.x <= 0.9 * self.WIDTH) and 90 <= self.y <= 590):
                    self.leaderboard = False
                    self.chatbox = False
                # close news if not in the box
                elif self.news and (
                        (
                                0 <= self.x <= self.inventory_position + 100 or 0.2 * self.WIDTH <= self.x <= 0.7 * self.WIDTH) and 90 <= self.y <= 590):
                    pass
                elif self.exchange and (
                        (
                                0 <= self.x <= self.inventory_position + 100 or 0.2 * self.WIDTH <= self.x <= 0.75 * self.WIDTH) and 90 <= self.y <= 590):
                    pass
                # chat corner
                elif 820 <= self.x and 350 <= self.y:
                    self.market = False
                    self.chatbox = False
                    self.chat_gui = True
                # everywhere else
                else:
                    self.market = False
                    self.exchange = False
                    self.leaderboard = False
                    self.chatbox = False
                    self.news = False
                    self.chat_gui = False
            elif event.type == pygame.KEYDOWN:
                if self.chatbox:
                    keys = pygame.key.get_pressed()
                    self.chat_gui = True
                    pygame.key.start_text_input()
                    pygame.key.set_text_input_rect(pygame.Rect(800, 660, 260, 55))
                    if keys[pygame.K_ESCAPE]:
                        pygame.key.stop_text_input()
                        self.chatbox = False
                    if keys[pygame.K_BACKSPACE]:
                        self.chatbox_msg = self.chatbox_msg[:-1]
                    if event.unicode in self.valid_chars:
                        self.chatbox_msg += event.unicode
                    if keys[pygame.K_RETURN] and len(self.chatbox_msg) > 0:
                        self.send_message(self.chatbox_msg)
                        self.chatbox_msg = ""
                elif self.quantitybox:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_BACKSPACE]:
                        if len(self.quantitybox_txt) > 0:
                            self.quantitybox_txt = self.quantitybox_txt[:-1]
                        try:
                            self.quantity = int(self.quantitybox_txt)
                        except ValueError:
                            self.quantity = 0
                    if event.unicode in self.valid_nums:
                        if len(self.quantitybox_txt) < 7:
                            self.quantitybox_txt += event.unicode
                        try:
                            self.quantity = int(self.quantitybox_txt)
                        except ValueError:
                            self.quantity = 1
                    if keys[pygame.K_ESCAPE] or keys[pygame.K_RETURN]:
                        self.quantitybox = False

            if event.type == pygame.USEREVENT + 2:
                self.GameObject.update_constant()
                if self.GameObject.time <= 0:
                    if self.GameObject.nighttime:
                        if not self.GameObject.next_day():
                            self.run = False
                    else:
                        self.next_night()
        else:
            pygame.key.stop_text_input()
        (self.x, self.y) = pygame.mouse.get_pos()
        if (
                0 <= self.x <= self.WIDTH * 0.23 and self.HEIGHT * 0.1 <= self.y <= self.HEIGHT * 0.9 or self.market or self.exchange) and not self.settings:
            self.inventory_open = True
        else:
            self.inventory_open = False
        if self.inventory_open:
            if self.inventory_percentage < 1:
                self.inventory_percentage += 0.12
        else:
            if self.inventory_percentage > 0:
                self.inventory_percentage -= 0.12
        # background
        self.window.fill(self.sky_blue)
        pygame.time.delay(50)
        if self.GameObject.nighttime:
            self.window.blit(self.nightclouds, (self.cloud_x, 0))
            self.window.blit(self.nightclouds, (self.cloud_x - 4000, 0))
            self.window.blit(self.night_background, (0, 0))
        else:
            self.window.blit(self.clouds, (self.cloud_x, 0))
            self.window.blit(self.clouds, (self.cloud_x - 4000, 0))
            self.window.blit(self.game_background, (0, 0))
        self.cloud_x += 3
        if self.cloud_x > 4000:
            self.cloud_x = 0
        # top bar
        pygame.draw.rect(self.window, self.green, (0, 0, self.WIDTH, self.HEIGHT * 0.09 + 5))
        # day display
        AAfilledRoundedRect(self.window, self.background_filled_color,
                            (self.WIDTH * 0.01, self.HEIGHT * 0.02, self.WIDTH * 0.12, self.HEIGHT * 0.06))
        if self.GameObject.day > 0 and not self.GameObject.nighttime:
            self.make_text("Day " + str(self.GameObject.day), self.font5, self.brown, 0.07 * self.WIDTH, 0.05 * self.HEIGHT + 2)
        else:
            self.make_text("Night", self.font5, self.brown, 0.07 * self.WIDTH, 0.05 * self.HEIGHT + 2)
        # seconds display
        AAfilledRoundedRect(self.window, self.background_filled_color,
                            (self.WIDTH * 0.15, self.HEIGHT * 0.02, self.WIDTH * 0.26, self.HEIGHT * 0.06))
        if self.GameObject.nighttime:
            self.make_text(str(self.GameObject.time) + " secs intermission", self.font5, self.brown, 0.28 * self.WIDTH,
                           0.05 * self.HEIGHT + 2)
        else:
            self.make_text(str(self.GameObject.time) + " secs left in day", self.font5, self.brown, 0.28 * self.WIDTH,
                           0.05 * self.HEIGHT + 2)
        # balance display
        AAfilledRoundedRect(self.window, self.background_filled_color,
                            (self.WIDTH * 0.72, self.HEIGHT * 0.02, self.WIDTH * 0.27, self.HEIGHT * 0.06))
        self.make_text("Balance: $" + make_dollars(round(self.GameObject.balance, 2)), self.font5, self.brown,
                       0.855 * self.WIDTH,
                       0.05 * self.HEIGHT + 2)
        # FPS / PING
        AAfilledRoundedRect(self.window, self.background_filled_color,
                            (self.WIDTH * 0.44, self.HEIGHT * 0.02, self.WIDTH * 0.25, self.HEIGHT * 0.06))
        self.make_text(str(round(self.Clock.get_fps(), 1)) + " FPS    30 ms", self.font5, self.brown,
                       0.565 * self.WIDTH,
                       0.05 * self.HEIGHT + 2)
        # bottom bar
        pygame.draw.rect(self.window, self.green, (0, self.HEIGHT * 0.91 - 5, self.WIDTH, self.HEIGHT * 0.1 + 5))
        # inventory box (0.2 * self.WIDTH, 90, self.WIDTH * 0.5, 500)
        # inventory_percentage * (self.WIDTH * 0.13) + self.WIDTH * 0.08
        self.inventory_position = -60 + self.inventory_percentage * 150
        AAfilledRoundedRect(self.window, self.green, (self.inventory_position - 100, 90, 200, 500), 0.23)
        # inventory text
        # font5.set_underline(True)
        self.make_text("Inventory", self.font5, self.brown, self.inventory_position, 120)
        pygame.draw.line(self.window, self.brown, (self.inventory_position - 65, 120 + self.title_height),
                         (self.inventory_position + 65, 120 + self.title_height), 2)
        # font5.set_underline(False)
        if self.market_selection == 1:
            AAfilledRoundedRect(self.window, self.bright_green,
                                (self.inventory_position - 70, -40 + 0.25 * self.HEIGHT + 31, 50, 50))
        self.window.blit(self.e[self.GameObject.g1], (self.inventory_position - 70, -40 + 0.25 * self.HEIGHT + 31))
        self.make_text("X", self.font5, self.brown, self.inventory_position + 15, -40 + 0.25 * self.HEIGHT + 60)
        self.make_text(str(self.GameObject.vegetables[self.GameObject.g1]["count"]), self.font5, self.brown, self.inventory_position + 60,
                       -40 + 0.25 * self.HEIGHT + 60)
        if self.market_selection == 2:
            AAfilledRoundedRect(self.window, self.bright_green,
                                (self.inventory_position - 70, -40 + 0.25 * self.HEIGHT + 91, 50, 50))
        self.window.blit(self.e[self.GameObject.g2], (self.inventory_position - 70, -40 + 0.25 * self.HEIGHT + 91))
        self.make_text("X", self.font5, self.brown, self.inventory_position + 15, -40 + 0.25 * self.HEIGHT + 120)
        self.make_text(str(self.GameObject.vegetables[self.GameObject.g2]["count"]), self.font5, self.brown, self.inventory_position + 60,
                       -40 + 0.25 * self.HEIGHT + 120)
        if self.market_selection == 3:
            AAfilledRoundedRect(self.window, self.bright_green,
                                (self.inventory_position - 70, -40 + 0.25 * self.HEIGHT + 151, 50, 50))
        self.window.blit(self.e[self.GameObject.g3], (self.inventory_position - 70, -40 + 0.25 * self.HEIGHT + 151))
        self.make_text("X", self.font5, self.brown, self.inventory_position + 15, -40 + 0.25 * self.HEIGHT + 180)
        self.make_text(str(self.GameObject.vegetables[self.GameObject.g3]["count"]), self.font5, self.brown, self.inventory_position + 60,
                       -40 + 0.25 * self.HEIGHT + 180)
        if self.market_selection == 4:
            AAfilledRoundedRect(self.window, self.bright_green,
                                (self.inventory_position - 70, -40 + 0.25 * self.HEIGHT + 211, 50, 50))
        self.window.blit(self.e[self.GameObject.g4], (self.inventory_position - 70, -40 + 0.25 * self.HEIGHT + 211))
        self.make_text("X", self.font5, self.brown, self.inventory_position + 15, -40 + 0.25 * self.HEIGHT + 240)
        self.make_text(str(self.GameObject.vegetables[self.GameObject.g4]["count"]), self.font5, self.brown, self.inventory_position + 60,
                       -40 + 0.25 * self.HEIGHT + 240)
        # font5.set_underline(True)
        self.make_text("Prediction", self.font5, self.brown, self.inventory_position, 450)
        pygame.draw.line(self.window, self.brown, (self.inventory_position - 70, 450 + self.title_height),
                         (self.inventory_position + 70, 450 + self.title_height), 2)
        # font5.set_underline(False)
        # AAfilledRoundedRect(window, bright_green, (inventory_position - 70, 500, 50, 50))
        if self.GameObject.day >= 1:
            self.window.blit(self.e[self.GameObject.g[self.GameObject.players[self.GameObject.playerid]["rank"]]], (self.inventory_position - 70, 500))
        # prediction icon

        self.make_text(self.prediction_text, self.font5, self.brown, self.inventory_position + 42, 528)
        # leaderboard gui
        if self.leaderboard:
            AAfilledRoundedRect(self.window, self.green, (825, 90, 245, 230), 0.2)
            # AAfilledRoundedRect(window, green, (795, 95, 270, 290), 0.2)
            # font5.set_underline(True)
            self.make_text("Leaderboard", self.font5, self.brown, 950, 120)  # 940
            pygame.draw.line(self.window, self.brown, (950 - 95, 120 + self.title_height),
                             (950 + 95, 120 + self.title_height), 2)

            for player in self.GameObject.players:
                self.make_text(
                    str(player["rank"]) + ". " + player["name"] + ": $" + make_dollars(player["net_worth"]),
                    self.font3,
                    self.brown, 950, 125 + 40 * player["rank"])

        # chat gui
        if self.chat_gui:
            AAfilledRoundedRect(self.window, self.green, (825, 350, 245, 420), 0.3)
            # AAfilledRoundedRect(window, green, (795, 405, 270, 320), 0.2)
            self.make_text("Chat", self.font5, self.brown, 950, 380)
            pygame.draw.line(self.window, self.brown, (915, 380 + self.title_height), (985, 380 + self.title_height), 2)
            msglim = len(self.GameObject.chat) - 1
            msgnum = msglim
            msg_y = 405
            while msg_y <= 825 and msgnum >= 0:
                msg_y = self.blit_text(235, 405, self.GameObject.chat[msgnum][0] + ": " + self.GameObject.chat[msgnum][1], (835, msg_y),
                                       self.font3,
                                       self.brown, 2)
                msgnum -= 1
                msg_y += 5
        #            window.blit(font3.render(chat[msgnum][0] + ": " + line, True, brown), (835, 635 - 30 * i))

        # font5.set_underline(False)
        # chat text box
        pygame.draw.rect(self.window, self.green, (825, 655, 245, 70))
        if 830 <= self.x <= 1055 and 660 <= self.y <= 715 or self.chatbox:
            AAfilledRoundedRect(self.window, self.beige, (830, 660, 235, 55), 0.2)
        else:
            AAfilledRoundedRect(self.window, self.dark_white, (830, 660, 235, 55), 0.2)
        self.blit_text(225, 50, self.chatbox_msg, (835, 665), self.font3, self.brown)
        # settings button
        if 0.01 * self.WIDTH <= self.x <= 0.17 * self.WIDTH and 0.925 * self.HEIGHT <= self.y <= 0.99 * self.HEIGHT or self.settings:
            AAfilledRoundedRect(self.window, self.background_filled_color,
                                (self.WIDTH * 0.01, self.HEIGHT * 0.925, self.WIDTH * 0.16, self.HEIGHT * 0.06 + 2))
        else:
            AAfilledRoundedRect(self.window, self.bright_green,
                                (self.WIDTH * 0.01, self.HEIGHT * 0.925, self.WIDTH * 0.16, self.HEIGHT * 0.06 + 2))
        self.make_text("Settings", self.font5, self.brown, 0.09 * self.WIDTH, 0.955 * self.HEIGHT + 4)
        # news button
        if 0.2 * self.WIDTH <= self.x <= 0.36 * self.WIDTH and 0.925 * self.HEIGHT <= self.y <= 0.99 * self.HEIGHT or self.news:
            AAfilledRoundedRect(self.window, self.background_filled_color,
                                (self.WIDTH * 0.2, self.HEIGHT * 0.925, self.WIDTH * 0.16, self.HEIGHT * 0.06 + 2))
        else:
            AAfilledRoundedRect(self.window, self.bright_green,
                                (self.WIDTH * 0.2, self.HEIGHT * 0.925, self.WIDTH * 0.16, self.HEIGHT * 0.06 + 2))
        self.make_text("News", self.font5, self.brown, 0.28 * self.WIDTH, 0.955 * self.HEIGHT + 4)
        # market button
        if 0.39 * self.WIDTH <= self.x <= 0.55 * self.WIDTH and 0.925 * self.HEIGHT <= self.y <= 0.99 * self.HEIGHT or self.market:
            AAfilledRoundedRect(self.window, self.background_filled_color,
                                (self.WIDTH * 0.39, self.HEIGHT * 0.925, self.WIDTH * 0.16, self.HEIGHT * 0.06 + 2))
        else:
            AAfilledRoundedRect(self.window, self.bright_green,
                                (self.WIDTH * 0.39, self.HEIGHT * 0.925, self.WIDTH * 0.16, self.HEIGHT * 0.06 + 2))
        self.make_text("Market", self.font5, self.brown, 0.47 * self.WIDTH, 0.955 * self.HEIGHT + 4)
        # exchange button EXB
        if 0.58 * self.WIDTH <= self.x <= 0.74 * self.WIDTH and 0.925 * self.HEIGHT <= self.y <= 0.99 * self.HEIGHT or self.exchange:
            AAfilledRoundedRect(self.window, self.background_filled_color,
                                (self.WIDTH * 0.58, self.HEIGHT * 0.925, self.WIDTH * 0.16, self.HEIGHT * 0.06 + 2))
        else:
            AAfilledRoundedRect(self.window, self.bright_green,
                                (self.WIDTH * 0.58, self.HEIGHT * 0.925, self.WIDTH * 0.16, self.HEIGHT * 0.06 + 2))
        self.make_text("Exchange", self.font5, self.brown, 0.66 * self.WIDTH, 0.955 * self.HEIGHT + 4)
        # news menu
        if self.news:
            # box
            pygame.draw.rect(self.window, self.beige, (0.2 * self.WIDTH, 90, self.WIDTH * 0.5, 500))
            pygame.draw.rect(self.window, self.beige2, (0.2 * self.WIDTH, 90, self.WIDTH * 0.5, 500), 3)
            # header
            self.make_text("The Farmer Times", self.newspaperfont, self.beige3, 0.45 * self.WIDTH, 130)
            self.make_text("Daily News - Day " + str(self.night) + " Edition", self.newspaperfont2, self.beige3,
                           0.45 * self.WIDTH, 170)
            pygame.draw.line(self.window, self.beige2, (0.2 * self.WIDTH, 200), (0.7 * self.WIDTH, 200), 10)
            pygame.draw.line(self.window, self.beige2, (0.3 * self.WIDTH, 200), (0.3 * self.WIDTH, 590), 5)
            pygame.draw.line(self.window, self.beige2, (0.6 * self.WIDTH, 200), (0.6 * self.WIDTH, 590), 5)
            pygame.draw.rect(self.window, self.beige3, (0.3 * self.WIDTH + 12, 215, 0.3 * self.WIDTH - 24, 60))
            self.make_text(self.daily_title, self.newspaperfont2, self.beige3, 0.45 * self.WIDTH, 295)
            self.blit_text(0.3 * self.WIDTH - 20, 275, self.daily_message, (0.3 * self.WIDTH + 10, 315), self.font3,
                           self.beige3, 5)
        # market menu
        elif self.market:
            # box
            AAfilledRoundedRect(self.window, self.green, (0.2 * self.WIDTH, 90, self.WIDTH * 0.7, 500), 0.1)
            # graph
            pygame.draw.rect(self.window, self.dark_white, (0.2 * self.WIDTH + 30, 125, 400, 400))
            for i in range(13):
                pygame.draw.line(self.window, self.beige, (0.2 * self.WIDTH + 60 + 29 * i, 125),
                                 (0.2 * self.WIDTH + 60 + 29 * i, 525))
            # pygame.draw.line(window, beige, (0.2 * self.WIDTH + 35, 125), (0.2 * self.WIDTH + 425, 125))
            for i in range(13):
                pygame.draw.line(self.window, self.beige, (0.2 * self.WIDTH + 30, 152 + 29 * i),
                                 (0.2 * self.WIDTH + 430, 152 + 29 * i))
            self.make_text("Day", self.font3, self.brown, 46 + 0.2 * self.WIDTH, 516)
            if self.GameObject.day < 13:
                pygame.draw.line(self.window, self.brown, (0.2 * self.WIDTH + 30, 383), (0.2 * self.WIDTH + 59, 383), 2)
                ii = 0
                graphdays = self.GameObject.day
            else:
                ii = self.GameObject.day - 12
                graphdays = 12
                pygame.draw.line(self.window, self.brown,
                                 (0.2 * self.WIDTH + 30,
                                  516 - 133 * self.GameObject.prices[self.market_selection - 1][self.GameObject.day - 13]),
                                 (0.2 * self.WIDTH + 59,
                                  516 - 133 * self.GameObject.prices[self.market_selection - 1][self.GameObject.day - 12]),
                                 2)
            for i in range(graphdays):
                pygame.draw.line(self.window, self.brown,
                                 (
                                     0.2 * self.WIDTH + 59 + 29 * i,
                                     516 - 133 * self.GameObject.prices[self.market_selection - 1][i + ii]),
                                 (0.2 * self.WIDTH + 89 + 29 * i,
                                  516 - 133 * self.GameObject.prices[self.market_selection - 1][i + ii + 1]),
                                 2)
                self.make_text(str(i + ii + 1), self.font3, self.brown, 83 + 0.2 * self.WIDTH + 28 * i, 516)

            # price display
            # AAfilledRoundedRect(window, dark_white, (240, 520, 155, self.HEIGHT * 0.06 + 2))
            self.make_text(str(self.GameObject.vegetables[self.GameObject.g[self.market_selection - 1]]["name"]), self.font5, self.brown, 807,
                           150)
            self.make_text("Price:", self.font5, self.brown, 725, 215)
            self.make_text("$" + make_dollars(
                round(self.GameObject.prices[self.market_selection - 1][self.GameObject.day] *
                      self.GameObject.vegetables[self.GameObject.g[self.market_selection - 1]]["cost"], 2)),
                           self.font5,
                           self.brown,
                           725, 255)
            self.make_text("Change:", self.font5, self.brown, 860, 215)
            if self.GameObject.day > 0:
                change = round(
                    100 * (-1 + self.GameObject.prices[self.market_selection - 1][self.GameObject.day] /
                           self.GameObject.prices[self.market_selection - 1][self.GameObject.day - 1]),
                    1)
            else:
                change = 0
            if change > 0:
                self.make_text("+" + str(change) + "%", self.font5, self.brown, 860, 255)
            else:
                self.make_text(str(change) + "%", self.font5, self.brown, 860, 255)
            # stock display
            self.make_text("Stock:", self.font5, self.brown, 725, 315)
            self.make_text(str(self.GameObject.vegetables[self.GameObject.g[self.market_selection - 1]]["stock"]), self.font5, self.brown,
                           725, 355)
            self.make_text("Owned:", self.font5, self.brown, 860, 315)
            self.make_text(str(self.GameObject.vegetables[self.GameObject.g[self.market_selection - 1]]["count"]), self.font5, self.brown,
                           860, 355)
            # buy button
            if 670 <= self.x <= 780 and 390 <= self.y <= 390 + self.HEIGHT * 0.06 + 2:
                AAfilledRoundedRect(self.window, self.background_filled_color, (670, 390, 110, self.HEIGHT * 0.06 + 2))
            else:
                AAfilledRoundedRect(self.window, self.bright_green, (670, 390, 110, self.HEIGHT * 0.06 + 2))
            self.make_text("Buy", self.font5, self.brown, 725, 415)
            # sell button
            if 670 <= self.x <= 780 and 470 <= self.y <= 470 + self.HEIGHT * 0.06 + 2:
                AAfilledRoundedRect(self.window, self.background_filled_color, (670, 470, 110, self.HEIGHT * 0.06 + 2))
            else:
                AAfilledRoundedRect(self.window, self.bright_green, (670, 470, 110, self.HEIGHT * 0.06 + 2))
            self.make_text("Sell", self.font5, self.brown, 725, 495)

            self.make_text("X", self.font5, self.brown, 795, 455)
            if self.quantitybox:
                AAfilledRoundedRect(self.window, self.bright_green, (815, 455, 138, 45))
            elif self.quantity == 1:
                AAfilledRoundedRect(self.window, self.bright_green, (820 - 5, 410, 45, 45), 0.3)
            # else:
            #    AAfilledRoundedRect(window, bright_green, (820 - 5, 430, 45, 45), 0.3)
            elif self.quantity == 5:
                AAfilledRoundedRect(self.window, self.bright_green, (820 + 44, 410, 45, 45), 0.3)
            # else:
            #    AAfilledRoundedRect(window, bright_green, (820 + 44, 430, 45, 45), 0.3)
            elif self.quantity == 10:
                AAfilledRoundedRect(self.window, self.bright_green, (820 + 93, 410, 45, 45), 0.3)
            else:
                #    AAfilledRoundedRect(window, bright_green, (820 + 93, 430, 45, 45), 0.3)
                AAfilledRoundedRect(self.window, self.bright_green, (815, 455, 138, 45))
            self.make_text("1", self.font5, self.brown, 815 + 22, 435)
            self.make_text("5", self.font5, self.brown, 886, 435)
            self.make_text("10", self.font5, self.brown, 820 + 93 + 22, 435)
            self.make_text(self.quantitybox_txt, self.font5, self.brown, 884, 480)
            # select veg buttons
        # exchange menu EXM
        elif self.exchange:
            self.offer = False
            AAfilledRoundedRect(self.window, self.green, (0.2 * self.WIDTH, 90, self.WIDTH * 0.52, 500), 0.1)
            if self.offer:
                AAfilledRoundedRect(self.window, self.bright_green, (255, 140 - self.title_height*1.5, 100, self.title_height*2.8), 0.3)
                self.make_text("your prediction for:", self.font5, self.brown, 380, 140 + self.title_height * 3)
            else:
                AAfilledRoundedRect(self.window, self.bright_green, (352, 140 - self.title_height*1.5, 136, self.title_height*2.8), 0.3)
                self.make_text("one prediction for:", self.font5, self.brown, 380, 140 + self.title_height * 3)
            self.make_text("Offer", self.font5, self.brown, 305, 140)
            self.make_text("Request", self.font5, self.brown, 420, 140)

        pygame.display.update()


class GameInstance:
    def __init__(self, multiplayer, playerid=1, player1name="Player", player2name="Computer 1", player3name="Computer 2", player4name="Computer 3", settings=None):
        if settings is None:
            settings = []
            self.multiplayer = multiplayer
            self.day_limit = 20
            self.day_timer = 25
            self.night_timer = 15
            self.day = 0
        if not multiplayer:
            self.prices = [[1.0], [1.0], [1.0], [1.0]]
            self.dayevent = []
            for de in range(0, self.day_limit + 1):
                if de > 0 and de % 3 == 0:
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
            g1, g2, g3, g4 = randint(0, 7), randint(0, 7), randint(0, 7), randint(0, 7)
            while g2 == g1 or g2 == g3 or g2 == g4:
                g2 = randint(0, 7)
            while g3 == g1 or g3 == g2 or g3 == g4:
                g3 = randint(0, 7)
            while g4 == g1 or g4 == g2 or g4 == g3:
                g4 = randint(0, 7)
        else:
            # set g values to acquired numbers
            pass
        self.playerid = playerid
        self.g1, self.g2, self.g3, self.g4 = g1, g2, g3, g4
        self.g = [g1, g2, g3, g4]
        self.balance = 100.00
        self.player1 = player1name
        self.player2 = player2name
        self.player3 = player3name
        self.player4 = player4name
        self.time = 60
        self.nighttime = True
        self.chat = [("System", "New messages appear from the top.")]
        self.players = [  # prediction vegetables will be based on g[rank - 1]
            {
                "name": self.player1,
                "net_worth": self.balance,
                "offer": None,
                "rank": 1
            },
            {
                "name": self.player2,
                "net_worth": 100.00,
                "offer": None,
                "rank": 4
            },
            {
                "name": self.player3,
                "net_worth": 100.00,
                "offer": None,
                "rank": 3
            },
            {
                "name": self.player4,
                "net_worth": 100.00,
                "offer": None,
                "rank": 2
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
        self.daily_title = "Farmers Markets Open!"
        self.daily_message = "Placeholder."

    def update_constant(self):
        if not self.multiplayer:
            self.time -= 1

    def update_daily(self):
        if not self.multiplayer:
            self.sort_four()

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
        self.chat.append((self.player1, msg))


farmers_market = ClientInstance()
while farmers_market.run:
    if farmers_market.loading:
        farmers_market.run_loading()
    elif farmers_market.game:
        farmers_market.run_game()
    elif farmers_market.menu:
        farmers_market.run_menu()
pygame.quit()
