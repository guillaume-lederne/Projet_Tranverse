import pygame
import pygame as p
pygame.init()
import game_file
import random
import time as t
fenetre = pygame.display.set_mode((1080, 720))
police1 = pygame.font.Font(None,30)
police2 = pygame.font.Font(None,38)
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


    if game.pressed.get(pygame.K_RIGHT)and game.playerJoueur.rect.x<960 :
        game.playerJoueur.move_right()
        game.playerJoueur.move_up()
        game.playerJoueur.rotate(fonction(game.playerJoueur.rect.x-60+game.terrain.offset)[1])
        game.playerJoueur.conso(1)
        if game.playerJoueur.essence <= 0:
            game.tour()

    elif game.pressed.get(pygame.K_LEFT) and game.playerJoueur.rect.x>0 :
        game.playerJoueur.move_left()
        game.playerJoueur.move_up()
        game.playerJoueur.rotate(fonction(game.playerJoueur.rect.x-50+game.terrain.offset)[1])
        game.playerJoueur.conso(2)
        if game.playerJoueur.essence <= 0:
            game.tour()

    text_essence_1 = police1.render(f"Essence : {round(game.player1.essence/10,1)} L", True,(0,0,0))
    text_essence_2 = police1.render(f"Essence : {round(game.player2.essence / 10, 1)} L", True, (0, 0, 0))
    if game.tour_du_joueur == 1:
        text_tour = police2.render(f"Tour du joueur {1}", True, (0, 0, 0))
    elif game.tour_du_joueur == 2:
        text_tour = police2.render(f"Tour du joueur {2}", True, (0, 0, 0))
    fenetre.blit(text_essence_1,(20,20))
    fenetre.blit(text_essence_2, (900, 20))
    fenetre.blit(text_tour, (430, 20))
    p.display.flip()

    for event in p.event.get():
        if event.type == p.QUIT:
            running=False
            p.quit()
        elif event.type == p.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == p.KEYUP:
            game.pressed[event.key] = False

