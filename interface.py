import pygame
pygame.init()
from tkinter import *
master = Tk()
import tkinter as tk
from PIL import Image, ImageTk

def lancer_jeu():
    print("Lancement du jeu...")

def ouvrir_options():
    print("Ouverture des options...")

# Création de la fenêtre
root = tk.Tk()
root.title("Menu du Jeu")
root.geometry("1184x672")
root.resizable(False, False)

# Charger l'image depuis un fichier existant
image_path = "asset/Image_Menu.jpeg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# Créer un label avec l'image de fond
background_label = tk.Label(root, image=photo)
background_label.image = photo  # 🔥 Ne surtout pas oublier cette ligne
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Boutons
btn_jouer = tk.Button(root, text="Jouer", command=lancer_jeu, font=("Helvetica", 14, "bold"), bg="#d9b44a")
btn_options = tk.Button(root, text="Options", command=ouvrir_options, font=("Helvetica", 14, "bold"), bg="#d9b44a")

# Positionnement des boutons (ajuste à ton image)
btn_jouer.place(x=510, y=300, width=160, height=50)
btn_options.place(x=510, y=380, width=160, height=50)

# Lancement de la boucle
root.mainloop()

