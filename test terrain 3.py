import pygame
import random
import math as m

pygame.init()

# Constantes
largeur, hauteur_fenetre = 1080, 720
hauteur = 450

# Couleurs
vert = (34, 139, 34)
marron = (139, 69, 19)
bleu = (135, 206, 235)
bleu_moins_bleu = (160, 180 ,200)
couleurs_sol = [vert, marron]
couleurs_ciel = [bleu, bleu_moins_bleu]
ciel = random.choice(couleurs_ciel)
sol = random.choice(couleurs_sol)


# t'ouvre la fenetre pr le terrain la
fenetre = pygame.display.set_mode((largeur, hauteur_fenetre))
pygame.display.set_caption("Terrain de Tank")

# la tu choisit une fonctions entre les 6 et tt
def f1(x): return hauteur + 40 * m.sin(x * 0.005), 40 * 0.005 * m.cos(x * 0.005)
def f2(x): return hauteur + 50 * m.cos(x / 90) + 44 * m.sin(100) + 50 * m.sin(x / 63), -(5 / 9) * m.sin(x / 90) + 44 / 100 * m.cos(x / 100) + 50 / 63 * m.cos(x / 63)
def f3(x): return hauteur + 300 * m.cos(x / 30), -10 * m.sin(x / 30)
def f4(x): return hauteur + 50 * m.sin(x / 49) + 42 * m.cos(x / 42 - 400) + 46 * m.sin(x / 80), 50 / 49 * m.cos(x / 49) - m.sin(x / 49) + 46 / 80 * m.sin(x / 80)
def f5(x): return hauteur + 50 * m.sin(x / 49) + 42 * m.cos(x / 42 - 400), 50 / 49 * m.cos(x / 49) - m.sin(x / 49)
def f6(x): return hauteur + 60 * m.cos(x * 0.004) + 14 * m.sin(x / 52), -60 * 0.004 * m.sin(x * 0.004) + 14 / 52 * m.cos(x / 52)

fonctions_a_choisir = [f1, f2, f3, f4, f5, f6]

# bam tu crées le terrain
def generer_terrain():
    terrain = [0] * largeur
    fonction_final = random.choice(fonctions_a_choisir)

    for x in range(largeur):
        resultat = fonction_final(x)
        if isinstance(resultat, tuple):
            terrain[x] = resultat[0]
        else:
            terrain[x] = resultat
    return terrain

terrain = generer_terrain()

# Bouquet final avec tt
jeu_actif = True
while jeu_actif:
    fenetre.fill(ciel)

    # Dessin en mode picasso
    points = []
    x = 0
    while x < largeur:
        points.append((x, terrain[x]))
        x += 1
    points.append((largeur, hauteur_fenetre))
    points.append((0, hauteur_fenetre))
    pygame.draw.polygon(fenetre, sol, points)
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            jeu_actif = False

    pygame.display.flip()

pygame.quit()
