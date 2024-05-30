import subprocess

from customtkinter import *
from Controlador.ctrlFunciones import *
from Vista.FrameCataRefacciones import FrameCataRefacciones
from Vista.FrameClientes import FrameClientes
from Vista.FrameEmpleados import FrameEmpleados
from Vista.FrameNuevoServicio import FrameNuevoServicio
from Vista.FramePagar import FramePagar
from Vista.FrameRefaccionesAdmi import FrameRefaccionesAdmi
from Vista.FrameAutomoviles import FrameAutomoviles

class FrameMenuPrincipal(CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.session_empleado = self.root.session_empleado

        set_appearance_mode("light")
        self.opciones = []

        self.cont_principal = CTkFrame(self, width=750, fg_color='white')
        self.cont_principal.pack(side=RIGHT, fill='both', expand=True)

        self._barra_opciones()

    def cerrar_sesion(self, e):
        self.root.destroy()
        subprocess.run(["python", "VentanaLogin.py"], check=True)

    def _opcion(self, label, acc, e):
        for lbl in self.opciones:
            lbl.configure(fg_color='blue')
            lbl.configure(text_color='white')
        label.configure(fg_color='white')
        label.configure(text_color='black')

        for widget in self.cont_principal.pack_slaves():
            widget.pack_forget()

        if acc==0:
            FrameNuevoServicio(self.cont_principal).pack(fill='both', expand=True)
        elif acc==1:
            FrameClientes(self.cont_principal).pack(padx=10, pady=10, fill='both', expand=True)
        elif acc==2:
            FrameAutomoviles(self.cont_principal).pack(padx=10, pady=10, fill='both', expand=True)
        elif acc==3:
            FrameEmpleados(self.cont_principal).pack(padx=10, pady=10, fill='both', expand=True)
        elif acc==4:
            FramePagar(self.cont_principal).pack(padx=10, pady=10, fill='both', expand=True)
        elif acc==5:
            FrameCataRefacciones(self.cont_principal).pack(padx=10, pady=10, fill='both', expand=True)
        elif acc==6:
            FrameRefaccionesAdmi(self.cont_principal).pack(padx=10, pady=10, fill='both', expand=True)

    def _barra_opciones(self):
        barra_opciones = CTkFrame(self, fg_color='blue', corner_radius=0)
        barra_opciones.pack(side=LEFT, fill='both', expand=False)

        label_logo = CTkLabel(barra_opciones, image=leer_imagen('../media/logo.png', (125, 125)))
        label_logo.grid(row=0, column=0, pady=20)

        opc = ['🚗 Nuevo Servicio', '👤Clientes', '🔧 Automoviles', '👤 Empleados', 'pagar', 'admi', 'admi +']
        for i in range(len(opc)):
            label = CTkLabel(barra_opciones, width=200, text=opc[i], text_color='white', font=('arial', 16, 'bold'), corner_radius=10)
            label.grid(row=i+1, column=0, ipady=15, padx=10)
            label.bind('<Button-1>', lambda event, lbl=label, acc=i: self._opcion(lbl, acc, event))
            self.opciones.append(label)

        texto_saludo = CTkLabel(barra_opciones, text=f'¡Hola, {self.session_empleado['nombre']}!', text_color='white', font=('arial', 16, 'bold'))
        texto_saludo.grid(row=11, column=0, pady=20, sticky=S)

        label_cerrar_sesion = CTkLabel(barra_opciones, text='Cerrar Sesión', text_color='white', font=('arial', 16, 'bold'))
        label_cerrar_sesion.grid(row=12, column=0, sticky=S)
        label_cerrar_sesion.bind('<Enter>', lambda event: color_text(event, boton=label_cerrar_sesion, color='#b8161b'))
        label_cerrar_sesion.bind('<Leave>', lambda event: color_text(event, boton=label_cerrar_sesion, color='white'))
        label_cerrar_sesion.bind('<Button-1>', self.cerrar_sesion)