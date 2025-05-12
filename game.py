import pygame as p
import player
import terraain
import terrain
class Game:
    def __init__(self):
        self.player = player.Player()
        self.pressed = {}
        self.terrain = terraain.Terrain()
        self.terrrain=terrain.Terrain()
