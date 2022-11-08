
from pygame import *
level = [
       "r                                                                    .",
       "r                                                                    .",
       "r                                                                    .",
       "r                                                                    .",
       "rr    °  °      l                             r    °  °  °     l     .",
       "r  ------------                                ---------------       .",
       "rr / l                                       r / l         r / l     .",
       "rr                                               l             l     .",
       "rr     °  l                       r     °  °     l   r         l     .",
       "r  ------                           ------------       -------       .",
       "r     r / l                                          r / l           .",
       "r                                                                    .",
       "rr           l                       r          °             °     l.",
       "r -----------                         ------------------------------ .",
       "r        r / l                                  r / l                ."]

hero_l = "images/sprite1_r.png"  # 1
hero_r = "images/sprite1.png"  # 1
enemy_l = "images/cyborg.png"  # 1
enemy_r = "images/cyborg_r.png"  # 1
coin = "images/coin.png"  # 1
door_img = "images/door.png"  # 1
key_img = "images/key.png"  # 1
chest_open = "images/cst_open.png"  # 1
chest_close = "images/cst_close.png"  # 1
stair = "images/stair.png"  # 1
port = "images/portal.png"  # 1
platform = "images/platform.png"  # 1
nothing = "images/nothing.png"  # 1
power = "images/mana.png"  # 1

level_width = len(level[0])*40  # прораховуємо ширину рівня
level_height = len(level)*40    # прораховуємо висоту рівня


class Settings(sprite.Sprite):
    def __init__(self, x, y, w, h, speed, img):
        super().__init__()

        self.speed = speed
        self.width = w
        self.height = h
        self.image = transform.scale(
            image.load(img), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Button():
    def __init__(self, color, x, y, w, h, text, fsize, txt_color):

        self.width = w
        self.height = h
        self.color = color

        self.image = Surface([self.width, self.height])
        self.image.fill((color))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.fsize = fsize
        self.text = text
        self.txt_image = font.Font(
            'font/impact.ttf', fsize).render(text, True, txt_color)
        self.txt_color = font.Font(
            'font/impact.ttf', fsize).render(text, True, txt_color)

    def draw(self, shift_x, shift_y):

        window.blit(self.image, (self.rect.x, self.rect.y))
        window.blit(self.txt_image, (self.rect.x +
                    shift_x, self.rect.y + shift_y))


class Enemy(Settings):
    def __init__(self, x, y, w, h, speed, img, side):
        Settings.__init__(self, x, y, w, h, speed, img)

        self.side = side

    def update(self):
        global side

        if self.side == "right":
            self.rect.x -= self.speed
        if self.side == "left":
            self.rect.x += self.speed


class Mana(Settings):
    def __init__(self, x, y, w, h, speed, img, side):
        Settings.__init__(self, x, y, w, h, speed, img)

        self.side = side

    def update(self):
        global side,f

        if self.side == 'left':
            self.rect.x -= self.speed
        if self.side == 'right':
            self.rect.x += self.speed
mana = Mana(0, -100, 25, 25, 35, power, 'left')

class Player(Settings):

    def r_l(self):
        global mana, img, f
        f = 1
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
            f = 1
        if keys[K_d]:
            self.rect.x += self.speed
            f = 0

        if f == 1:
            self.image = transform.scale(
                image.load(hero_r), (self.width, self.height))
        if f == 0:
            self.image = transform.scale(
                image.load(hero_l), (self.width, self.height))

    def u_d(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed


class Camera(object):

    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_configure(camera, target_rect):

    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + win_width / 2, -t + win_height / 2

    l = min(0, l)
    l = max(-(camera.width - win_width), l)
    t = max(-(camera.height - win_height), t)
    t = min(0, t)

    return Rect(l, t, w, h)


def menu():
    #mixer.music.load('sounds/menu.ogg')
    #mixer.music.play()
    menu = True

    while menu:

        for e in event.get():
            if e.type == QUIT:
                menu = False

        time.delay(15)
        pos_x, pos_y = mouse.get_pos()
        window.blit(background, (0, 0))
        window.blit(gname, (320, 70))

        btn_start.draw(15, 5)
        btn_control.draw(10, 5)
        btn_exit.draw(37, 5)

        for e in event.get():

            if btn_start.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                menu = False
                res_pos()
                lvl_1()

            if btn_control.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                menu = False
                rules()

            if btn_exit.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                menu = False
                a = 0

            if e.type == QUIT:
                menu = False
                a = 0

        display.update()


def pause():
    stop = True

    while stop:
        for e in event.get():
            if e.type == QUIT:
                stop = False

        time.delay(15)

        window.fill((0, 0, 0))
        window.blit(pausa, (440, 200))

        btn_continue.draw(50, 5)
        btn_restart.draw(60, 5)
        btn_menu.draw(0, 5)

        pos_x, pos_y = mouse.get_pos()

        for e in event.get():
            if btn_continue.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                stop = False
                lvl_1()

            if btn_restart.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                res_pos()
                stop = False
                lvl_1()

            if btn_menu.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                game = False
                stop = False
                menu()

        display.update()


def lvl_end():  # рівень пройдено
    mixer.music.stop()
    mixer.music.load('sounds/game_over.ogg')
    mixer.music.play()
    stop = True

    while stop:

        for e in event.get():
            if e.type == QUIT:
                stop = False

        time.delay(15)

        window.fill((0, 0, 0,))
        window.blit(done(300, 200))

        btn_restart.draw(60, 5)
        btn_menu.draw(0, 5)

        pos_x, pos_y = mouse.get_pos()

        for e in event.get():

            if btn_restart.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                mixer.music.stop()
                stop = False

            if btn_menu.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                stop = False
                menu()


def rules():
    rule = True

    while rule:

        for e in event.get():
            if e.type == QUIT:
                rule = False

        time.delay(15)

        window.blit(background, (0, 0))
        window.blit(gname, (320, 70))
        window.blit(wasd_b, (50, 250))
        window.blit(space_b, (50, 350))
        window.blit(e_b, (50, 450))

        btn_menu.draw(0, 5)

        pos_x, pos_y = mouse.get_pos()

        for e in event.get():

            if btn_menu.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                rule = False
                menu()

            if e.type == QUIT:
                rule = False

        display.update()


def res_pos():

    global items, manas, coins, platforms, stairs, blocks_r, blocks_l
    global hero, en1, en2, door, key1, key2, portal, chest, camera
    global k_door, k_chest, o_chest, c_count

    hero = Player(200, 605, 45, 80, 5, hero_l)

    en1 = Enemy(380, 463, 95, 65, 3, enemy_l, 'left')
    en2 = Enemy(380, 300, 95, 65, 3, enemy_l, 'left')

    mana = Mana(0, -100, 25, 25, 35, power, 'left')

    door = Settings(1000, 530, 80, 150, 0, door_img)
    key1 = Settings(170, 335, 50, 20, 0, key_img)
    key2 = Settings(1500, 335, 50, 20, 0, key_img)
    chest = Settings(500, 150, 60, 60, 0, chest_close)
    portal = Settings(2700, 600, 100, 200, 0, port)

    camera = Camera(camera_configure, level_width, level_height)

    blocks_r = []
    blocks_l = []
    coins = []
    stairs = []
    platforms = []

    items = sprite.Group()
    manas = sprite.Group()

    items.add(door)
    items.add(key1)
    items.add(key2)
    items.add(portal)
    items.add(chest)
    items.add(en1)
    items.add(en2)
    items.add(hero)

    game = True

    k_door = False
    k_chest = False
    o_chest = False

    c_count = 0

    x = y = 0
    for r in level:

        for c in r:

            if c == "r":
                r1 = Settings(x, y, 30, 30, 0, nothing)
                blocks_r.append(r1)
                items.add(r1)

            if c == "l":
                r1 = Settings(x, y, 30, 30, 0, nothing)
                blocks_l.append(r1)
                items.add(r1)

            if c == "/":
                r2 = Settings(x, y - 45, 40, 153, 0, stair)
                stairs.append(r2)
                items.add(r2)

            if c == "°":
                r3 = Settings(x, y, 40, 40, 0, coin)
                coins.append(r3)
                items.add(r3)

            if c == "*":
                r4 = Settings(x, y, 40, 40, 0, portal)
                items.add(r4)

            if c == "-":
                r5 = Settings(x, y, 40, 40, 0, platform)
                platforms.append(r5)
                items.add(r5)

            if c == ">":
                r6 = Settings(x, y - 40, 80, 80, 0, chest_close)
                items.add(r6)

            x += 40

        y += 40
        x = 0


def collider():
    global k_door, k_chest, o_chest, c_count

    keys = key.get_pressed()

    for r in blocks_r:
        if sprite.collide_rect(hero, r):
            hero.rect.x = r.rect.x + hero.width
        if sprite.collide_rect(en1, r):
            en1.side = ' left '
            en1.image = transform.scale(
                image.load(enemy_l), (en1.width, en1.height))
        if sprite.collide_rect(en2, r):
            en2.side = ' left '
            en2.image = transform.scale(
                image.load(enemy_l), (en2.width, en2.height))

    for l in blocks_l:
        if sprite.collide_rect(hero, l):
            hero.rect.x = l.rect.x - hero.width
        if sprite.collide_rect(en1, l):
            en1.side = ' right '
            en1.image = transform.scale(
                image.load(enemy_r), (en1.width, en1.height))
        if sprite.collide_rect(en2, l):
            en2.side = ' right '
            en2.image = transform.scale(
                image.load(enemy_r), (en2.width, en2.height))

    for r in blocks_r:

        if sprite.spritecollide(r, manas, True):
            items.remove(mana)

        if sprite.collide_rect(hero, r):
            hero.rect.x = r.rect.x + hero.width - 5

        if sprite.collide_rect(en1, r):
            en1.side = 'left'
            en1.image = transform.scale(
                image.load(enemy_l), (en1.width, en1.height))

        if sprite.collide_rect(en2, r):
            en2.side = 'left'
            en2.image = transform.scale(
                image.load(enemy_l), (en2.width, en2.height))

        # if sprite.spritecollide(en3, r):
        #     en3.side = 'left'
        #     en3.image =transform.scale(image.load(enemy_l), (en3.width, en3.height))

        # if sprite.spritecollide(en4, r):
        #     en4.side = 'left'
        #     en4.image =transform.scale(image.load(enemy_l), (en4.width, en4.height))

    for l in blocks_l:

        if sprite.spritecollide(l, manas, True):
            items.remove(mana)

        if sprite.collide_rect(hero, l):
            hero.rect.x = l.rect.x - hero.width

        if sprite.collide_rect(en1, l):
            en1.side = 'right'
            en1.image = transform.scale(
                image.load(enemy_r), (en2.width, en1.height))

        if sprite.collide_rect(en2, l):
            en2.side = 'right'
            en2.image = transform.scale(
                image.load(enemy_r), (en2.width, en2.height))

        # if sprite.collide_rect(en3, l):
        #     en3.side = 'right'
        #     en3.image = transform.scale(image.load(enemy_r), (en3.width, e3.height))

        # if sprite.collide_rect(e4, l):
        #     en4.side = 'right'
        #     en4.image = transform.scale(image.load(enemy_r),(en4.width, en4.height))

    coin_c = font2.render(':' + str(c_count), True, (255, 255, 255))
    window.blit(transform.scale(image.load(
        "images/coin.png"), (50, 50)), (10, 10))
    window.blit(coin_c, (55, 15))

    for c in coins:
        if sprite.collide_rect(hero, c):
            #c_coll.play()
            c_count += 1
            coins.remove(c)
            items.remove(c)

    for s in stairs:
        if sprite.spritecollide(s, manas, True):
            items.remove(mana)

        if sprite.collide_rect(hero, s):
            hero.u_d()
            if hero.rect.y <= (s.rect.y - 80):
                hero.rect.y = s.rect.y - 80
            if hero.rect.y >= (s.rect.y + 130):
                hero.rect.y = s.rect.y + 130

    if sprite.collide_rect(hero, key1):
        window.blit(e_tap, (500, 50))
        if keys[K_e]:
            k_up.play()
            k_chest = True
            key1.rect.y = -100
            items.remove(key1)

    if sprite.collide_rect(hero, key2):
        window.blit(e_tap, (500, 50))
        if keys[K_e]:
            k_up.play()
            k_door = True
            key2.rect.y = -100
            items.remove(key2)

    if sprite.collide_rect(hero, door) and k_door == False:
        window.blit(k_need, (450, 50))
        hero.rect.x = door.rect.x - 100

    if sprite.collide_rect(hero, door) and k_door == True:
        hero.rect.x = door.rect.x - 100
        window.blit(e_tap, (500, 50))

        if keys[K_e]:
            #d_o.play()
            door.rect.x += 1500
            k_door = False

    if sprite.collide_rect(hero, chest) and k_chest == False:
        window.blit(k_need, (450, 50))

    if sprite.collide_rect(hero, chest) and k_chest == True and c_count != 15:
        window.blit(e_tap, (450, 50))
        
        if keys[K_e]:
            cst_o.play()

            o_chest = True
            c_count += 10
            chest.image = transform.scale(image.load(
                chest_open), (chest.width, chest.height))
            k_door = True
            hero.rect.x-=20
            chest.rect.x=-100 

    if sprite.collide_rect(hero, portal):
        game = False
    if sprite.spritecollide(en1, manas, True):
        en1.rect.y = -150 # якщо не перемістити ворога за межі екрану, його привид може вбити грваця
        items.remove(mana)
        #kick.play()
    if sprite.spritecollide(en2, manas, True):
        en2.rect.y = -150
        items.remove(mana)
        #kick.play()


def restart():  # перезапуск
    mixer.music.stop()
    mixer.music.load('sounds/game_over.ogg')
    mixer.music.play()
    over = True

    while over:

        for e in event.get():
            if e.type == QUIT:
                over = False

        time.delay(15)

        window.fill((0, 0, 0))
        window.blit(lose, (350, 200))

        btn_restart.draw(60, 5)
        btn_menu.draw(0, 5)

        pos_x, pos_y = mouse.get_pos()

        for e in event.get():

            if btn_restart.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                over = False
                res_pos()
                lvl_1()

            if btn_menu.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                over = False
                menu()

        display.update()


mixer.init()
fire_s = mixer.Sound('sounds/fire.ogg')
#kick = mixer.Sound('sounds/kick.ogg')
k_up = mixer.Sound('sounds/k_coll.ogg')
# c_coll = mixer.Sound('sounds/c_coll.ogg')
d_o = mixer.Sound('sounds/lock.ogg')
# tp = mixer.Sound('sounds/teleport.ogg')
click = mixer.Sound('sounds/click.ogg')
cst_o = mixer.Sound('sounds/chest.ogg')


c_count = 0
win_width = 1280
win_height = 720
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load("images/Fone.png"), (win_width, win_height))
window.blit(background, (0, 0))

display.set_caption("Maze_defection")

clock = time.Clock()
FPS = 60



font.init()
font1 = font.SysFont((' font / ariblk.ttf '), 200)
gname = font1.render(' Blockada ', True, (106, 90, 205), (250, 235, 215))
font2 = font.SysFont((' font / ariblk.ttf '), 60)
e_tap = font2.render(' press ( e ) ', True, (255, 80, 255))
k_need = font2.render(' You need a key to open ! ', True, (255, 0, 255))
space = font2.render(' press( space ) to kill the enemy ', True, (255, 0, 255))
font3 = font.SysFont((' font / calibrib.ttf '), 45)
wasd_b = font3.render(
    ' WASD - move buttons . You can only go up and down the stairs ', True, (255, 0, 0))
space_b = font3.render(
    ' Space - shoot button . You are a wizard who only knows one spell ', True, (255, 0, 0))
e_b = font3.render(
    ' E interaction button . Open doors , collect keys , activate portals ', True, (255, 0, 0))
font4 = font.SysFont((' font / ariblk.ttf '), 150)
done = font4.render('LEVEL DONE !', True, (0, 255, 0), (255, 100, 0))
lose = font4.render(' YOU LOSE ! ', True, (255, 0, 0), (245, 222, 179))
pausa = font4.render(' PAUSE ', True, (255, 0, 0), (245, 222, 179))

btn_start = Button((178, 34, 34), 470, 300, 280, 70,
                   ' START GAME ', 50, (255, 255, 255))
btn_control = Button((178, 34, 34), 470, 450, 280, 70,
                     ' HOW TO PLAY ', 50, (255, 255, 255))
btn_exit = Button((178, 34, 34), 470, 600, 280, 70,
                  ' EXIT GAME ', 50, (255, 255, 255))
btn_menu = Button((178, 34, 34), 470, 600, 280, 70,
                  ' BACK to MENU ', 50, (255, 255, 255))
btn_restart = Button((178, 34, 34), 470, 450, 280, 70,
                     ' RESTART ', 50, (255, 255, 255))
btn_continue = Button((178, 34, 34), 470, 350, 280, 70,
                      ' CONTINUE ', 50, (255, 255, 255))
btn_pause = Button((178, 34, 34), 1200, 15, 50, 50,
                   ' I I ', 40, (255, 255, 255))




def lvl_1():
    #mixer.music.load('sounds/game.ogg') # настав час додати фонову музику
    #mixer.music.play()
    game = True
    while game:
        time.delay(15)
        window.blit(background, (0, 0))
        keys = key.get_pressed()
        pos_x, pos_y = mouse.get_pos()
        for e in event.get():
            if e.type == QUIT:
                game = False
            if btn_pause.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                pause()
                game = False
        en1.update()
        en2.update()
        # en3.update()
        # en4.update()
        hero.r_l()
        mana.update()
        btn_pause.draw(10, 0)
        collider()
        if keys[K_SPACE]:
            mana.rect.x, mana.rect.y = hero.rect.centerx, hero.rect.centery
            if f==1:
                mana.side = "left"
            if f==0:
                mana.side = "right"
            manas.add(mana)
            items.add(mana)
            fire_s.play()

        camera.update(hero)
        for i in items:
            window.blit(i.image, camera.apply(i))
        if sprite.collide_rect(hero, en1) or sprite.collide_rect(hero, en2):
            restart()
            game = False
        if sprite.collide_rect(hero, portal):
            lvl_end()
            game = False

        display.update()


menu()