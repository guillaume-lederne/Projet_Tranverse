import pygame
import pygame as p
import game_file
import random
import time as t

p.init()

p.display.set_caption('WWI')


game = game_file.Game()

screen = game.terrain.fenetre
game.terrain.fonctions()
fonction=game.terrain.fonction
game.player.terrain=game.terrain.fonction

running=True

terrain=game.terrain.generer_terrain()
game.player.rect.y=fonction(0)[0]-40
game.terrain.choix_couleur()
while running:
    t.sleep(0.005)

    # Dessin du terrain

    screen.fill(game.terrain.couleur_ciel)

    # Dessin du terrain
    points = []
    p.draw.rect(screen, game.terrain.couleur_sol, ((0, terrain[0]), (50, game.terrain.hauteur_fenetre)))
    x = 0
    while x < game.terrain.largeur:
        points.append((x+50, terrain[x]))
        x += 1
    points.append((game.terrain.largeur, game.terrain.hauteur_fenetre))
    points.append((0, game.terrain.hauteur_fenetre))
    pygame.draw.polygon(screen, game.terrain.couleur_sol, points)

    screen.blit(game.player.image,game.player.rect)


    if game.pressed.get(pygame.K_RIGHT)and game.player.rect.x<960 and game.player.essence>=0:
        game.player.move_right()
        game.player.move_up()
        game.player.rotate(fonction(game.player.rect.x-60+game.terrain.offset)[1])
        angle_conso = game.player.angle
        if angle_conso<-1:
            angle_conso=-1
        if angle_conso>1:
            angle_conso=1
        game.player.essence -= (1-angle_conso)*3
        print(game.player.essence)

    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x>0 and game.player.essence>=0:
        game.player.move_left()
        game.player.move_up()
        game.player.rotate(fonction(game.player.rect.x-50+game.terrain.offset)[1])
        angle_conso = game.player.angle
        if angle_conso < -1:
            angle_conso = -1
        if angle_conso > 1:
            angle_conso = 1
        game.player.essence -= (1 + angle_conso) * 3
        print(game.player.essence)

    p.display.flip()

    for event in p.event.get():
        if event.type == p.QUIT:
            running=False
            p.quit()
        elif event.type == p.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == p.KEYUP:
            game.pressed[event.key] = False

