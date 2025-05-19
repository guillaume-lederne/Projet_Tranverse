import pygame as p
import player
import terrain_file

class Game:
    def __init__(self):
        self.tour_du_joueur = 1
        self.player1 = player.Player(1)
        self.player2 = player.Player(2)
        self.playerjoueur=self.player1
        self.pressed = {}
        self.terrain=terrain_file.Terrain()
        self.fonction=self.terrain.fonction

    def tour(self):
        self.playerjoueur.essence = self.playerjoueur.max_essence
        if self.playerjoueur == self.player1:
            self.tour_du_joueur = 2
            self.playerjoueur = self.player2
        elif self.playerjoueur == self.player2:
            self.tour_du_joueur = 1
            self.playerjoueur = self.player1




