from pygame import *
level = [
    "                                       ",
    "----------                    ---------",
    "                  oo                   ",
    "              o        o           o   ",
    "-----         ----------          -----",
    "  o                                    ",
    "                                       ",
    " ----------                  ----------",
    "                                       ",
    "             o                         ",
    "                  o                    ",
    "---------------------------------------"]

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


class Player(Settings):

    def r_l(self):
        global mana, img, f
        f = 1
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
            mana.side = "left"
            f = 1
        if keys[K_d]:
            self.rect.x += self.speed
            f = 0
            mana.side = "right"

        if f == 1:
            self.image = transform.scale(
                image.load(hero_r), (self.width, self.height))
        if f == 0:
            self.image = transform.scale(
                image.load(hero_l), (self.width, self.height))

    def u_d(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect -= self.speed
        if keys[K_s]:
            self.rect += self.speed


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


# mixer.init()
# fire_s = mixer.Sound('sounds/fire.ogg')
# kick = mixer.Sound('sounds/kick.ogg')
# k_up = mixer.Sound('sounds/k_coll.ogg')
# c_coll = mixer.Sound('sounds/c_coll.ogg')
# d_o = mixer.Sound('sounds/lock.ogg')
# tp = mixer.Sound('sounds/teleport.ogg')
# click = mixer.Sound('sounds/click.ogg')
# cst_o = mixer.Sound('sounds/chest.ogg')

c_count = 0
win_width = 1280
win_height = 720
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(
    "images/Fone.png"), (win_width, win_height))
window.blit(background, (0, 0))

display.set_caption("Maze_defection")

clock = time.Clock()
FPS = 60

hero_r = "images/sprite1_r.png"  # 1
hero_l = "images/sprite1.png"  # 1
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
# nothing = "images/nothing.png"  # 0
power = "images/mana.png"  # 1

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


hero = Player(300, 650, 50, 50, 5, hero_l)

en1 = Enemy(420, 480, 50, 50, 3, enemy_l, 'left')
en2 = Enemy(230, 320, 50, 50, 3, enemy_l, 'left')

door = Settings(1000, 580, 40, 120, 0, door_img)
key1 = Settings(160, 350, 50, 20, 0, key_img)
key2 = Settings(1500, 350, 50, 20, 0, key_img)
portal = Settings(2700, 600, 100, 100, 0, port)
chest = Settings(450, 130, 80, 80, 0, chest_close)

camera = Camera(camera_configure, level_width, level_height)

blocks_r = []
blocks_l = []
coins = []
stairs = []
platforms = []

items = sprite.Group()

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

x = y = 0
for r in level:

    for c in r:

        if c == "r":
            r1 = Settings(x, y, 40, 40, 0, nothing)
            blocks_r.append(r1)
            items.add(r1)

        if c == "l":
            r1 = Settings(x, y, 40, 40, 0, nothing)
            blocks_l.append(r1)
            items.add(r1)

        if c == "/":
            r2 = Settings(x, y - 40, 40, 180, 0, stair)
            stairs.append(r2)
            items.add(r2)

        if c == "o":
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
    х = 0

while game:

    time.delay(15)
    window.blit(background, (0, 0))
    keys = key.get_pressed()

    for e in event.get():
        if e.type == QUIT:
            game = False

    en1.update()
    en2.update()

    hero.r_l()

    for s in stairs:
        if sprite.collide_rect(hero, s):
            hero.u_d()
            if hero.rect.y <= (s.rect.y - 40):
                hero.rect.y = s.rect.y - 40
            if hero.rect.y >= (s.rect.y + 130):
                hero.rect.y = s.rect.y + 130

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

    if sprite.collide_rect(hero, chest) and k_chest == False:
        window.blit(k_need, (450, 50))
    if sprite.collide_rect(hero, chest) and k_chest == True and c_count != 15:

        window.blit(e_tap, (450, 50))

        if keys[K_e]:

            o_chest = True
            c_count += 10
            chest.image = transform.scale(image.load(
                chest_open), (chest.width, chest.height))
            cst_o.play()
            k_door = True

    if sprite.collide_rect(hero, portal):
        tp.play()
        game = False

    camera.update(hero)

    for i in items:
        window.blit(i.image, camera.apply(i))

    if sprite.collide_rect(hero, key1):
        window.blit(e_tap, (500, 50))
        if keys[K_e]:
            k_chest = True
            key1.rect.y = -100
            items.remove(key1)
            k_up.play()
    if sprite.collide_rect(hero, key2):
        window.blit(e_tap, (500, 50))
        if keys[K_e]:
            k_door = True
            key2.rect.y = -100
            items.remove(key2)
            k_up.play()

    if sprite.collide_rect(hero, door) and k_door == False:
        window.blit(k_need, (450, 50))
        hero.rect.x = door.rect.x - 47
    if sprite.collide_rect(hero, door) and k_door == True:
        hero.rect.x = door.rect.x - 47
        window.blit(e_tap, (500, 50))
        if keys[K_e]:
            door.rect.x += 1500
            d_o.play()
            k_door = False

    for c in coins:
        if sprite.collide_rect(hero, c):
            c_coll.play()
            c_count += 1
            coins.remove(c)
            items.remove(c)

    coin_c = font2.render(':' + str(c_count), True, (255, 255, 255))
    window.blit(transform.scale(image.load(
        "images/coin.png"), (50, 50)), (10, 10))
    window.blit(coin_c, (55, 15))

    display.update()
    clock.tick(FPS)
