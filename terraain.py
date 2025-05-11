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
        self.x = 0
        self.fenetre=pygame.display.set_mode((self.largeur, self.hauteur_fenetre))

    def choix_couleur(self):
        vert = (34, 139, 34)
        marron = (139, 69, 19)
        bleu = (135, 206, 235)
        bleu_moins_bleu = (160, 180, 200)

        couleurs_sol = [vert, marron]
        couleurs_ciel = [bleu, bleu_moins_bleu]
        self.couleur_ciel = random.choice(couleurs_ciel)
        self.couleur_sol = random.choice(couleurs_sol)

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


    def generer_terrain(self):
        terrain = [0] * self.largeur
        nb_segments = 5
        largeur_segment = self.largeur // nb_segments
        fonction=self.generer_fonctions_hauteur()
        liste_segment=[]
        liste_dep_arr=[]
        for i in range(nb_segments):
            fonction_final = random.choice(fonction)
            liste_segment.append(fonction_final)
            debut_x = i * largeur_segment
            fin_x = (i + 1) * largeur_segment if i < nb_segments - 1 else self.largeur

            local_x=0
            liste_dep_arr.append((debut_x,fin_x))
            for x in range(debut_x, fin_x):
                terrain[x] = fonction_final(local_x)
                local_x+= 1

        # Lissage plus doux pour encore plus d'arrondi
        terrain_lisse = []
        taille_fenetre = 20
        for i in range(self.largeur):
            debut = max(0, i - taille_fenetre)
            fin = min(self.largeur, i + taille_fenetre + 1)
            total = sum(terrain[debut:fin])
            nb = fin - debut
            moyenne = total / nb
            terrain_lisse.append(moyenne)

        return terrain_lisse,liste_segment,liste_dep_arr
