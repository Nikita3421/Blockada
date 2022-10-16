for l in blocks_1:

        if sprite.spritecollide(l, manas, True):
            kick.play()
            items.remove(mana)

        if sprite.collide_rect(hero, l):
            hero.rect.x = l.rect.x - hero.width

        if sprite.collide_rect(en1, l):
            en1.side = 'right'
            en1.image = transform.scale(image.load(enemy_r),(en2.width, en1.height))

        if sprite.collide_rect(en2, l):
            en2.side = 'right'
            en2.image = transform.scale(image.load(enemy_r), (en2.width, en2.height))

        if sprite.collide_rect(en3, l):
            en3.side = 'right'
            en3.image = transform.scale(image.load(enemy_r), (en3.width, e3.height))

        if sprite.collide_rect(e4, l):
            en4.side = 'right'
            en4.image = transform.scale(image.load(enemy_r),(en4.width, en4.height))

def rules(): #правила
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

def restart(): #перезапуск

    over = True

    mixer.music.stop()
    mixer.music.load('sounds/game_over.ogg')
    mixer.music.play()

    while over:

        for e in event.get():
            if e.type == QUIT:
                over = False

        time.delay(15)

        win.fill((0,0,0))
        win.blit(lose,(350, 200))

        btn_restart.draw(60, 5)
        btn_menu.draw(0, 5)

        pos_x, pos_y = mouse.get_pos()

        for e in event.get():

            if btn_restart.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                click.play()
                mixer.music.stop()
                over = False
                res_pos()
                lvl_1()

            if btn_restart.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                click.play()
                over = False
                menu()

        display.update()

def res_pos():

    global items, manas, coins, platforms, stairs, blocks_r, blocks_l
    global hero, en1, en2, en3, en4, door, key1, key2, portal, chest, camera
    global k_door, k_chest, o_chest, c_count
