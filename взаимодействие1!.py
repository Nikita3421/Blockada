    for r in blocks_r:

        if sprite.spritecollide(r, manas, True):
            kick.play()
            items.remove(mana)

        if sprite.spritecollide(r):
            hero.rect.x = r.rect.x + hero.width - 5

        if sprite.spritecollide(en1, r):
            en1.side = 'left'
            en1.image =transform.scale(image.load(enemy_l), (en1.width, en1.height))

        if sprite.spritecollide(en2, r):
            en2.side = 'left'
            en2.image =transform.scale(image.load(enemy_l), (en2.width, en2.height))

        if sprite.spritecollide(en3, r):
            en3.side = 'left'
            en3.image =transform.scale(image.load(enemy_l), (en3.width, en3.height))

        if sprite.spritecollide(en4, r):
            en4.side = 'left'
            en4.image =transform.scale(image.load(enemy_l), (en4.width, en4.height))
