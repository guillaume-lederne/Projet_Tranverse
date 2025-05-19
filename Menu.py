import tkinter as tk
from PIL import Image, ImageTk
from Options import affichage_icone

def lancer_jeu():
    print("Lancement du jeu...")

def ouvrir_options():
    print("Ouverture des options...")
    affichage_icone()


root = tk.Tk()
root.title("Menu du Jeu")
root.geometry("1184x672")
root.resizable(False, False)

image_path = "image/Image_Menu.jpeg"
try:
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
except FileNotFoundError:
    print(f"Erreur : L'image '{image_path}' est introuvable.")
    root.destroy()
    exit()

background = tk.Label(root, image=photo)
background.image = photo
background.place(x=0, y=0, relwidth=1, relheight=1)


btn_jouer_image_path = "image/jouer_transparent.png"  # Assurez-vous que cette image existe
try:
    btn_jouer_image = Image.open(btn_jouer_image_path)
    btn_jouer_photo = ImageTk.PhotoImage(btn_jouer_image)
except FileNotFoundError:
    print(f"Erreur : L'image '{btn_jouer_image_path}' est introuvable.")
    root.destroy()
    exit()

btn_jouer = tk.Button(root, image=btn_jouer_photo, command=lancer_jeu, borderwidth=0)
btn_jouer.image = btn_jouer_photo
btn_jouer.place(x=510, y=287, width=160, height=50)

btn_option_image_path = "image/option_transparent.png"
try:
    btn_option_image = Image.open(btn_option_image_path)
    btn_option_photo = ImageTk.PhotoImage(btn_option_image)
except FileNotFoundError:
    print(f"Erreur : L'image '{btn_option_image_path}' est introuvable.")
    root.destroy()
    exit()

btn_option = tk.Button(root, image=btn_option_photo, command=ouvrir_options, borderwidth=0)
btn_option.image = btn_option_photo
btn_option.place(x=510, y=450, width=160, height=50)


root.mainloop()


