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
