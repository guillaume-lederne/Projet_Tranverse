import tkinter as tk
from PIL import Image, ImageTk
from Options import affichage_icone
from main import lancer_jeu


def lancer_menu():
    root = tk.Tk()
    root.title("Menu du Jeu")
    root.geometry("1080x720")
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

    btn_jouer_image_path = "image/jouer.jpg"  # Assurez-vous que cette image existe
    try:
        btn_jouer_image = Image.open(btn_jouer_image_path)
        btn_jouer_photo = ImageTk.PhotoImage(btn_jouer_image)
    except FileNotFoundError:
        print(f"Erreur : L'image '{btn_jouer_image_path}' est introuvable.")
        root.destroy()
        exit()

    btn_jouer = tk.Button(root, image=btn_jouer_photo, command=lancer_jeu, borderwidth=-10)
    btn_jouer.place(x=355, y=265)
    root.mainloop()
"""
    btn_option_image_path = "image/options.jpg"
    try:
        btn_option_image = Image.open(btn_option_image_path)
        btn_option_photo = ImageTk.PhotoImage(btn_option_image)
    except FileNotFoundError:
        print(f"Erreur : L'image '{btn_option_image_path}' est introuvable.")
        root.destroy()
        exit()

    btn_option = tk.Button(root, image=btn_option_photo, command=ouvrir_options, borderwidth=0)

    btn_option.place(x=365, y=433)

"""

    
def ouvrir_options():
    print("Ouverture des options...")
    affichage_icone()

if __name__ == "__main__":
    lancer_menu()
