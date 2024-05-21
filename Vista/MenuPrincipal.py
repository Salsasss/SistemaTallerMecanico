from customtkinter import *
from Controlador import ctrlFunciones
from Vista.FrameNuevoServicio import FrameNuevoServicio
from Vista.FrameServicios import FrameServicios
from Vista.FrameUsuarios import FrameUsuarios

class MenuPrincipal(CTk):
    def __init__(self):
        super().__init__()
        set_appearance_mode("light")

        self.configure(fg_color='white')
        self.title('Sistema de Taller Mecánico')
        self.geometry(f'1000x700+{((self.winfo_screenwidth() - 1000) // 2)}+{((self.winfo_screenheight() - 760) // 2)}')
        self.opciones = []
        self.cont_principal = CTkFrame(self, fg_color='white')
        self.cont_principal.pack(side=RIGHT, fill='both', padx=15, pady=15, expand=True)

    def _accion(self, label, acc, e):
        for lbl in self.opciones:
            lbl.configure(fg_color='blue')
            lbl.configure(text_color='white')
        label.configure(fg_color='white')
        if get_appearance_mode()=='Dark':
            label.configure(text_color='#b3b3b3')
        else:
            label.configure(text_color='black')

        for widget in self.cont_principal.pack_slaves():
            widget.pack_forget()

        if acc==0:
            FrameNuevoServicio(self.cont_principal).pack(fill='both', expand=True)
        elif acc==1:
            FrameServicios(self.cont_principal).pack(fill='both', expand=True)
        elif acc==2:
            FrameUsuarios(self.cont_principal).pack(fill='both', expand=True)

    def _barra_opciones(self):
        barra_opciones = CTkFrame(self, width=250,  fg_color='blue', corner_radius=0)
        barra_opciones.pack(side=LEFT, fill='both', expand=False)

        label_logo = CTkLabel(barra_opciones, image=ctrlFunciones.leer_imagen('../media/logo.jpg', (100, 100)))
        label_logo.grid(row=0, column=0, pady=40)

        opc = ['🚗 Nuevo Servicio', '🔧 Servicios', '👤 Usuarios']
        for i in range(3):
            label = CTkLabel(barra_opciones, width=200, text=opc[i], fg_color='blue', text_color='white', font=('arial', 16, 'bold'), corner_radius=10)
            label.grid(row=i+1, column=0, ipady=15, padx=10)
            label.bind('<Button-1>', lambda event, lbl=label, acc=i: self._accion(lbl, acc, event))
            self.opciones.append(label)

        texto_saludo = CTkLabel(barra_opciones, text="¡Hola, Aaron!", text_color='white', font=('arial', 16, 'bold'))
        texto_saludo.grid(row=5, column=0, sticky=S, pady=240)

    def desplegar(self):
        self._barra_opciones()
        #FrameServicios(self.cont_principal).pack(fill='both', expand=True)
        self.mainloop()

menu = MenuPrincipal()
menu.desplegar()