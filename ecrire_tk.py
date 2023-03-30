import tkinter as tk
from tkinter import *
from tkinter.messagebox import *

fenetre = tk.Tk()

def change_name():
    if var.get():
        label_name.config(text=f"Name : {value.get()}")

def change_age():
    if var.get():
        label_age.config(text=f"Age : {value.get()}")

canvas = Canvas(fenetre, width=150, height=25, background='White')

txt = canvas.create_text(75, 15, text="Mon Profil:", font="Arial 16 italic", fill="Black")
canvas.pack()

label_name = tk.Label(fenetre, text = "Name :", bg="black", fg = 'white', font="Arial", width = 12)
label_name.pack()
label_age = tk.Label(fenetre, text = "Age :", bg="black", fg = 'white', font="Arial", width = 12)
label_age.pack()

name_button = tk.Button(fenetre, text = "Modifier Le Nom", font="Arial", command = change_name)
name_button.pack()
age_button = tk.Button(fenetre, text = "Modifier L'age", font="Arial", command = change_age)
age_button.pack()
bouton_quit = tk.Button(fenetre, text = "Fermer", command = fenetre.quit, bg="red", fg = 'white', font="Arial 16 italic")
bouton_quit.pack()

value = tk.StringVar()
value.set("Modif Infos:")

var = tk.BooleanVar()
checkbox = tk.Checkbutton(fenetre, text="Débloquer saisie :", font="Arial 16 italic", variable = var)
checkbox.pack()

entree = tk.Entry(fenetre, textvariable = value, width = 20, font="Arial 16 italic")
entree.pack()

fenetre.mainloop()

# 2 ligne qui affiche une info different genre nom et age
# 2 bouttons qui change le nom et l'autre l'age
# 1 zone de texte qui permet d'ecrire soit le nom soit l'age