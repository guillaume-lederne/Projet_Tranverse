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
game.player1.terrain=game.terrain.fonction
game.player2.terrain=game.terrain.fonction

running=True

terrain=game.terrain.generer_terrain()
game.player1.rect.x=0
game.player1.rect.y=fonction(0)[0]-40
game.player2.rect.x=960
game.player2.rect.y=fonction(960)[0]-40
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

    screen.blit(game.player1.image,game.player1.rect)
    screen.blit(game.player2.image,game.player2.rect)


    if game.pressed.get(pygame.K_RIGHT)and game.player1.rect.x<960 :
        game.playerjoueur.move_right()
        game.playerjoueur.move_up()
        game.playerjoueur.rotate(fonction(game.player1.rect.x-60+game.terrain.offset)[1])
        game.playerjoueur.conso(1)

    elif game.pressed.get(pygame.K_LEFT) and game.player1.rect.x>0 :
        game.playerjoueur.move_left()
        game.playerjoueur.move_up()
        game.playerjoueur.rotate(fonction(game.player1.rect.x-50+game.terrain.offset)[1])
        game.playerjoueur.conso(2)


    if game.playerjoueur.essence<=0:
        game.tour()

    p.display.flip()

    for event in p.event.get():
        if event.type == p.QUIT:
            running=False
            p.quit()
        elif event.type == p.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == p.KEYUP:
            game.pressed[event.key] = False

