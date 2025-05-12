import pygame
import pygame as p
import game
import random

p.init()

p.display.set_caption('WWI')


game = game.Game()

screen = game.terrain.fenetre

running=True
info_terrain=game.terrain.generer_terrain()
terrain=info_terrain[0]
game.terrain.choix_couleur()
fonction=game.terrrain.fonctions()
while running:

    # Dessin du terrain

    screen.fill(game.terrain.couleur_ciel)
    points = []
    x = 0
    while x < game.terrain.largeur:
        points.append((x, terrain[x]))
        x += 1
    points.append((game.terrain.largeur, game.terrain.hauteur_fenetre))  # Coin inférieur droit
    points.append((0, game.terrain.hauteur_fenetre))  # Coin inférieur gauche
    pygame.draw.polygon(screen, game.terrain.couleur_sol, points)

    screen.blit(game.player.image,game.player.rect)


    if game.pressed.get(pygame.K_RIGHT)and game.player.rect.x<900:
        game.player.move_right()



    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x>0:
        game.player.move_left()



    p.display.flip()

    for event in p.event.get():
        if event.type == p.QUIT:
            running=False
            p.quit()
        elif event.type == p.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == p.KEYUP:
            game.pressed[event.key] = False

