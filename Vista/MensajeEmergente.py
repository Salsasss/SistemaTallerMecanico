from customtkinter import *
from Controlador import ctrlFunciones
from Controlador.ctrlFunciones import *

class MensajeEmergente(CTkToplevel):
    def __init__(self, root, titulo, msg):
        super().__init__(root, fg_color='#dbdbdb')
        self.title(titulo)
        self.geometry(f'+{(self.winfo_screenwidth() // 2)}+{(self.winfo_screenheight() // 2)}')
        self.resizable(False, False)
        self.grab_set()

        self.ans = None
        self.label_imagen = CTkLabel(self, text='')
        self.label_imagen.grid(row=0, column=0, padx=(10, 0), pady=(15, 0))
        CTkLabel(self, text=msg).grid(row=0, column=1, padx=10, pady=(15, 0))

    def mensaje_error(self):
        self.label_imagen.configure(image=ctrlFunciones.leer_imagen('../media/error.png', (50, 50)))
        CTkButton(self, text='OK', fg_color='blue', font=('arial', 14, 'bold'), command=self._cerrar).grid(row=1, column=0, pady=10, columnspan=2)

    def mensaje_correcto(self):
        self.label_imagen.configure(image=ctrlFunciones.leer_imagen('../media/corr.png', (50, 50)))
        boton_ok = CTkButton(self, text='OK', fg_color='#1e8b1e', font=('arial', 14, 'bold'), command=self._cerrar)
        boton_ok.grid(row=1, column=0, pady=10, columnspan=2)
        boton_ok.bind('<Enter>', lambda event: color_fg(event, boton=boton_ok, color='#125412'))
        boton_ok.bind('<Leave>', lambda event: color_fg(event, boton=boton_ok, color='#1e8b1e'))

    def _si(self):
        self.ans = True
        self._cerrar()

    def _no(self):
        self.ans = False
        self._cerrar()

    def mensaje_pregunta(self):
        self.label_imagen.configure(image=ctrlFunciones.leer_imagen('../media/question.png', (50, 40)))

        cont_botones = CTkFrame(self)
        cont_botones.grid(row=1, column=0, padx=5, columnspan=2)

        boton_no = CTkButton(cont_botones, width=100, text='No', fg_color='#b8161b', font=('arial', 14, 'bold'), command=self._no)
        boton_no.grid(row=0, column=0, padx=10, pady=10)
        boton_no.bind('<Enter>', lambda event: color_fg(event, boton=boton_no, color='#891014'))
        boton_no.bind('<Leave>', lambda event: color_fg(event, boton=boton_no, color='#b8161b'))

        boton_si = CTkButton(cont_botones, width=100, text='Si', fg_color='#1e8b1e', font=('arial', 14, 'bold'), command=self._si)
        boton_si.grid(row=0, column=1, padx=10, pady=10)
        boton_si.bind('<Enter>', lambda event: color_fg(event, boton=boton_si, color='#125412'))
        boton_si.bind('<Leave>', lambda event: color_fg(event, boton=boton_si, color='#1e8b1e'))

    def _cerrar(self):
        self.destroy()
