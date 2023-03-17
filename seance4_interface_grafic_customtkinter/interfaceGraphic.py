import os
import sys
import customtkinter
import tkinter


#################################
# creation de classe avec 2 methode 1 pour initialiser 
# et une pour quitter l'application 
#################################

"""
class  Interface(customtkinter.CustomTkinter):
    def __init__(self):
        super().__init__()

        # Ajouter un bouton
        self.bouton = self.add_button(text="Cliquez ici")

        # Configurer le bouton
        self.bouton.config(command=lambda: print("Bouton cliqué !"))

# Afficher la fenêtre
Interface().run()
 """



customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()