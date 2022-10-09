class Mana(Settings):
    def __init__(self, x, y, w, h, speed, img, side):
        Settings.__init__(self, x, y, w, h, speed, img)
        
        self.side = side
        
    def update(self):
        global side
        
        if self.side == 'left':
            self.rect.x -= self.speed
        if self.side == 'right':
            self.rect.x += self.speed

mana = Mana(0, -100, 25, 25, 35, power, 'left')
