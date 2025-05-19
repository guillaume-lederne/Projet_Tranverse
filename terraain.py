import pygame
import random
import math

class Terrain:
    def __init__(self):
        self.couleur_sol=None
        self.couleur_ciel=None
        self.hauteur_terrain=450
        self.largeur= 1080
        self.hauteur_fenetre=720
        self.fenetre=pygame.display.set_mode((self.largeur, self.hauteur_fenetre))


    def generer_fonctions_hauteur(self):
        """Génère une liste de fonctions de hauteur."""
        def f1(x):
            return self.hauteur_terrain + 30 * math.sin(x * 0.005)
        def f2(x):
            return self.hauteur_terrain + 50 * math.sin(x * 0.003 + 1)
        def f3(x):
            return self.hauteur_terrain + 40 * math.sin(x * 0.004) + 20 * math.sin(x * 0.008)
        def f4(x):
            return self.hauteur_terrain + 60 * math.sin(x * 0.0025 + 2)
        def f5(x):
            return self.hauteur_terrain + 35 * math.sin(x * 0.004) - 10 * math.cos(x * 0.008)
        def f6(x):
            return self.hauteur_terrain + 45 * math.sin(x * 0.003 + 1.5) + 10 * math.sin(x * 0.006)
        def f7(x):
            return self.hauteur_terrain + 25 * math.sin(x * 0.005) + 25 * math.sin(x * 0.0025)
        def f8(x):
            return self.hauteur_terrain + 55 * math.sin(x * 0.002)
        def f9(x):
            return self.hauteur_terrain + 40 * math.sin(x * 0.003) - 10 * math.sin(x * 0.005)
        def f10(x):
            return self.hauteur_terrain + 30 * math.sin(x * 0.004 + 3) + 15 * math.sin(x * 0.0065)
        return [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]



