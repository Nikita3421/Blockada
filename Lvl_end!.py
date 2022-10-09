def lvl_end():#рівень пройдено

    stop = True

    mixer.music.stop()
    mixer.music.load("sounds/game_over.ogg")
    mixer.music.play()

    while stop:

        for e in event.get():
            if e.type == QUIT:
                stop = False

        time.delay(15)

        win.fill((0, 0, 0,))     
        win.blit(done(300, 200))   

        btn_restart.draw(60, 5)
        btn_menu.draw(0, 5)

        pos_x, pos_y = mouse.get_pos()

        for e in event.get():
            #перезапуск гри
            if btn_restart.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                click.play()
                mixer.music.stop()
                stop = False
                res_pos()
                lvl_1()
            
            #меню
            if btn_menu.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                click.play()
                mixer.music.stop()
                stop = False
                menu()