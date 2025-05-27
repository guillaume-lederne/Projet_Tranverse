import pygame as p
import math as m
import Tir

class Player(p.sprite.Sprite):

    def __init__(self, joueur):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.max_essence = 1000
        self.essence = 1000
        self.velocity = 1
        if joueur == 1:
            self.image = p.image.load('image/tank.png')
            self.coeur_image = p.image.load('image/5coeurs.png')
            self.coeur_image = p.transform.scale(self.coeur_image, (140, 35))
            self.coeur_rect = self.coeur_image.get_rect()
            self.coeur_rect.x=10
            self.coeur_rect.y = 10
        elif joueur == 2:
            self.image = p.image.load('image/tank2.png')
            self.coeur_image = p.image.load('image/5coeurs.png')
            self.coeur_image = p.transform.scale(self.coeur_image, (140, 35))
            self.coeur_rect = self.coeur_image.get_rect()
            self.coeur_rect.x = 930
            self.coeur_rect.y = 10
        self.image = p.transform.scale(self.image,(100,50))
        self.image_og=self.image
        self.image=self.image_og
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.angle = 0
        self.terrain=None


    def compt_coeur(self):
        if self.health < 80 and self.health > 60:
            self.coeur_image=p.coeur_image.load('image/4coeurs.png')
        elif self.health < 60 and self.health > 40:
            self.coeur_image=p.coeur_image.load('image/3coeurs.png')
        elif self.health < 40 and self.health > 20:
            self.coeur_image=p.coeur_image.load('image/2coeurs.png')
        elif self.health < 20 and self.health > 0:
            self.coeur_image=p.coeur_image.load('image/coeur.png')



    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def rotate(self,pente):
        angle_radians = m.atan(pente)
        self.angle = angle_radians
        self.image = p.transform.rotate(self.image_og, m.degrees(-angle_radians))
        self.rect = self.image.get_rect(center=self.rect.center)

    def move_up(self):
        self.rect.y = self.terrain(self.rect.x)[0]-45

    def conso(self,sens):
        angle_conso = self.angle
        if angle_conso < -1:
            angle_conso = -1
        if angle_conso > 1:
            angle_conso = 1
        if sens == 1:
            self.essence -= (1 - angle_conso) * 3
        elif sens == 2:
            self.essence -= (1 + angle_conso) * 3