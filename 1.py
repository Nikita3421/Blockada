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



def pause():
    stop = True

    mixer.music.stop()

    while stop:
        for e in event.get():
            if e.type == QUIT:
                stop = False
        
        time.delay(15)

        win.fill((0,0,0))
        win.blit(pausa,(440,200))

        btn_continue.draw(50,5)
        btn_restart(60,5)
        btn_menu.draw(0, 5)

        for e in event.get():
            if btn_continue.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                click.play()
                stop = False
                mixer.music.stop()
                lvl_1()

            if btn_continue.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                click.play()
                mixer.music.stop()
                res_pos()
                stop = False
                lvl_1()

            if btn_continue.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                click.play()
                mixer.music.stop()
                stop = False
                game = False
                menu()
        display.update()



def rules():
    rule = True
    mixer.music.stop()

    while rule:

        for e in event.get():
            if e.type == QUIT:
                rule = False
        
        time.delay(15)

        win.blit(bg, (0, 0))
        win.blit(gname,(320, 70))
        win.blit(wasd_b,(50, 250))
        win.blit(space_b,(50, 350))
        win.blit(e_b,(50, 450))

        btn_menu.draw(0, 5)

        pos_x, pos_y = mouse.get_pos()

        for e in event.get():

            if btn_menu.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                click.play()
                rule = False
                menu()
            
            if e.type == QUIT:
                rule = False
            
        display.update()


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