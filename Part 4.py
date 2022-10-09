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
