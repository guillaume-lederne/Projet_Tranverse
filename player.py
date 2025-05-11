import pygame as p
import math as m


class Player(p.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.velocity = 1
        self.image =p.image.load('image/tank.png')
        self.rect=self.image.get_rect()
        self.rect.x=100
        self.rect.y=500
        self.image = p.transform.scale(self.image,(100,50))
        self.nb_terrain = 0
        self.orientation=0

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def new_terrain(self,x):
        self.nb_terrain = x

    def move_up(self,x):
        if self.nb_terrain == 1:
            self.rect.y = 50*m.cos(x/90)+44*m.sin(100)+50*m.sin(x/63)+500
            self.orientation= -(5/9)*m.sin(x/90)+50/63*m.cos(x/63)
        if self.nb_terrain == 2:
            self.rect.y = 600*m.cos(x/90)