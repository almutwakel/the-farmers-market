# old & obsolete version


from random import random

import pygame

pygame.init()

if True:
    last_next_item = 0
    last_keyboard_choose = 0
    title_background = pygame.transform.scale2x(pygame.image.load("images/scrolling_ground2.png"))
    game_background = pygame.image.load("images/farm3.png")
    clouds = pygame.image.load("images/clouds.png")
    title = pygame.image.load("images/title.png")
    pygame.mixer.music.load("music/SlushHike.mp3")
    valid_chars = "`1234567890-= qwertyuiop[]\\asdfghjkl;'zxcvbnm,./" + '~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'
    inventory_open = False
    run_loading = True
    run = True
    run_menu = True
    run_game = False
    chatbox = False
    settings = False
    market = False
    exchange = False
    box_filled_color = (120 - 16, 150, 80 - 16)
    background_filled_color = (120 - 16, 160, 80 - 16)
    sky_blue = (135, 206, 235)
    green = (120, 180, 80)
    white = (253, 245, 232)
    dark_white = (253 - 25, 245 - 25, 232 - 25)
    beige = (198, 198, 178)
    brown = (153, 102, 51)
    light_brown = (204, 153, 0)
    black = (0, 0, 0)
    yellow = (120 - 16, 140, 80 - 16)
    X = 0
    Y = 0
    Y_increment = 0.2
    WIDTH = 1080
    HEIGHT = 720
    RGB = 20
    RGB_increment = 3
    inventory_percentage = 0.3
    cloud_x = 1500
    time = 120
    market_selection = 1
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.font.init()
    font2 = pygame.font.Font("fonts/orange_juice.ttf", 60)
    font3 = pygame.font.SysFont("freesansbold.ttf", 30)
    font1 = pygame.font.SysFont("Arial", 30)
    font4 = pygame.font.SysFont("Segoe UI", 30)
    font5 = pygame.font.Font("fonts/orange_juice.ttf", 35)
    pygame.display.set_caption("The Farmer's Market")
    pygame.mixer.music.play(-1)


# hover = what button to hover over, main = main menu buttons (0 = none, 1 = play, 2 = help, 3 = credits, 4 = quit)
# type = game mode (1 = single-player, 2 = multi-player, 3 = back), exit = when 1 will set all others to 0)
menu_gui = {"hover": 1, "main": 0, "type": 0}


def make_text(text, font, color, center_x, center_y):
    text_surface = font.render(text, True, color)
    text_box = text_surface.get_rect()
    text_box.center = (center_x, center_y)
    window.blit(text_surface, text_box)


def check_mouse_hover(click=False):
    global inventory_open
    x, y = pygame.mouse.get_pos()
    if run_menu:
        if WIDTH * 0.25 <= x <= WIDTH * 0.75 and HEIGHT * 0.39 <= y <= HEIGHT * 0.49:
            menu_gui["hover"] = 1
            if click:
                keyboard_choose()
        elif WIDTH * 0.25 <= x <= WIDTH * 0.75 and HEIGHT * 0.54 <= y <= HEIGHT * 0.64:
            menu_gui["hover"] = 2
            if click:
                keyboard_choose()
        elif WIDTH * 0.25 <= x <= WIDTH * 0.75 and HEIGHT * 0.69 <= y <= HEIGHT * 0.79:
            menu_gui["hover"] = 3
            if click:
                keyboard_choose()
        elif WIDTH * 0.25 <= x <= WIDTH * 0.75 and HEIGHT * 0.84 <= y <= HEIGHT * 0.94 and menu_gui["main"] == 0:
            menu_gui["hover"] = 4
            if click:
                keyboard_choose()


def mouse_choose():
    check_mouse_hover(True)


def next_item(increment):
    global last_next_item
    if pygame.time.get_ticks() > last_next_item + 100:
        # goes to the next item in the gui
        menu_gui["hover"] += increment
        if menu_gui["main"] == 0 and menu_gui["hover"] > 4:
            menu_gui["hover"] = 1
        elif not menu_gui["main"] == 0 and menu_gui["type"] == 0 and menu_gui["hover"] > 3:
            menu_gui["hover"] = 1
        elif menu_gui["hover"] < 1 and menu_gui["main"] == 0:
            menu_gui["hover"] = 4
        elif menu_gui["hover"] < 1 and menu_gui["type"] == 0:
            menu_gui["hover"] = 3
        # elif menu_gui["exit"] == 0 and menu_gui["hover"] > 1:
        #    menu_gui["hover"] = 0
    last_next_item = pygame.time.get_ticks()


def keyboard_choose():
    global run, run_game, run_menu, last_keyboard_choose
    # presses the button that's hovered
    if pygame.time.get_ticks() > last_keyboard_choose + 100:
        if menu_gui["main"] == 0:
            print(menu_gui["hover"])
            if menu_gui["hover"] == 4:
                run = False
            else:
                menu_gui["main"] = menu_gui["hover"]
                menu_gui["hover"] = 1
        elif menu_gui["type"] == 0:
            if menu_gui["hover"] == 3:
                menu_gui["main"] = 0
                menu_gui["hover"] = 1
            elif menu_gui["hover"] == 1 and menu_gui["main"] == 1:
                menu = False
                game = True
            else:
                menu_gui["type"] = menu_gui["hover"]
                menu_gui["hover"] = 1
    last_keyboard_choose = pygame.time.get_ticks()


def send_message(msg):
    pass
# ------------------------------------------------]
# game variables


loading_X = 0
vegetables = [
                {
                     "id": 0,
                     "name": "potatoes",
                     "init_cost": 0.50,
                     "count": 0
                },
                {
                     "id": 1,
                     "name": "carrots",
                     "init_cost": 0.75,
                     "count": 0
                },
                {
                     "id": 2,
                     "name": "apples",
                     "init_cost": 1.00,
                     "count": 0
                },
                {
                     "id": 3,
                     "name": "tomatoes",
                     "init_cost": 2.00,
                     "count": 0
                },
                {
                     "id": 4,
                     "name": "cabbages",
                     "init_cost": 4.00,
                     "count": 0
                },
                {
                     "id": 5,
                     "name": "lettuce",
                     "init_cost": 6.00,
                     "count": 0
                },
                {
                     "id": 6,
                     "name": "pumpkin",
                     "init_cost": 8.00,
                     "count": 0
                },
                {
                     "id": 7,
                     "name": "melon",
                     "init_cost": 10.00,
                     "count": 0
                }
             ]

g1, g2, g3, g4 = 0, 1, 2, 3
balance = 100
day = 0
chat = ["this", "is", "the", "chat"]
chatbox_msg = "Enter message"
prediction_text = "NONE"
pred_veg = 0
days = {}


def generate_prediction():
    global prediction_text, pred_veg
    pred_veg = random.randint(1, 4)
    if day < 10 and days[day + 1]["vegetables"][pred_veg] > days[day]["vegetables"][pred_veg]:
        prediction_text = "UP"
    elif day < 10 and days[day + 1]["vegetables"][pred_veg] < days[day]["vegetables"][pred_veg]:
        prediction_text = "DOWN"
    else:
        prediction_text = "NONE"


while run and run_menu:
    pygame.time.delay(5)

    check_mouse_hover()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_choose()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_UP]:
        next_item(-1)
    if keys[pygame.K_RIGHT] or keys[pygame.K_DOWN]:
        next_item(1)
    if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
        keyboard_choose()
    window.fill(background_filled_color)
    if RGB >= 38:
        RGB_increment *= -1
    elif RGB <= 2:
        RGB_increment *= -1
    RGB += RGB_increment
    pygame.draw.rect(window, (0, 0, 0), (WIDTH * 0, HEIGHT * 0, WIDTH, 245))
    pygame.draw.rect(window, sky_blue, (WIDTH * 0, HEIGHT * 0, WIDTH, 240))
    pygame.draw.rect(window, (0, 0, 0), (WIDTH * 0, HEIGHT - 6, WIDTH, 10))
    window.blit(title_background, (X, 0))
    window.blit(title_background, (X - 1080, 0))
    window.blit(title_background, (X + 1080, 0))
    window.blit(title, (0, Y))
    X += 0.55
    if X > 1080:
        X = 0
    if Y > 10 or Y < -10:
        Y_increment *= -1
    Y += Y_increment
    if menu_gui["hover"] == 1:
        pygame.draw.rect(window, box_filled_color, (WIDTH * 0.25, HEIGHT * 0.39, WIDTH * 0.5, HEIGHT * 0.1))
    else:
        pygame.draw.rect(window, green, (WIDTH * 0.25, HEIGHT * 0.39, WIDTH * 0.5, HEIGHT * 0.1))
    pygame.draw.rect(window, (0, 0, 0), (WIDTH * 0.25, HEIGHT * 0.39, WIDTH * 0.5, HEIGHT * 0.1), 3)
    if menu_gui["hover"] == 2:
        pygame.draw.rect(window, box_filled_color, (WIDTH * 0.25, HEIGHT * 0.54, WIDTH * 0.5, HEIGHT * 0.1))
    else:
        pygame.draw.rect(window, green, (WIDTH * 0.25, HEIGHT * 0.54, WIDTH * 0.5, HEIGHT * 0.1))
    pygame.draw.rect(window, (0, 0, 0), (WIDTH * 0.25, HEIGHT * 0.54, WIDTH * 0.5, HEIGHT * 0.1), 3)
    if menu_gui["hover"] == 3:
        pygame.draw.rect(window, box_filled_color, (WIDTH * 0.25, HEIGHT * 0.69, WIDTH * 0.5, HEIGHT * 0.1))
    else:
        pygame.draw.rect(window, green, (WIDTH * 0.25, HEIGHT * 0.69, WIDTH * 0.5, HEIGHT * 0.1))
    pygame.draw.rect(window, (0, 0, 0), (WIDTH * 0.25, HEIGHT * 0.69, WIDTH * 0.5, HEIGHT * 0.1), 3)
    if menu_gui["main"] == 0:
        make_text("Play", font2, black, WIDTH * 0.5, HEIGHT * 0.44 + 5)
        make_text("Settings", font2, black, WIDTH * 0.5, HEIGHT * 0.59 + 5)
        make_text("Credits", font2, black, WIDTH * 0.5, HEIGHT * 0.74 + 5)
        if menu_gui["hover"] == 4:
            pygame.draw.rect(window, box_filled_color, (WIDTH * 0.25, HEIGHT * 0.84, WIDTH * 0.5, HEIGHT * 0.1))
        else:
            pygame.draw.rect(window, green, (WIDTH * 0.25, HEIGHT * 0.84, WIDTH * 0.5, HEIGHT * 0.1))
        make_text("Quit", font2, black, WIDTH * 0.5, HEIGHT * 0.89 + 5)
        pygame.draw.rect(window, (0, 0, 0), (WIDTH * 0.25, HEIGHT * 0.84, WIDTH * 0.5, HEIGHT * 0.1), 3)
    elif menu_gui["main"] == 1:
        make_text("Single-player", font2, black, WIDTH * 0.5, HEIGHT * 0.44 + 5)
        make_text("Multi-player", font2, black, WIDTH * 0.5, HEIGHT * 0.59 + 5)
        make_text("Back", font2, black, WIDTH * 0.5, HEIGHT * 0.74 + 5)
    pygame.display.update()
    # HEIGHT = window.get_height()
    # WIDTH = window.get_width()

pygame.mixer_music.stop()

window.fill(box_filled_color)
make_text("Loading...", font5, white, WIDTH * 0.5, HEIGHT * 0.4)
pygame.draw.rect(window, white, (WIDTH * 0.3, HEIGHT * 0.45, WIDTH * 0.4, HEIGHT * 0.1), 5)
pygame.mixer_music.load("music/guitar_music.mp3")

while run and run_loading:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.rect(window, green, (WIDTH * 0.3 + loading_X + 3, HEIGHT * 0.45 + 3, 6, HEIGHT * 0.1 - 6))
    pygame.display.update()
    pygame.time.delay(50)

    loading_X += 10

    if loading_X >= WIDTH * 0.4 - 6:
        run_loading = False

pygame.mixer.music.play(-1)
chatbox = False
settings = False
(x, y) = pygame.mouse.get_pos()

while run and run_game:
    pygame.time.delay(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            (x, y) = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # market button
            if 0.33 * WIDTH <= x <= 0.49 * WIDTH and 0.925 * HEIGHT <= y <= 0.99 * HEIGHT:
                exchange = False
                market = True
            # exchange button
            elif 0.53 * WIDTH <= x <= 0.69 * WIDTH and 0.925 * HEIGHT <= y <= 0.99 * HEIGHT:
                market = False
                exchange = True
            # close market or exchange
            elif (market or exchange) and not (0.2 * WIDTH <= x <= 0.7 * WIDTH and 90 <= y <= 590):
                market = False
                exchange = False
    keys = pygame.key.get_pressed()
    if chatbox:
        pygame.key.start_text_input()
        pygame.key.set_text_input_rect(pygame.Rect(800, 660, 260, 55))
        if keys[pygame.K_RETURN]:
            send_message(chat)
        elif keys[pygame.K_ESCAPE]:
            pygame.key.stop_text_input()
            chatbox = False
    else:
        if keys[pygame.K_LEFT] or keys[pygame.K_UP]:
            next_item(-1)
        if keys[pygame.K_RIGHT] or keys[pygame.K_DOWN]:
            next_item(1)
        if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
            keyboard_choose()
    (x, y) = pygame.mouse.get_pos()
    if 0 <= x <= WIDTH * 0.23 and HEIGHT * 0.1 <= y <= HEIGHT * 0.9 or market or exchange:
        inventory_open = True
    else:
        inventory_open = False
    if inventory_open:
        if inventory_percentage < 1:
            inventory_percentage += 0.12
    else:
        if inventory_percentage > 0:
            inventory_percentage -= 0.12
    # background
    window.fill(sky_blue)
    pygame.time.delay(50)
    window.blit(clouds, (cloud_x, 0))
    window.blit(clouds, (cloud_x - 4000, 0))
    window.blit(game_background, (0, 0))
    cloud_x += 3
    if cloud_x > 4000:
        cloud_x = 0
    # top bar
    pygame.draw.rect(window, green, (0, 0, WIDTH, HEIGHT * 0.09))
    pygame.draw.rect(window, background_filled_color, (0, HEIGHT * 0.09, WIDTH, 5))
    # day display
    pygame.draw.rect(window, dark_white, (WIDTH * 0.01, HEIGHT * 0.02, WIDTH * 0.12, HEIGHT * 0.06))
    pygame.draw.rect(window, brown, (WIDTH * 0.01, HEIGHT * 0.02, WIDTH * 0.12, HEIGHT * 0.06), 2)
    make_text("Day " + str(day), font5, brown, 0.07 * WIDTH, 0.05 * HEIGHT + 2)
    # seconds display
    pygame.draw.rect(window, dark_white, (WIDTH * 0.17, HEIGHT * 0.02, WIDTH * 0.26, HEIGHT * 0.06))
    pygame.draw.rect(window, brown, (WIDTH * 0.17, HEIGHT * 0.02, WIDTH * 0.26, HEIGHT * 0.06), 2)
    make_text(str(time) + " sec left in day", font5, brown, 0.3 * WIDTH, 0.05 * HEIGHT + 2)
    # balance display
    pygame.draw.rect(window, dark_white, (WIDTH * 0.75, HEIGHT * 0.02, WIDTH * 0.24, HEIGHT * 0.06))
    pygame.draw.rect(window, brown, (WIDTH * 0.75, HEIGHT * 0.02, WIDTH * 0.24, HEIGHT * 0.06), 2)
    make_text("Balance: $" + str(balance), font5, brown, 0.87 * WIDTH, 0.05 * HEIGHT + 2)

    # bottom bar
    pygame.draw.rect(window, background_filled_color, (0, HEIGHT * 0.91 - 5, WIDTH, 5))
    pygame.draw.rect(window, green, (0, HEIGHT * 0.91, WIDTH, HEIGHT * 0.1))
    # inventory box (0.2 * WIDTH, 90, WIDTH * 0.5, 500)
    # inventory_percentage * (WIDTH * 0.13) + WIDTH * 0.08
    inventory_position = -60 + inventory_percentage * 150
    pygame.draw.rect(window, green, (inventory_position - 100, 90, 200, 550))
    pygame.draw.rect(window, background_filled_color, (inventory_position - 100, 90, 200, 550), 4)
    # inventory text

    make_text("Inventory", font5, brown, inventory_position, 120)
    pygame.draw.rect(window, background_filled_color, (inventory_position - 60, -40 + 0.25 * HEIGHT + 31, 50, 50))
    make_text("X " + str(vegetables[g1]["count"]), font5, brown, inventory_position + 30, -40 + 0.25 * HEIGHT + 60)
    pygame.draw.rect(window, background_filled_color, (inventory_position - 60, -40 + 0.25 * HEIGHT + 91, 50, 50))
    make_text("X " + str(vegetables[g2]["count"]), font5, brown, inventory_position + 30, -40 + 0.25 * HEIGHT + 120)
    pygame.draw.rect(window, background_filled_color, (inventory_position - 60, -40 + 0.25 * HEIGHT + 151, 50, 50))
    make_text("X " + str(vegetables[g3]["count"]), font5, brown, inventory_position + 30, -40 + 0.25 * HEIGHT + 180)
    pygame.draw.rect(window, background_filled_color, (inventory_position - 60, -40 + 0.25 * HEIGHT + 211, 50, 50))
    make_text("X " + str(vegetables[g4]["count"]), font5, brown, inventory_position + 30, -40 + 0.25 * HEIGHT + 240)
    make_text("Prediction", font5, brown, inventory_position, 480)
    pygame.draw.rect(window, background_filled_color, (inventory_position - 60, 530, 50, 50))
    make_text("UP", font5, brown, inventory_position + 30, 558)
    # leaderboard gui
    pygame.draw.rect(window, background_filled_color, (790, 90, 280, 300))
    pygame.draw.rect(window, green, (795, 95, 270, 290))
    make_text("Leaderboard", font5, brown, 930, 120)
    # chat gui
    pygame.draw.rect(window, background_filled_color, (790, 400, 280, 320))
    pygame.draw.rect(window, green, (795, 405, 270, 320))
    if 800 <= x <= 1060 and 660 <= y <= 715 or chatbox:
        pygame.draw.rect(window, beige, (800, 660, 260, 55))
    else:
        pygame.draw.rect(window, dark_white, (800, 660, 260, 55))
    pygame.draw.rect(window, black, (800, 660, 260, 55), 1)
    make_text("Chat", font5, brown, 930, 430)
    # chat text box
    window.blit(font3.render(chatbox_msg, True, brown), (805, 665))
    # settings button
    if 0.01 * WIDTH <= x <= 0.17 * WIDTH and 0.925 * HEIGHT <= y <= 0.99 * HEIGHT:
        pygame.draw.rect(window, beige, (WIDTH * 0.01, HEIGHT * 0.925, WIDTH * 0.16, HEIGHT * 0.06 + 2))
    else:
        pygame.draw.rect(window, dark_white, (WIDTH * 0.01, HEIGHT * 0.925, WIDTH * 0.16, HEIGHT * 0.06 + 2))
    pygame.draw.rect(window, brown, (WIDTH * 0.01, HEIGHT * 0.925, WIDTH * 0.16, HEIGHT * 0.06 + 2), 2)
    make_text("Settings", font5, brown, 0.09 * WIDTH, 0.955 * HEIGHT + 4)
    # market button
    if 0.33 * WIDTH <= x <= 0.49 * WIDTH and 0.925 * HEIGHT <= y <= 0.99 * HEIGHT or market:
        pygame.draw.rect(window, beige, (WIDTH * 0.33, HEIGHT * 0.925, WIDTH * 0.16, HEIGHT * 0.06 + 2))
    else:
        pygame.draw.rect(window, dark_white,
                         (WIDTH * 0.33, HEIGHT * 0.925, WIDTH * 0.16, HEIGHT * 0.06 + 2))
    pygame.draw.rect(window, brown, (WIDTH * 0.33, HEIGHT * 0.925, WIDTH * 0.16, HEIGHT * 0.06 + 2), 2)
    make_text("Market", font5, brown, 0.41 * WIDTH, 0.955 * HEIGHT + 4)
    # exchange button
    if 0.53 * WIDTH <= x <= 0.69 * WIDTH and 0.925 * HEIGHT <= y <= 0.99 * HEIGHT or exchange:
        pygame.draw.rect(window, beige, (WIDTH * 0.53, HEIGHT * 0.925, WIDTH * 0.16, HEIGHT * 0.06 + 2))
    else:
        pygame.draw.rect(window, dark_white,
                         (WIDTH * 0.53, HEIGHT * 0.925, WIDTH * 0.16, HEIGHT * 0.06 + 2))
    pygame.draw.rect(window, brown, (WIDTH * 0.53, HEIGHT * 0.925, WIDTH * 0.16, HEIGHT * 0.06 + 2), 2)
    make_text("Exchange", font5, brown, 0.61 * WIDTH, 0.955 * HEIGHT + 4)
    # market menu
    if market:
        # top bar
        pygame.draw.rect(window, green, (0.2 * WIDTH, 90, WIDTH * 0.5, 500))
        pygame.draw.rect(window, background_filled_color, (0.2 * WIDTH, 90, WIDTH * 0.5, 500), 4)
        pygame.draw.rect(window, dark_white, (0.2 * WIDTH + 100, 100, WIDTH * 0.39, 400))
        # buy button
        if 400 <= x <= 550 and 520 <= y <= 520 + HEIGHT * 0.06 + 2:
            pygame.draw.rect(window, beige, (400, 520, 150, HEIGHT * 0.06 + 2))
        else:
            pygame.draw.rect(window, dark_white, (400, 520, 150, HEIGHT * 0.06 + 2))
        pygame.draw.rect(window, brown, (400, 520, 150, HEIGHT * 0.06 + 2), 2)
        make_text("Buy X 1", font5, brown, 475, 550-4)
        # sell button
        if 575 <= x <= 725 and 520 <= y <= 520 + HEIGHT * 0.06 + 2:
            pygame.draw.rect(window, beige, (575, 520, 150, HEIGHT * 0.06 + 2))
        else:
            pygame.draw.rect(window, dark_white, (575, 520, 150, HEIGHT * 0.06 + 2))
        pygame.draw.rect(window, brown, (575, 520, 150, HEIGHT * 0.06 + 2), 2)
        make_text("Sell X 1", font5, brown, 650, 550-4)
        # select veg buttons
        if market_selection == 1:
            pygame.draw.rect(window, yellow, (240, -40 + 0.25 * HEIGHT + 31, 50, 50))
        else:
            pygame.draw.rect(window, background_filled_color, (240, -40 + 0.25 * HEIGHT + 31, 50, 50))
        if market_selection == 2:
            pygame.draw.rect(window, yellow, (240, -40 + 0.25 * HEIGHT + 91, 50, 50))
        else:
            pygame.draw.rect(window, background_filled_color, (240, -40 + 0.25 * HEIGHT + 91, 50, 50))
        if market_selection == 3:
            pygame.draw.rect(window, yellow, (240, -40 + 0.25 * HEIGHT + 151, 50, 50))
        else:
            pygame.draw.rect(window, background_filled_color, (240, -40 + 0.25 * HEIGHT + 151, 50, 50))
        if market_selection == 4:
            pygame.draw.rect(window, yellow, (240, -40 + 0.25 * HEIGHT + 211, 50, 50))
        else:
            pygame.draw.rect(window, background_filled_color, (240, -40 + 0.25 * HEIGHT + 211, 50, 50))

    pygame.display.update()


pygame.quit()
