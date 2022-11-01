       if keys[K_SPACE]:
            mana.rect.x, mana.rect.y = hero.rect.centerx, hero.rect.top
            if f==1:
                mana.side = "left"
            if f==0:
                mana.side = "right"
