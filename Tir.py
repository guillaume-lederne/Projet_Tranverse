import pygame
import math

class Missile(pygame.sprite.Sprite):
    def __init__(self, joueur):
        super().__init__()
        self.g = 9.81
        self.vitesse_initiale =50
        self.angle_initial = 45
        self.vitesse = self.vitesse_initiale
        self.angle = self.angle_initial
        self.char_x = 100
        self.char_y = 100
        self.gravite=9.81
        if joueur == 1:
            self.image=pygame.image.load('image/balle_tank_gauche.png')
        if joueur == 1:
            self.image=pygame.image.load('image/balle_tank_droit.png')
        self.rect=self.image.get_rect()



# Fonction pour calculer la trajectoire
    def trajectoire(self,v, angle_deg):
        # Convertir l'angle en radians
        angle_rad = math.radians(angle_deg)

        # Liste des coordonnées du tir
        x_vals = []
        y_vals = []

        t = 0  # Temps initial
        dt = 0.1  # Pas de temps

        while True:
            x = v * math.cos(angle_rad) * t
            y = v * math.sin(angle_rad) * t - 0.5 * self.gravite * t ** 2
            if y < -50 : #valeur arbitraire pour que la trajectoire calcul un point en plus et évite les problèmes de sortie d'écran
                break # Arrêter lorsque le projectile touche le sol
            x_vals.append(x+char_x)
            y_vals.append(char_y - y)  # Inverser l'axe y pour l'affichage (haut/bas)
            t += dt

        return x_vals, y_vals


# Position du char (le point de départ du tir)
char_x= 100
char_y = hauteur - 20 # Position initiale




# Boucle principale du jeu
clock = pygame.time.Clock()
running = True
tir_active = False  # Flag pour savoir si le tir est actif
x_vals, y_vals = [], []  # Initialisation des listes de trajectoire
missile_x, missile_y = -1, -1  # Position initiale du missile hors écran

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Récupérer la position de la souris pour définir l'angle de tir
    souris_x, souris_y = pygame.mouse.get_pos()
    dx = souris_x - char_x
    dy = char_y - souris_y  # Inverser dy pour avoir l'angle correct

    # Calculer l'angle en fonction de la souris
    angle = math.degrees(math.atan2(dy, dx))

    # Gérer la vitesse avec les touches fléchées
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        vitesse += 1  # Augmenter la vitesse
    if keys[pygame.K_DOWN]:
        vitesse = max(1, vitesse - 1)  # Diminuer la vitesse (avec un minimum de 1)

    # Tirer lorsque l'utilisateur appuie sur la barre d'espace
    if keys[pygame.K_SPACE] and not tir_active:
        tir_active = True
        missile_x = char_x
        missile_y = char_y  # Réinitialiser la position du missile
        x_vals, y_vals = trajectoire(vitesse, angle)  # Calculer la trajectoire
        print(f"Tir effectué avec angle {angle:.2f}° et vitesse {vitesse} m/s")


    # Dessiner le char
    pygame.draw.rect(screen, (0, 0, 0), (char_x - 10, char_y - 10, 20, 20))  # Représente le char

    # Dessiner la trajectoire du tir avant le lancement
    if not tir_active:
        x_vals, y_vals = trajectoire(vitesse, angle)  # Recalculer la trajectoire à chaque frame avant le tir
        for i in range(len(x_vals)):
                pygame.draw.circle(screen, (0, 0, 255), (int(x_vals[i] ), int(y_vals[i])), 3)

    # Dessiner le missile (si le tir est actif)
    if tir_active:
        if len(x_vals) > 0:
            # Le missile suit la trajectoire (l'exemple simplifié ici déplace le missile selon les points de la trajectoire)
            missile_x += (x_vals[0] - missile_x)
            missile_y += (y_vals[0] - missile_y)

            dessiner_missile(missile_x, missile_y)

            # Retirer les coordonnées utilisées de la trajectoire pour le missile
            x_vals.pop(0)
            y_vals.pop(0)

        # Vérifier si le missile touche le sol ou sort de l'écran
        if missile_y >= hauteur  or missile_x > largeur or missile_x < -1:
            tir_active = False  # Réinitialiser le tir lorsque le missile touche le sol

    # Afficher l'angle et la vitesse sur l'écran
    font = pygame.font.SysFont(None, 30)
    text = font.render(f"Vitesse: {vitesse} m/s  Angle: {int(angle)}°", True, (0, 0, 0))
    screen.blit(text, (10, 10))
    # Mettre à jour l'affichage
    pygame.display.flip()
    # Limiter le nombre de frames par seconde
    clock.tick(60)

# Quitter Pygame
pygame.quit()