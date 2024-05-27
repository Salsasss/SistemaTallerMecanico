from customtkinter import *
from Controlador import ctrlFunciones

class MensajeEmergente(CTkToplevel):
    def __init__(self, root, titulo, msg):
        super().__init__(root)
        self.title(titulo)
        self.ans = None  # Cambiado de BooleanVar a None

        self.label_imagen = CTkLabel(self, text='')
        self.label_imagen.grid(row=0, column=0, padx=(10, 0), pady=(15, 0))
        CTkLabel(self, text=msg).grid(row=0, column=1, padx=10, pady=(15, 0))

    def mensaje_error(self):
        self.label_imagen.configure(image=ctrlFunciones.leer_imagen('../media/error.png', (50, 50)))
        CTkButton(self, text='OK', fg_color='blue', font=('arial', 14, 'bold'), command=self._cerrar).grid(row=1, column=0, pady=10, columnspan=2)

    def mensaje_correcto(self):
        self.label_imagen.configure(image=ctrlFunciones.leer_imagen('../media/corr.png', (50, 50)))
        CTkButton(self, text='OK', fg_color='blue', font=('arial', 14, 'bold'), command=self._cerrar).grid(row=1, column=0, pady=10, columnspan=2)

    def _si(self):
        self.ans = True
        self._cerrar()

    def _no(self):
        self.ans = False
        self._cerrar()

    def mensaje_pregunta(self):
        self.label_imagen.configure(image=ctrlFunciones.leer_imagen('../media/question.png', (60, 50)))

        cont_botones = CTkFrame(self, fg_color='#dbdbdb')
        cont_botones.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

        CTkButton(cont_botones, width=100, text='No', fg_color='blue', font=('arial', 14, 'bold'), command=self._no).grid(row=0, column=0, padx=10)
        CTkButton(cont_botones, width=100, text='Si', fg_color='blue', font=('arial', 14, 'bold'), command=self._si).grid(row=0, column=1, padx=10)

    def _cerrar(self):
        self.destroy()
