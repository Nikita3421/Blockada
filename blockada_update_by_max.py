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

    return Rect(1, t, w, h)


win_width = 1280
win_height = 720
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(
    "image/Fone.png"), (win_width, win_height))
window.blit(background, (0, 0))

display.set_caption("Maze_defection")

clock = time.Clock()
game = True
FPS = 60

mixer.init()
fire_s = mixer.Sound('sounds/fire.ogg')
kick = mixer.Sound('sounds/kick.ogg')
k_up = mixer.Sound('sounds/k_coll.ogg')
c_coll = mixer.Sound('sounds/c_coll.ogg')
d_o = mixer.Sound('sounds/lock.ogg')
tp = mixer.Sound('sounds/teleport.ogg')
click = mixer.Sound('sounds/click.ogg')
cst_o = mixer.Sound('sounds/chest.ogg')

btn_start = Button((178, 34, 34), 470, 300, 280, 70,
                   'START GAME', 50, (255, 255, 255))
btn_control = Button((178, 34, 34), 470, 450, 280, 70,
                     'HOW TO PLAY', 50, (255, 255, 255))
btn_exit = Button((178, 34, 34), 470, 600, 280, 70,
                  'EXIT GAME', 50, (255, 255, 255))
btn_menu = Button((178, 34, 34), 470, 600, 280, 70,
                  'BACK to MENU', 50, (255, 255, 255))
btn_restart = Button((178, 34, 34), 470, 450, 280, 70,
                     'RESTART', 50, (255, 255, 255))
btn_continue = Button((178, 34, 34), 470, 350, 280, 70,
                      'CONTINUE', 50, (255, 255, 255))
btn_pause = Button((178, 34, 34), 1200, 15, 50, 50, 'I I', 40, (255, 255, 255))

hero_r = "images/sprite1_r.png"
hero_l = "images/sprite1.png"
enemy_l = "images/cyborg.png"
enemy_r = "images/cyborg_r.png"
coin = "images/coin.png"
door_img = "images/door.png"
key_img = "images/key.png"
chest_open = "images/cst_open.png"
chest_close = "images/cst_close.png"
cyborg = "images/cyborg.png"
stair = "images/stair.png"
port = "images/portal.png"
platform = "images/platform.png"
nothing = "images/nothing.png"
power = "images/mana.png"

hero = Player(300, 650, 50, 50, 5, hero_l)

en1 = Enemy(420, 480, 50, 50, 3, enemy_l, 'left')
en2 = Enemy(230, 320, 50, 50, 3, enemy_l, 'left')

door = Settings(1000, 580, 40, 120, 0, door_img)
key1 = Settings(160, 350, 50, 20, 0, key_img)
key2 = Settings(1500, 350, 50, 20, 0, key_img)
portal = Settings(2700, 600, 100, 100, 0, port)
chest = Settings(450, 130, 80, 80, 0, chest_close)

# camera = Camera(camera_configure, level_width, level_height)

blocks_r = []
blocks_l = []
coins = []
stairs = []
platforms = []

items = sprite.Group()

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

        if c == "":
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

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)