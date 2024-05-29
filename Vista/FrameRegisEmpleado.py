from customtkinter import *
from PIL import Image
from Modelo.Data_Base import Empleado, session
from tkinter import messagebox, BooleanVar

class FrameRegisEmpleado(CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        CTkLabel(self, text='Registro de Usuario', font=('arial', 25, 'bold')).pack(pady=(0, 5), ipady=10)

        self.show = BooleanVar()
        self.rfc = StringVar()
        self.nombre = StringVar()
        self.apellido_paterno = StringVar()
        self.apellido_materno = StringVar()
        self.telefono = StringVar()
        self.puesto = StringVar()
        self.contrasenia = StringVar()
        self.mostrar_contrasenia = BooleanVar()
        self.original_rfc = None  # Variable para almacenar el RFC original

        self._elementos_usuario()
        self._boton_submit()

    def _elementos_usuario(self):
        def unshow(e):
            entry_passwd.configure(show='*')
            self.show.set(False)

        def show(e):
            entry_passwd.configure(show='')

        img_path_buscar = "../media/lupa.png"
        image_buscar = CTkImage(Image.open(img_path_buscar), size=(25, 25))

        info_usuario = CTkFrame(self)
        info_usuario.pack(fill='x', padx=10, pady=(0, 10), ipady=15, expand=True)

        CTkLabel(info_usuario, text='Datos del Empleado', font=('arial', 18, 'bold')).grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        CTkLabel(info_usuario, width=135, text='RFC: ', font=('arial', 16, 'bold'), anchor='e').grid(row=1, column=1, padx=10, pady=5)
        self.rfc_entry = CTkEntry(info_usuario, width=200, font=('arial', 16), fg_color='#dbdbdb', state=DISABLED, textvariable=self.rfc)
        self.rfc_entry.grid(row=1, column=2, padx=(0, 10))

        CTkLabel(info_usuario, width=135, text='Nombre: ', font=('arial', 16, 'bold'), anchor='e').grid(row=2, column=1, padx=10, pady=5)
        CTkEntry(info_usuario, width=200, font=('arial', 16), textvariable=self.nombre).grid(row=2, column=2, padx=(0, 10))

        CTkLabel(info_usuario, width=135, text='Apellido Paterno: ', font=('arial', 16, 'bold'), anchor='e').grid(row=3, column=1, padx=10, pady=5)
        CTkEntry(info_usuario, width=200, font=('arial', 16), textvariable=self.apellido_paterno).grid(row=3, column=2, padx=(0, 10))

        CTkLabel(info_usuario, width=135, text='Apellido Materno: ', font=('arial', 16, 'bold'), anchor='e').grid(row=4, column=1, padx=10, pady=5)
        CTkEntry(info_usuario, width=200, font=('arial', 16), textvariable=self.apellido_materno).grid(row=4, column=2, padx=(0, 10))

        CTkLabel(info_usuario, width=135, text='Teléfono: ', font=('arial', 16, 'bold'), anchor='e').grid(row=5, column=1, padx=10, pady=5)
        CTkEntry(info_usuario, width=200, font=('arial', 16), textvariable=self.telefono).grid(row=5, column=2, padx=(0, 10))

        CTkLabel(info_usuario, width=135, text='Puesto: ', font=('arial', 16, 'bold'), anchor='e').grid(row=6, column=1, padx=10, pady=5)
        CTkEntry(info_usuario, width=200, font=('arial', 16), textvariable=self.puesto).grid(row=6, column=2, padx=(0, 10))

        CTkLabel(info_usuario, width=135, text='Contraseña: ', font=('arial', 16, 'bold'), anchor='e').grid(row=7, column=1, padx=10, pady=5)
        check_show = CTkCheckBox(info_usuario, text='Mostrar', font=('arial', 16, 'bold'), variable=self.show)
        check_show.bind('<ButtonPress-1>', show)
        check_show.bind('<ButtonRelease-1>', unshow)
        check_show.grid(row=8, column=2, sticky=E)

        entry_passwd = CTkEntry(info_usuario, width=200, font=('arial', 16), textvariable=self.contrasenia, show='*')
        entry_passwd.grid(row=7, column=2, padx=(0, 10))

    def _boton_submit(self):
        buttons_frame = CTkFrame(self)
        buttons_frame.pack(padx=10, pady=(0, 10), expand=True)

        CTkButton(buttons_frame, text='Guardar', text_color='white', fg_color='green', font=('arial', 16, 'bold'), command=self.guardar_empleado).pack(side='left', padx=10, pady=5)
        CTkButton(buttons_frame, text='Modificar', text_color='white', fg_color='orange', font=('arial', 16, 'bold'), command=self.modificar_empleado).pack(side='left', padx=10, pady=5)
        CTkButton(buttons_frame, text='Eliminar', text_color='white', fg_color='red', font=('arial', 16, 'bold'), command=self.eliminar_empleado).pack(side='left', padx=10, pady=5)

    def toggle_mostrar_contrasenia(self):
        pass

    def buscar_empleado(self):
        rfc = self.rfc.get()
        empleado = session.query(Empleado).filter(Empleado.RFC == rfc).first()
        if empleado:
            self.nombre.set(empleado.Nombre)
            self.apellido_paterno.set(empleado.Apellido_Paterno)
            self.apellido_materno.set(empleado.Apellido_Materno)
            self.telefono.set(empleado.Telefono)
            self.puesto.set(empleado.Puesto)
            self.contrasenia.set(empleado.Contrasenia)
            self.original_rfc = rfc  # Guardar el RFC original
            messagebox.showinfo("Éxito", "Empleado encontrado")
        else:
            messagebox.showerror("Error", "Empleado no encontrado")
            self.limpiar_campos()

    def guardar_empleado(self):
        if session.query(Empleado).filter(Empleado.RFC == self.rfc.get()).first():
            messagebox.showerror("Error", "El empleado ya existe")
        else:
            new_empleado = Empleado(
                RFC=self.rfc.get(),
                Nombre=self.nombre.get(),
                Apellido_Paterno=self.apellido_paterno.get(),
                Apellido_Materno=self.apellido_materno.get(),
                Telefono=self.telefono.get(),
                Puesto=self.puesto.get(),
                Contrasenia=self.contrasenia.get()
            )
            session.add(new_empleado)
            session.commit()
            messagebox.showinfo("Éxito", "Empleado guardado con éxito")
            self.limpiar_campos()

    def modificar_empleado(self):
        rfc = self.rfc.get()
        if rfc != self.original_rfc:
            messagebox.showerror("Error", "No se puede modificar el RFC del empleado")
            return

        empleado = session.query(Empleado).filter(Empleado.RFC == rfc).first()
        if empleado:
            empleado.Nombre = self.nombre.get()
            empleado.Apellido_Paterno = self.apellido_paterno.get()
            empleado.Apellido_Materno = self.apellido_materno.get()
            empleado.Telefono = self.telefono.get()
            empleado.Puesto = self.puesto.get()
            empleado.Contrasenia = self.contrasenia.get()
            session.commit()
            messagebox.showinfo("Éxito", "Empleado modificado con éxito")
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "Empleado no encontrado")

    def eliminar_empleado(self):
        rfc = self.rfc.get()
        empleado = session.query(Empleado).filter(Empleado.RFC == rfc).first()
        if empleado:
            session.delete(empleado)
            session.commit()
            messagebox.showinfo("Éxito", "Empleado eliminado con éxito")
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "Empleado no encontrado")

    def limpiar_campos(self):
        self.rfc.set('')
        self.nombre.set('')
        self.apellido_paterno.set('')
        self.apellido_materno.set('')
        self.telefono.set('')
        self.puesto.set('')
        self.contrasenia.set('')
        self.original_rfc = None  # Limpiar el RFC original
