import pygame as p
import math as m



class Player(p.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.velocity = 1
        self.image =p.image.load('image/tank.png')
        self.image = p.transform.scale(self.image,(100,50))
        self.image_og=self.image
        self.image=self.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 440

        self.terrain=None



    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def rotate(self,pente):
        """Fait pivoter l'objet autour de son centre."""
        angle_radians = m.atan(pente)
        self.image = p.transform.rotate(self.image_og, m.degrees(-angle_radians))
        self.rect = self.image.get_rect(center=self.rect.center)

    def move_up(self):
        self.rect.y = self.terrain(self.rect.x)[0]-40