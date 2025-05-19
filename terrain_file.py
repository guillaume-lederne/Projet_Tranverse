import pygame
import random
import math as m

class Terrain:
    def __init__(self):
        self.couleur_sol = None
        self.couleur_ciel = None
        self.hauteur_terrain=450
        self.largeur= 1080
        self.hauteur_fenetre=720
        self.fenetre=pygame.display.set_mode((self.largeur, self.hauteur_fenetre))
        self.fonction=None


    def choix_couleur(self):
        vert = (34, 139, 34)
        marron = (139, 69, 19)
        bleu = (135, 206, 235)
        bleu_moins_bleu = (160, 180, 200)

        couleurs_sol = [vert, marron]
        couleurs_ciel = [bleu, bleu_moins_bleu]
        self.couleur_ciel = random.choice(couleurs_ciel)
        self.couleur_sol = random.choice(couleurs_sol)


    def fonctions(self):
        def f1(x):
            return self.hauteur_terrain + 40 * m.sin(x * 0.005),40*0.005*m.cos(x * 0.005)#+image du terrain DESSINEE PAR CLEMENT
        def f2(x):
            return self.hauteur_terrain + 50*m.cos(x/90)+44*m.sin(100)+50*m.sin(x/63),-(5/9)*m.sin(x/90)+44/100*m.cos(x/100)+50/63*m.cos(x/63)#+image du terrain DESSINEE PAR CLEMENT
        # def f3(x):
        #     return self.hauteur_terrain + 300*m.cos(x/30),-10*m.sin(x/30)
        def f4(x):
            return self.hauteur_terrain + 50*m.sin(x/49)+42*m.cos(x/42-400),50/49*m.cos(x/49)-m.sin(x/49)
        def f5(x):
            return self.hauteur_terrain + 50*m.sin(x/49)+42*m.cos(x/42-400)+46*m.sin(x/80),50/49*m.cos(x/49)-m.sin(x/49)+46/80*m.sin(x/80)
        def f6(x):
            return self.hauteur_terrain + 60*m.cos(x*0.004)+14*m.sin(x/52),-60*0.004*m.sin(x*0.004)+14/52*m.cos(x/52)
        self.fonction=random.choice([f1,f2,f4,f5,f6])

    def generer_terrain(self):
        terrain = [0] * self.largeur
        for x in range(self.largeur):
            resultat = self.fonction(x)[0]
            if isinstance(resultat, tuple):
                terrain[x] = resultat[0]
            else:
                terrain[x] = resultat
        return terrain
