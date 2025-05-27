import tkinter as tk
from tkinter import Toplevel, Label, Button
from PIL import Image, ImageTk

from tkinter import *
from PIL import Image, ImageTk

from tkinter import *
from PIL import Image, ImageTk

def affichage_icone():
    def selection_tank(tank_name):
        print(f"Vous avez sélectionné : {tank_name}")
        selection_window.destroy()

    selection_window = Toplevel()
    selection_window.title("Choix du Tank")
    selection_window.geometry("900x600")

    try:
        fond_image = Image.open("image/Image_Menu_option.png").resize((900, 600))
        fond_photo = ImageTk.PhotoImage(fond_image)
        background = Label(selection_window, image=fond_photo)
        background.image = fond_photo
        background.place(x=0, y=0, relwidth=1, relheight=1)
    except FileNotFoundError:
        print("Erreur : L'image de fond est introuvable.")

    label_texte = Label(selection_window, text="Choisissez votre équipe :", font=("Helvetica", 24, "bold"), bg="white", fg="black")
    label_texte.place(relx=0.5, y=50, anchor="center")

    label_rouge = Label(selection_window, text="Équipe rouge", font=("Helvetica", 16, "bold"), bg="white", fg="red")
    label_rouge.place(relx=0.3, y=100, anchor="center")

    label_verte = Label(selection_window, text="Équipe verte", font=("Helvetica", 16, "bold"), bg="white", fg="green")
    label_verte.place(relx=0.7, y=100, anchor="center")

    tank1_path = "image/logo_rouge_tank.png"
    tank2_path = "image/logo_tank_vert.png"
    taille_image = (150, 150)

    try:
        tank1_image = Image.open(tank1_path).convert("RGBA").resize(taille_image)
        tank1_photo = ImageTk.PhotoImage(tank1_image)
        btn_tank1 = Button(selection_window, image=tank1_photo, command=lambda: selection_tank("Tank Rouge"),
                           borderwidth=0, bg='white', highlightthickness=0)
        btn_tank1.image = tank1_photo
        btn_tank1.place(relx=0.3, y=200, anchor="center")
    except FileNotFoundError:
        print(f"Erreur : L'image '{tank1_path}' est introuvable.")

    try:
        tank2_image = Image.open(tank2_path).convert("RGBA").resize(taille_image)
        tank2_photo = ImageTk.PhotoImage(tank2_image)
        btn_tank2 = Button(selection_window, image=tank2_photo, command=lambda: selection_tank("Tank Vert"),
                           borderwidth=0, bg='white', highlightthickness=0)
        btn_tank2.image = tank2_photo
        btn_tank2.place(relx=0.7, y=200, anchor="center")
    except FileNotFoundError:
        print(f"Erreur : L'image '{tank2_path}' est introuvable.")
