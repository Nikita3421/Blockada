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
