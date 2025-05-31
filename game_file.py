import pygame as p
import pygame.image

import player
import terrain_file
import Tir
import time as t


class Game:
    def __init__(self):
        self.timer = 9.9
        self.time_start = t.time()
        self.largeur = 1080
        self.hauteur = 720
        self.player1 = player.Player(1)
        self.player2 = player.Player(2)
        self.missile = Tir.Missile()
        self.playerJoueur=self.player1
        self.pressed = {}
        self.terrain=terrain_file.Terrain()
        self.fonction=self.terrain.fonction
        self.tour_du_joueur = 1

        self.img_explosion = pygame.image.load('image/Explosion_1.png')
        self.img_explosion = p.transform.scale(self.img_explosion, (90,90))
        self.img_rect = self.img_explosion.get_rect()
        self.explosion_timer = 0


    def tour(self):
        self.playerJoueur.essence = self.playerJoueur.max_essence
        if self.playerJoueur == self.player1:
            self.tour_du_joueur = 2
            self.playerJoueur = self.player2
        elif self.playerJoueur == self.player2:
            self.tour_du_joueur = 1
            self.playerJoueur = self.player1

    def collision(self,rectA, rectB,screen):
        if rectB.x + 10 < rectA.x:
            return False

        if rectB.y+10 < rectA.y:
            return False

        if rectB.x > rectA.x+100:
            return False

        if rectB.y > rectA.y+50:
            return False

        self.missile.tir_active = False
        self.time_start = t.time()

        self.explosion_timer = t.time()+0.75
        if self.playerJoueur == self.player1:
            self.img_rect.x = self.player2.rect.x
            self.img_rect.y = self.player2.rect.y
        else:
            self.img_rect.x = self.player1.rect.x
            self.img_rect.y = self.player1.rect.y

        self.missile.missile_x, self.missile.missile_y = -1, -1
        self.tour()
        return True

