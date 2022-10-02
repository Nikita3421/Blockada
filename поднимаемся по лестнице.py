#піднімаємося по сходамвв
for s in stairs:

    if sprite.spritecollide(s, manas, True): #атакуючі закляття безсильні проти сходів
        kick.play()
        items.remove(mana)

    if spride.collide_rect(hero, s):
        hero.u_d()

        if hero.rect.y <= (s.rect.y - 40): #умова, щоб гравець не піднімався вище платформи
            hero.rect.y = s.rect.y - 40

        if hero.rect.y >= (s.rect.y + 130): #умова, щоб гравець не спускався вище платформи
            hero.rect.y = s.rect.y + 130    