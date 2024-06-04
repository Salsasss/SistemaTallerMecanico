from customtkinter import *

from Controlador.ctrlFunciones import hashear
from Data_Base import Empleado, session
from tkinter import BooleanVar
from Vista.MensajeEmergente import MensajeEmergente

class FrameRegisEmpleado(CTkToplevel):
    def __init__(self, root, accion, rfc=''): #0 -> Nuevo Empleado, 1 -> Editar Empleado
        super().__init__(root)
        self.root = root
        self.rfc_buscar = rfc

        self.title('Nuevo Empleado')
        CTkLabel(self, text='Datos del Empleado', font=('arial', 25, 'bold')).pack(pady=(0, 5), ipady=10)

        self.accion = accion
        self.tipos_empleados = {'Normal':0, 'Gerente':1}
        self.tipos_empleados_ar = ['Normal', 'Gerente']
        self.show = BooleanVar()

        self.rfc = StringVar()
        self.nombre = StringVar()
        self.apellido_paterno = StringVar()
        self.apellido_materno = StringVar()
        self.telefono = StringVar()
        self.tipo = StringVar()
        self.contrasenia = StringVar()
        self.mostrar_contrasenia = BooleanVar()
        self.original_rfc = None  # Variable para almacenar el RFC original

        if self.accion==1: # Editar empleado
            self.buscar_empleado()

        self._elementos_usuario()
        self._boton_submit()

    def _elementos_usuario(self):
        def unshow(e):
            entry_passwd.configure(show='*')
            self.show.set(False)

        def show(e):
            entry_passwd.configure(show='')

        info_usuario = CTkFrame(self)
        info_usuario.pack(fill='x', padx=10, pady=(0, 10), ipady=15, expand=True)

        CTkLabel(info_usuario, width=135, text='RFC:', font=('arial', 16, 'bold'), anchor='e').grid(row=1, column=1, padx=10, pady=5)

        self.rfc_entry = CTkEntry(info_usuario, width=200, font=('arial', 16), textvariable=self.rfc)
        self.rfc_entry.grid(row=1, column=2, padx=(0, 10))

        if self.accion==1: # Editar Empleado
            self.rfc_entry.configure(state=DISABLED, fg_color='#dbdbdb')

        CTkLabel(info_usuario, width=135, text='Nombre: ', font=('arial', 16, 'bold'), anchor='e').grid(row=2, column=1, padx=10, pady=5)
        CTkEntry(info_usuario, width=200, font=('arial', 16), textvariable=self.nombre).grid(row=2, column=2, padx=(0, 10))

        CTkLabel(info_usuario, width=135, text='Apellido Paterno: ', font=('arial', 16, 'bold'), anchor='e').grid(row=3, column=1, padx=10, pady=5)
        CTkEntry(info_usuario, width=200, font=('arial', 16), textvariable=self.apellido_paterno).grid(row=3, column=2, padx=(0, 10))

        CTkLabel(info_usuario, width=135, text='Apellido Materno: ', font=('arial', 16, 'bold'), anchor='e').grid(row=4, column=1, padx=10, pady=5)
        CTkEntry(info_usuario, width=200, font=('arial', 16), textvariable=self.apellido_materno).grid(row=4, column=2, padx=(0, 10))

        CTkLabel(info_usuario, width=135, text='Teléfono: ', font=('arial', 16, 'bold'), anchor='e').grid(row=5, column=1, padx=10, pady=5)
        CTkEntry(info_usuario, width=200, font=('arial', 16), textvariable=self.telefono).grid(row=5, column=2, padx=(0, 10))

        CTkLabel(info_usuario, width=135, text='Tipo: ', font=('arial', 16, 'bold'), anchor='e').grid(row=6, column=1, padx=10, pady=5)
        CTkOptionMenu(info_usuario, width=200, variable=self.tipo, fg_color='white', text_color='black', font=('arial', 16, 'bold'), values=['Normal', 'Gerente']).grid(row=6, column=2, padx=(0, 10))

        txt_contra = 'Contraseña:'
        if self.accion==1: # Editar empleado
            txt_contra = 'Nueva Contraseña:'

        CTkLabel(info_usuario, width=135, text=txt_contra, font=('arial', 16, 'bold'), anchor='e').grid(row=7, column=1, padx=10, pady=5)
        check_show = CTkCheckBox(info_usuario, text='Mostrar', font=('arial', 16, 'bold'), variable=self.show)
        check_show.bind('<ButtonPress-1>', show)
        check_show.bind('<ButtonRelease-1>', unshow)
        check_show.grid(row=8, column=2, sticky=E)

        entry_passwd = CTkEntry(info_usuario, width=200, font=('arial', 16), textvariable=self.contrasenia, show='*')
        entry_passwd.grid(row=7, column=2, padx=(0, 10))

    def _boton_submit(self):
        buttons_frame = CTkFrame(self, fg_color='#ebebeb')
        buttons_frame.pack(padx=10, pady=(0, 10), expand=True)

        CTkButton(buttons_frame, text='Guardar', text_color='white', fg_color='green', font=('arial', 16, 'bold'), command=self.guardar_empleado).pack(side='left', padx=10, pady=5)
        if self.accion==1: # Editar empleado
            CTkButton(buttons_frame, text='Dar de Baja', text_color='white', fg_color='red', font=('arial', 16), command=self.baja_empleado).pack(side='left', padx=10, pady=5)

    def buscar_empleado(self):
        empleado = session.query(Empleado).filter(Empleado.RFC == self.rfc_buscar).first()
        if empleado:
            self.rfc.set(empleado.RFC)
            self.nombre.set(empleado.Nombre)
            self.apellido_paterno.set(empleado.Apellido_Paterno)
            self.apellido_materno.set(empleado.Apellido_Materno)
            self.telefono.set(empleado.Telefono)
            self.tipo.set(self.tipos_empleados_ar[empleado.Tipo])
            self.original_rfc = self.rfc_buscar
        else:
            MensajeEmergente(self, 'Error', 'Empleado no encontrado').mensaje_error()

    def guardar_empleado(self):
        #Revisar que todos los campos esten llenos
        datos = [self.rfc.get(), self.nombre.get(), self.apellido_paterno.get(), self.apellido_materno.get(), self.telefono.get(), self.tipo.get(), self.contrasenia.get()]

        if self.accion==1: # Si se esta editando
            datos.pop() # No se revisara que se halla escrito contraseña

        for dato in datos:
            if dato == '':
                MensajeEmergente(self, 'Error', 'Por favor. Llene todos los campos').mensaje_error()
                return

        if self.accion==0:
            # Nuevo empleado
            if session.query(Empleado).filter(Empleado.RFC == self.rfc.get()).first():
                MensajeEmergente(self, 'Error', 'El Empleado ya existe').mensaje_error()
            else:
                new_empleado = Empleado(
                    Estado=1,
                    RFC=self.rfc.get(),
                    Nombre=self.nombre.get(),
                    Apellido_Paterno=self.apellido_paterno.get(),
                    Apellido_Materno=self.apellido_materno.get(),
                    Telefono=self.telefono.get(),
                    Tipo=self.tipos_empleados.get(self.tipo.get()),
                    Contrasenia=hashear(self.contrasenia.get())
                )
                session.add(new_empleado)
                session.commit()
                MensajeEmergente(self, 'Exito', '¡Empleado guardado con éxito!').mensaje_correcto()
                self.limpiar_campos()
        elif self.accion==1:
            # Editar empleado
            empleado = session.query(Empleado).filter(Empleado.RFC == self.rfc_buscar).first()
            if empleado:
                empleado.Nombre = self.nombre.get()
                empleado.Apellido_Paterno = self.apellido_paterno.get()
                empleado.Apellido_Materno = self.apellido_materno.get()
                empleado.Telefono = self.telefono.get()
                empleado.Tipo = self.tipos_empleados.get(self.tipo.get())
                if self.contrasenia.get()!='':
                    empleado.Contrasenia = self.contrasenia.get()
                session.commit()
                MensajeEmergente(self, 'Exito', '¡Empleado modificado con éxito!').mensaje_correcto()

    def baja_empleado(self):
        empleado = session.query(Empleado).filter(Empleado.RFC == self.rfc_buscar).first()
        if empleado:
            ans = MensajeEmergente(self, 'Dar de Baja Empleado', '¿Esta seguro que desea dar de baja al empleado?')
            ans.mensaje_pregunta()
            self.wait_window(ans)
            if ans.ans:
                empleado.Estado = 0 # Inactivo
                session.commit()
                MensajeEmergente(self.root, 'Exito', '¡Empleado dado de baja con éxito!').mensaje_correcto()
                self.destroy()
        else:
            MensajeEmergente(self, 'Error', 'Empleado no encontrado').mensaje_error()

    def limpiar_campos(self):
        self.rfc.set('')
        self.nombre.set('')
        self.apellido_paterno.set('')
        self.apellido_materno.set('')
        self.telefono.set('')
        self.tipo.set('')
        self.contrasenia.set('')
        self.original_rfc = None  # Limpiar el RFC original
