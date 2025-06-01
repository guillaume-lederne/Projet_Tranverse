import pygame
import pygame as p
import game_file
import random
import time as t




def lancer_jeu():
    p.init()
    p.display.set_caption('WWIII')

    game = game_file.Game()
    fenetre = p.display.set_mode((game.largeur, game.hauteur))



    police1 = pygame.font.Font(None,30)
    police2 = pygame.font.Font(None,38)


    screen = game.terrain.fenetre
    game.terrain.fonctions()
    fonction=game.terrain.fonction
    game.player1.terrain=game.terrain.fonction
    game.player2.terrain=game.terrain.fonction
    game.missile.terrain=game.terrain.fonction

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
        screen.blit(game.player1.coeur_image,game.player1.coeur_rect)
        screen.blit(game.player2.coeur_image, game.player2.coeur_rect)

        game.player1.compt_coeur()
        game.player2.compt_coeur()

        if game.pressed.get(pygame.K_RIGHT)and game.playerJoueur.rect.x<960 and game.playerJoueur.essence>0 :
            game.playerJoueur.move_right()
            game.playerJoueur.move_up()
            game.playerJoueur.rotate(fonction(game.playerJoueur.rect.x-60+game.terrain.offset)[1])
            game.playerJoueur.conso(1)
    #        if game.playerJoueur.essence <= 0:
    #            game.tour()

        elif game.pressed.get(pygame.K_LEFT) and game.playerJoueur.rect.x>0 and game.playerJoueur.essence>0:
            game.playerJoueur.move_left()
            game.playerJoueur.move_up()
            game.playerJoueur.rotate(fonction(game.playerJoueur.rect.x-50+game.terrain.offset)[1])
            game.playerJoueur.conso(2)
    #        if game.playerJoueur.essence <= 0:
    #           game.tour()
        game.missile.char_x = game.playerJoueur.rect.x+50
        game.missile.char_y = game.playerJoueur.rect.y
        game.missile.update(game.hauteur)
        game.missile.afficher_trajectoire(screen,game.hauteur)
        game.missile.tirer(game.hauteur,game.largeur,screen)
        if game.tour_du_joueur == 1 and game.missile.tir_active:
            if game.collision(game.player2.rect, game.missile.rect,screen):
                game.player2.health -= 20
                game.missile.tir_active = False
                if game.player2.health==0:
                    game.a_gagne_j1=True
                    running=False
                    image_fin = pygame.image.load("image/gray_wins.png")
                    image_fin = pygame.transform.scale(image_fin, (game.largeur, game.hauteur))
                    fenetre.blit(image_fin, (0, 0))
                    pygame.display.flip()
                    attente = True
                    while attente:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                exit()
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                    lancer_jeu()  # Relance le jeu
                                    return
                                elif event.key == pygame.K_ESCAPE:
                                    pygame.quit()
                                    exit()
        elif game.tour_du_joueur == 2 and game.missile.tir_active:
            if game.collision(game.player1.rect,game.missile.rect,screen):
                game.player1.health -= 20
                game.missile.tir_active = False
                if game.player1.health==0:
                    game.a_gagne_j2=True
                    running=False
                    image_fin = pygame.image.load("image/red_wins.png")
                    image_fin = pygame.transform.scale(image_fin, (game.largeur, game.hauteur))
                    fenetre.blit(image_fin, (0, 0))
                    pygame.display.flip()
                    attente = True
                    while attente:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                exit()
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                    lancer_jeu()  # Relance le jeu
                                    return
                                elif event.key == pygame.K_ESCAPE:
                                    pygame.quit()
                                    exit()
        if (game.missile.rect.y >= game.hauteur or game.missile.rect.x > game.largeur or game.missile.rect.x < 0 or game.missile.rect.y > game.missile.terrain(game.missile.rect.x)[0])and game.missile.tir_active == True:
            game.missile.tir_active = False
            game.time_start = t.time()
            game.tour()

        if t.time() > game.time_start + game.timer:
            game.time_start = t.time()
            if not game.missile.tir_active:
                game.tour()
        text_essence_1 = police1.render(f"Essence : {round(game.player1.essence/10,1)} L", True,(0,0,0))
        text_essence_2 = police1.render(f"Essence : {round(game.player2.essence / 10, 1)} L", True, (0, 0, 0))
        text_timer = police1.render(f"Il vous reste : {round(game.time_start-t.time()+game.timer, 1)} s pour tirer", True, (255, 0, 0))
        if game.tour_du_joueur == 1:
            text_tour = police2.render(f"Tour du joueur {1}", True, (0, 0, 0))
        elif game.tour_du_joueur == 2:
            text_tour = police2.render(f"Tour du joueur {2}", True, (0, 0, 0))
        fenetre.blit(text_essence_1,(20,60))
        fenetre.blit(text_essence_2, (900, 60))
        fenetre.blit(text_tour, (430, 20))
        fenetre.blit(text_timer, (400, 45))
        p.display.flip()


        for event in p.event.get():
            if event.type == p.QUIT:
                running=False
                p.quit()
            elif event.type == p.KEYDOWN:
                game.pressed[event.key] = True
            elif event.type == p.KEYUP:
                game.pressed[event.key] = False



if __name__ == '__main__':
    lancer_jeu()