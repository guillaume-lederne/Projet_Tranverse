import pygame as p
import player
import terrain_file

class Game:
    def __init__(self):
        self.player1 = player.Player(1)
        self.player2 = player.Player(2)
        self.playerJoueur=self.player1
        self.pressed = {}
        self.terrain=terrain_file.Terrain()
        self.fonction=self.terrain.fonction

    def tour(self):
        self.playerJoueur.essence = self.playerJoueur.max_essence
        if self.playerJoueur == self.player1:
            self.playerJoueur = self.player2
        elif self.playerJoueur == self.player2:
            self.playerJoueur = self.player1




