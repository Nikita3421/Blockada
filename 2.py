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