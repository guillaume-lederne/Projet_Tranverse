import tkinter as tk
from tkinter import Toplevel, Label, Button
from PIL import Image, ImageTk

def affichage_icone():
    def selection_tank(tank_name):
        print(f"Vous avez sélectionné : {tank_name}")
        selection_window.destroy()  # Ferme la fenêtre après la sélection

    # Create a new window
    selection_window = Toplevel()
    selection_window.title("Choix du Tank")
    selection_window.geometry("400x300")

    # Tank image paths
    tank1_path = "image/tank_rouge.png"
    tank2_path = "image/tank_vert.png."

    taille_image=(100,100)
    # Load and display Tank 1
    try:
        tank1_image = Image.open(tank1_path).resize(taille_image)
        tank1_photo = ImageTk.PhotoImage(tank1_image)
        btn_tank1 = Button(selection_window, image=tank1_photo, command=lambda: selection_tank("Tank Rouge"), borderwidth=0)
        btn_tank1.image = tank1_photo
        btn_tank1.pack(side="left", padx=20, pady=20)
    except FileNotFoundError:
        print(f"Erreur : L'image '{tank1_path}' est introuvable.")

    # Load and display Tank 2
    try:
        tank2_image = Image.open(tank2_path).resize(taille_image)
        tank2_photo = ImageTk.PhotoImage(tank2_image)
        btn_tank2 = Button(selection_window, image=tank2_photo, command=lambda: selection_tank("Tank Vert"), borderwidth=0)
        btn_tank2.image = tank2_photo
        btn_tank2.pack(side="right", padx=20, pady=20)
    except FileNotFoundError:
        print(f"Erreur : L'image '{tank2_path}' est introuvable.")