from customtkinter import *

class FrameMenuPrincipal(CTkFrame):
    def __init__(self, root, fg_color='red'):
        super().__init__(root)
        set_appearance_mode("light")

        CTkButton(self, width=100, text='Completar Servicio', fg_color='blue', font=('arial', 14, 'bold'), command=self._no).grid(row=0, column=0, padx=10)
