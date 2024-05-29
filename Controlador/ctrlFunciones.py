from customtkinter import CTkImage
from PIL import Image

def leer_imagen(path, size):
        return CTkImage(light_image=Image.open(path), size=size)

def color(e, boton, color):
        boton.configure(fg_color=color)
