from customtkinter import CTkImage
from PIL import Image

def leer_imagen(path, size):
        return CTkImage(light_image=Image.open(path), size=size)

def color_fg(e, boton, color):
        boton.configure(fg_color=color)

def color_text(e, boton, color):
        boton.configure(text_color=color)