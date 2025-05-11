import pygame as p
import player
import terraain

class Game:
    def __init__(self):
        self.player = player.Player()
        self.pressed = {}
        self.terrain = terraain.Terrain()
