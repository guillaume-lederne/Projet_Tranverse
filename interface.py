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

# Chargement de l'image de fond
bg_image = Image.open("Image_Menu.jpeg")
bg_photo = ImageTk.PhotoImage(bg_image)

# Canvas pour afficher l'image de fond
canvas = tk.Canvas(root, width=1184, height=672)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Ajout des boutons (positions ajustées à la main)
btn_jouer = tk.Button(root, text="Jouer", command=lancer_jeu, font=("Helvetica", 14, "bold"), bg="#d9b44a")
btn_options = tk.Button(root, text="Options", command=ouvrir_options, font=("Helvetica", 14, "bold"), bg="#d9b44a")

# Positionnement sur le Canvas (ajuste selon l’image)
canvas.create_window(592, 310, window=btn_jouer)    # Coordonnée x, y centrée sur bouton Jouer
canvas.create_window(592, 390, window=btn_options)  # Coordonnée x, y centrée sur bouton Options

root.mainloop()
