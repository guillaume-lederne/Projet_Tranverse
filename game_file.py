import pygame as p
import player
import terrain_file

class Game:
    def __init__(self):
        self.player = player.Player()
        self.pressed = {}
        self.terrain=terrain_file.Terrain()
        self.fonction=self.terrain.fonction


