from pygame import * 
class Settings(sprite.Sprite):
    def __init__(self, x, y, w, h, speed, img):
        super().__init__()
        self.speed = speed
        self.width = w
        self.height = h
        self.image = transform.scale(image.load(img),(self.width,self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
win_width = 1280
win_height = 720
window = display.set_mode((win_width, win_height))
display.set_caption("Maze_defection")
background = transform.scale(image.load("Fone.jpg"), (win_width, win_height))
window.blit(background,(0,0))
clock = time.Clock()
game = True
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)  

   
