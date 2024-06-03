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
from PIL import Image, ImageTk


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
        self.cargar_pantalla_principal()

    def cargar_pantalla_principal(self):
        self.background_image("../media/principal.png")
        self.welcome()
        self.add_botones()

    def background_image(self, image_path):
        image = Image.open(image_path)
        ctk_image = CTkImage(light_image=image, size=(955, 685))

        self.background_label = CTkLabel(self.cont_principal, image=ctk_image, text='')
        self.background_label.pack(padx=10, pady=10, fill='both', expand=True)

    def welcome(self):
        welcome_label = CTkLabel(self.cont_principal, text=f"¡BIENVENIDO {self.session_empleado["nombre"]}!", font=('helvetica', 30, 'bold'), fg_color='white')
        welcome_label.place(x=100, y=50)

    def add_botones(self):
        button1_image = CTkImage(light_image=Image.open("../media/agregar-usuario.png"), size=(110, 110))
        button2_image = CTkImage(light_image=Image.open("../media/carpeta.png"), size=(110, 110))
        button3_image = CTkImage(light_image=Image.open("../media/reporte.png"), size=(110, 110))

        button1 = CTkLabel(self.cont_principal, image=button1_image, text='')
        button2 = CTkLabel(self.cont_principal, image=button2_image, text='')
        button3 = CTkLabel(self.cont_principal, image=button3_image, text='')

        label1 = CTkLabel(self.cont_principal, text="EMPLEADOS", font=('helvetica', 12))
        label2 = CTkLabel(self.cont_principal, text="AGREGAR REFACCIONES", font=('helvetica', 12))
        label3 = CTkLabel(self.cont_principal, text="REPORTES", font=('helvetica', 12))

        button1.place(x=60, y=200)
        button2.place(x=270, y=200)
        button3.place(x=50, y=370)

        label1.place(x=50, y=310)
        label2.place(x=250, y=310)
        label3.place(x=70, y=480)

        button1.bind('<Button-1>', lambda event: self.button1_action())
        button2.bind('<Button-1>', lambda event: self.button2_action())
        button3.bind('<Button-1>', lambda event: self.button3_action())

    def button1_action(self):
        print("Boton 1")

    def button2_action(self):
        print("Boton 2")

    def button3_action(self):
        print("Boton 3")

    def cerrar_sesion(self, e):
        self.root.destroy()
        subprocess.run(["python", "VentanaLogin.py"], check=True)

    def _opcion(self, label, acc, e):
        for lbl in self.opciones:
            lbl.configure(fg_color='blue')
            lbl.configure(text_color='white')
        label.configure(fg_color='white')
        label.configure(text_color='black')

        # Vaciando el contenedor principal
        for widget in self.cont_principal.pack_slaves():
            widget.pack_forget()

        if acc == 0:
            FrameNuevoServicio(self.cont_principal).pack(fill='both', expand=True)
        elif acc == 1:
            FrameClientes(self.cont_principal).pack(padx=10, pady=10, fill='both', expand=True)
        elif acc == 2:
            FrameAutomoviles(self.cont_principal).pack(padx=10, pady=10, fill='both', expand=True)
        elif acc == 3:
            FrameEmpleados(self.cont_principal).pack(padx=10, pady=10, fill='both', expand=True)
        elif acc == 4:
            FramePagar(self.cont_principal).pack(padx=10, pady=10, fill='both', expand=True)
        elif acc == 5:
            FrameRefaccionesAdmi(self.cont_principal).pack(padx=10, pady=10, fill='both', expand=True)

    def _barra_opciones(self):
        def pantalla_principal(e):
            # Vaciando el contenedor principal
            for widget in self.cont_principal.pack_slaves():
                widget.pack_forget()

            self.cargar_pantalla_principal()

        barra_opciones = CTkFrame(self, fg_color='blue', corner_radius=0)
        barra_opciones.pack(side=LEFT, fill='both', expand=False)

        logo_image = Image.open('../media/logo.png')
        ctk_logo_image = CTkImage(light_image=logo_image, size=(135, 135))
        label_logo = CTkLabel(barra_opciones, text='', image=ctk_logo_image)
        label_logo.grid(row=0, column=0, pady=10)
        label_logo.bind('<Button-1>', pantalla_principal)

        opc = ['🚗 Nuevo Servicio', '👤Clientes', '🔧 Automoviles', '👤 Empleados', 'pagar', '🔧 Refacciones']
        for i in range(len(opc)):
            label = CTkLabel(barra_opciones, width=200, text=opc[i], text_color='white', font=('arial', 16, 'bold'), corner_radius=10)
            label.grid(row=i + 1, column=0, ipady=15, padx=10)
            label.bind('<Button-1>', lambda event, lbl=label, acc=i: self._opcion(lbl, acc, event))
            self.opciones.append(label)

        texto_saludo = CTkLabel(barra_opciones, text=f'¡Hola, {self.session_empleado["nombre"]}!', text_color='white', font=('arial', 16, 'bold'))
        texto_saludo.grid(row=11, column=0, pady=(130, 20), sticky=S)

        label_cerrar_sesion = CTkLabel(barra_opciones, text='Cerrar Sesión', text_color='white', font=('arial', 16, 'bold'))
        label_cerrar_sesion.grid(row=12, column=0, sticky=S)
        label_cerrar_sesion.bind('<Enter>', lambda event: color_text(event, boton=label_cerrar_sesion, color='#b8161b'))
        label_cerrar_sesion.bind('<Leave>', lambda event: color_text(event, boton=label_cerrar_sesion, color='white'))
        label_cerrar_sesion.bind('<Button-1>', self.cerrar_sesion)

def color_text(event, boton, color):
    boton.configure(text_color=color)
