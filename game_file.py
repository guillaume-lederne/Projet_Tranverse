import pygame as p
import player
import terrain_file
import Tir


class Game:
    def __init__(self):
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

    def tour(self):
        self.playerJoueur.essence = self.playerJoueur.max_essence
        if self.playerJoueur == self.player1:
            self.tour_du_joueur = 2
            self.playerJoueur = self.player2
        elif self.playerJoueur == self.player2:
            self.tour_du_joueur = 1
            self.playerJoueur = self.player1

    def collision(self,rectA, rectB):
        return False


