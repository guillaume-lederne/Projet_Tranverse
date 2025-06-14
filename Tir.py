import pygame
import math
import time


class Missile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.g = 9.81
        self.terrain = None
        self.vitesse_initiale =50
        self.angle_initial = 45
        self.vitesse = self.vitesse_initiale
        self.angle = self.angle_initial
        self.char_x = 100
        self.char_y = 100
        self.gravite=9.81
        self.x_vals, self.y_vals = [], []
        self.tir_active = False
        self.missile_x, self.missile_y = -1, -1
        self.image_right=pygame.image.load('image/balle_tank_gauche.png')
        self.image_right = pygame.transform.scale(self.image_right, (35, 35))
        self.image_left=pygame.image.load('image/balle_tank_droit.png')
        self.image_left = pygame.transform.scale(self.image_left, (35, 35))
        self.image = self.image_right
        self.rect=self.image.get_rect()
        self.dx = 0
        self.dy = 0
        self.shoot_delay = 0


    def trajectoire(self,v, angle_deg,hauteur):
        calc_trajectoire = True
        angle_rad = math.radians(angle_deg)

        x_vals = []
        y_vals = []

        t = 0  # Temps initial
        dt = 0.1  # Pas de temps
        y = v * math.sin(angle_rad) * t - 0.5 * self.gravite * t ** 2
        while not y < -hauteur :
            x = v * math.cos(angle_rad) * t
            y = v * math.sin(angle_rad) * t - 0.5 * self.gravite * t ** 2
            x_vals.append(x+self.char_x)
            y_vals.append(self.char_y - y)  # Inverser l'axe y pour l'affichage (haut/bas)
            t += dt
        return x_vals, y_vals

    def dessiner_missile(self,screen,joueur):
        if self.char_x < self.missile_x:
            self.image = self.image_right
            screen.blit(self.image, self.rect)
        else:
            self.image = self.image_left
            screen.blit(self.image, self.rect)

    def dessiner_data(self,screen):
        font = pygame.font.SysFont(None, 30)
        text = font.render(f"Vitesse: {self.vitesse} m/s  Angle: {int(self.angle)}°", True, (0, 0, 0))
        screen.blit(text, (10, 10))

    def update(self,hauteur):
        souris_x, souris_y = pygame.mouse.get_pos()
        dx = souris_x - self.char_x
        dy = self.char_y - souris_y

        self.angle = math.degrees(math.atan2(dy, dx))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.vitesse = min(100, self.vitesse+1)
        if keys[pygame.K_DOWN]:
            self.vitesse = max(1, self.vitesse - 1)
        if keys[pygame.K_SPACE] and not self.tir_active and time.time() > self.shoot_delay:
            self.shoot_delay = time.time() + 1
            self.tir_active = True
            self.missile_x = self.char_x
            self.rect.x = self.missile_x

            self.missile_y = self.char_y  # Réinitialiser la position du missile
            self.rect.y = self.missile_y
            self.x_vals, self.y_vals = self.trajectoire(self.vitesse, self.angle,hauteur)

    def afficher_trajectoire(self,screen,hauteur):
        count = 50
        if not self.tir_active:
            x_vals, y_vals = self.trajectoire(self.vitesse, self.angle,hauteur)  # Recalculer la trajectoire à chaque frame avant le tir
            for i in range(len(x_vals)):
                if count>1:
                    count -=1
                    pygame.draw.circle(screen, (0,0,255), (int(x_vals[i]+5 ), int(y_vals[i]+20)), 3)

    def tirer(self,screen,joueur):
        if self.tir_active:
            if len(self.x_vals) > 0:
                self.missile_x += (self.x_vals[0] - self.missile_x)
                self.missile_y += (self.y_vals[0] - self.missile_y)
                self.rect.x = self.missile_x
                self.rect.y = self.missile_y

                self.dessiner_missile(screen,joueur)

                self.x_vals.pop(0)
                self.y_vals.pop(0)


