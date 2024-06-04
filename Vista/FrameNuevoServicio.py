import datetime
from customtkinter import *
from datetime import *
from Controlador.ctrlFunciones import color_fg
from Vista.MensajeEmergente import MensajeEmergente
from Data_Base import session, Cliente, Vehiculo, Mantenimiento

class FrameNuevoServicio(CTkFrame):
    def __init__(self, root):
        super().__init__(root, fg_color='white')
        CTkLabel(self, text='Nuevo Servicio ', font=('arial', 25, 'bold')).pack(pady=(10, 5))

        self.tipo_cliente = StringVar()
        self.nombre = StringVar()
        self.ap_paterno = StringVar()
        self.ap_materno = StringVar()
        self.telefono = StringVar()
        self.rfc = StringVar()

        self.estado = StringVar()
        self.ciudad = StringVar()
        self.colonia = StringVar()
        self.cp = StringVar()
        self.calle = StringVar()
        self.num_int = StringVar()
        self.num_ext = StringVar()

        self.marca = StringVar()
        self.modelo = StringVar()
        self.anio = StringVar()
        self.motor = StringVar()
        self.km = StringVar()
        self.vin = StringVar()
        self.placas = StringVar()

        self._elementos_cliente()
        self._elementos_dire()
        self._elementos_auto()
        self._boton_submit()

    def _guardar_servicio(self):
        #Revisar que todos los campos esten llenos
        datos = [self.nombre.get(), self.ap_paterno.get(), self.ap_materno.get(), self.telefono.get(), self.rfc.get(), self.estado.get(), self.ciudad.get(), self.colonia.get(), self.cp.get(), self.calle.get(), self.num_int.get(), self.num_ext.get(), self.marca.get(), self.modelo.get(), self.anio.get(), self.motor.get(), self.km.get(), self.vin.get(), self.placas.get()]
        if self.tipo_cliente.get()=='1':
            del datos[1]
            del datos[1]

        for dato in datos:
            if dato == '':
                MensajeEmergente(self, 'Error', 'Por favor. Llene todos los campos').mensaje_error()
                return

        self.datetime = datetime.now()
        part_1 = Mantenimiento(Fecha_inicio=date(self.datetime.year,self.datetime.month, self.datetime.day), Estatus=0)
        session.add(part_1)
        session.commit()

        # ---------------# Inserts #---------------

        try:
            self.Insert_into_client = Cliente(
                # -------------# Cliente #-------------
                Nombre=self.nombre.get(),
                Apellido_Paterno=self.ap_paterno.get(),
                Apellido_Materno=self.ap_materno.get(),
                Telefono=self.telefono.get(),
                RFC=self.rfc.get(),

                # -------------# Direccion #-------------
                Estado=self.estado.get(),
                Ciudad=self.ciudad.get(),
                Colonia=self.colonia.get(),
                Codigo_Postal=self.cp.get(),
                Calle=self.calle.get(),
                no_interior=self.num_int.get(),
                no_exterior=self.num_ext.get(),
            )
        except Exception as e:
            session.rollback()
            MensajeEmergente(self, 'Error', 'Error al guardar el Cliente. Por favor revise los campos').mensaje_error()

        try:
            # -------------# Auto #-------------
            self.Insert_into_car = Vehiculo(
                Marca=self.marca.get(),
                Modelo=self.modelo.get(),
                Anio=self.anio.get(),
                Motor=self.motor.get(),
                Kilometraje=self.km.get(),
                VIN=self.vin.get(),
                Placa=self.placas.get()
            )
            self.finder = session.query(Mantenimiento).order_by(Mantenimiento.Orden.desc()).first()
            self.Insert_into_car.Maintenance.append(self.finder)
            self.Insert_into_client.vehicle.append(self.Insert_into_car)
            session.add(self.Insert_into_client)
            session.commit()

            MensajeEmergente(self, 'Exito', 'Servicio registrado Correctamente').mensaje_correcto()

            self.nombre.set('')
            self.ap_paterno.set('')
            self.ap_materno.set('')
            self.telefono.set('')
            self.rfc.set('')

            self.estado.set('')
            self.ciudad.set('')
            self.colonia.set('')
            self.cp.set('')
            self.calle.set('')
            self.num_int.set('')
            self.num_ext.set('')

            self.marca.set('')
            self.modelo.set('')
            self.anio.set('')
            self.motor.set('')
            self.km.set('')
            self.vin.set('')
            self.placas.set('')
        except Exception as e:
            session.rollback()
            MensajeEmergente(self, 'Error', 'Error al guardar el Automovil. Por favor revise los campos').mensaje_error()

    def _elementos_cliente(self):
        def elementos_persona(cont):
            CTkLabel(cont, width=135, text='Apellido Paterno: ', font=('arial', 16, 'bold'), anchor='e').grid(row=0, column=0, padx=5, pady=5)
            CTkEntry(cont, width=200, font=('arial', 16), textvariable=self.ap_paterno).grid(row=0, column=1, padx=(0, 20))

            CTkLabel(cont, width=135, text='Apellido Materno: ', font=('arial', 16, 'bold'), anchor='e').grid(row=0, column=2, padx=5, pady=5)
            CTkEntry(cont, width=200, font=('arial', 16), textvariable=self.ap_materno).grid(row=0, column=3, padx=(0, 20))

        def revisar_tipo():
            if self.tipo_cliente.get() == '1': # Es empresa
                cont.grid_remove()
            else: # Es persona
                cont.grid(row=2, column=0, columnspan=4, sticky=EW)
                elementos_persona(cont)

        info_cliente = CTkFrame(self)
        info_cliente.pack(fill='x', padx=10, pady=5, expand=False)

        CTkLabel(info_cliente, text='Datos del Cliente', font=('arial', 18, 'bold')).pack(fill='x', padx=10, pady=5, expand=False)

        tipo_cliente = CTkCheckBox(info_cliente, text='Es empresa', font=('arial', 16, 'bold'), variable=self.tipo_cliente, command=revisar_tipo)
        tipo_cliente.pack(pady=5, expand=False)

        info_persona = CTkFrame(info_cliente, fg_color='#dbdbdb')
        info_persona.pack(pady=5, expand=False)

        CTkLabel(info_persona, width=135, text='Nombre: ', font=('arial', 16, 'bold'), anchor='e').grid(row=1, column=0, padx=5, pady=5)
        CTkEntry(info_persona, width=200, font=('arial', 16), textvariable=self.nombre).grid(row=1, column=1, padx=(0, 20))

        CTkLabel(info_persona, width=135, text='Teléfono: ', font=('arial', 16, 'bold'), anchor='e').grid(row=1, column=2, padx=5, pady=5)
        CTkEntry(info_persona, width=200, font=('arial', 16), textvariable=self.telefono).grid(row=1, column=3, padx=(0, 20))

        cont = CTkFrame(info_persona)
        cont.grid(row=2, column=0, columnspan=4)

        elementos_persona(cont)

        CTkLabel(info_persona, width=135, text='RFC: ', font=('arial', 16, 'bold'), anchor='e').grid(row=3, column=0, padx=5, pady=5)
        CTkEntry(info_persona, width=200, font=('arial', 16), textvariable=self.rfc).grid(row=3, column=1, padx=(0, 20))

    def _elementos_dire(self):
        info_dir_cont = CTkFrame(self, fg_color='#dbdbdb')
        info_dir_cont.pack(fill='x', padx=10, pady=5, expand=False)

        info_dir = CTkFrame(info_dir_cont)
        info_dir.pack(expand=False)

        CTkLabel(info_dir, text='Datos de Dirección', font=('arial', 18, 'bold')).grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        CTkLabel(info_dir, width=135, text='Estado: ', font=('arial', 16, 'bold'), anchor='e').grid(row=1, column=0, padx=5, pady=5)
        CTkEntry(info_dir, width=200, font=('arial', 16), textvariable=self.estado).grid(row=1, column=1, padx=(0,20))

        CTkLabel(info_dir, width=135, text='Ciudad: ', font=('arial', 16, 'bold'), anchor='e').grid(row=1, column=2, padx=5, pady=5)
        CTkEntry(info_dir, width=200, font=('arial', 16), textvariable=self.ciudad).grid(row=1, column=3, padx=(0,20))

        CTkLabel(info_dir, width=135, text='Colonia: ', font=('arial', 16, 'bold'), anchor='e').grid(row=2, column=0, padx=5, pady=5)
        CTkEntry(info_dir, width=200, font=('arial', 16), textvariable=self.colonia).grid(row=2, column=1, padx=(0,20))

        CTkLabel(info_dir, width=135, text='Código Postal: ', font=('arial', 16, 'bold'), anchor='e').grid(row=2, column=2, padx=5, pady=5)
        CTkEntry(info_dir, width=200, font=('arial', 16), textvariable=self.cp).grid(row=2, column=3, padx=(0,20))

        CTkLabel(info_dir, width=135, text='Calle: ', font=('arial', 16, 'bold'), anchor='e').grid(row=3, column=0, padx=5, pady=5)
        CTkEntry(info_dir, width=200, font=('arial', 16), textvariable=self.calle).grid(row=3, column=1, padx=(0,20))

        CTkLabel(info_dir, width=135, text='Num. Interior: ', font=('arial', 16, 'bold'), anchor='e').grid(row=3, column=2, padx=5, pady=5)
        CTkEntry(info_dir, width=200, font=('arial', 16), textvariable=self.num_int).grid(row=3, column=3, padx=(0,20))

        CTkLabel(info_dir, width=135, text='Num. Exterior: ', font=('arial', 16, 'bold'), anchor='e').grid(row=4, column=0, padx=5, pady=5)
        CTkEntry(info_dir, width=200, font=('arial', 16), textvariable=self.num_ext).grid(row=4, column=1, padx=(0,20))

    def _elementos_auto(self):
        info_auto_cont = CTkFrame(self)
        info_auto_cont.pack(fill='x', padx=10, pady=5, expand=False)

        info_auto= CTkFrame(info_auto_cont, fg_color='#dbdbdb')
        info_auto.pack(expand=False)

        CTkLabel(info_auto, text='Datos del Auto', font=('arial', 18, 'bold')).grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        CTkLabel(info_auto, width=135, text='Marca: ', font=('arial', 16, 'bold'), anchor='e').grid(row=1, column=0, padx=5, pady=5)
        CTkEntry(info_auto, width=200, font=('arial', 16), textvariable=self.marca).grid(row=1, column=1, padx=(0, 20))

        CTkLabel(info_auto, width=135, text='Modelo: ', font=('arial', 16, 'bold'), anchor='e').grid(row=1, column=2, padx=5, pady=5)
        CTkEntry(info_auto, width=200, font=('arial', 16), textvariable=self.modelo).grid(row=1, column=3, padx=(0,20))

        CTkLabel(info_auto, width=135, text='Año: ', font=('arial', 16, 'bold'), anchor='e').grid(row=2, column=0, padx=5, pady=5)
        CTkEntry(info_auto, width=200, font=('arial', 16), textvariable=self.anio).grid(row=2, column=1, padx=(0,20))

        CTkLabel(info_auto, width=135, text='Motor: ', font=('arial', 16, 'bold'), anchor='e').grid(row=2, column=2, padx=5, pady=5)
        CTkEntry(info_auto, width=200, font=('arial', 16), textvariable=self.motor).grid(row=2, column=3, padx=(0,20))

        CTkLabel(info_auto, width=135, text='Kilometraje: ', font=('arial', 16, 'bold'), anchor='e').grid(row=3, column=0, padx=5, pady=5)
        CTkEntry(info_auto, width=200, font=('arial', 16), textvariable=self.km).grid(row=3, column=1, padx=(0,20))

        CTkLabel(info_auto, width=135, text='VIN: ', font=('arial', 16, 'bold'), anchor='e').grid(row=3, column=2, padx=5, pady=5)
        CTkEntry(info_auto, width=200, font=('arial', 16), textvariable=self.vin).grid(row=3, column=3, padx=(0,20))

        CTkLabel(info_auto, width=135, text='Placas: ', font=('arial', 16, 'bold'), anchor='e').grid(row=4, column=0, padx=5, pady=5)
        CTkEntry(info_auto, width=200, font=('arial', 16), textvariable=self.placas).grid(row=4, column=1, padx=(0,20))

    def _boton_submit(self):
        frm_botones = CTkFrame(self, fg_color='white')
        frm_botones.pack(fill='x', padx=10, pady=5, expand=False)
        boton_submit = CTkButton(frm_botones, text='Guardar Servicio', font=('arial', 16, 'bold'), fg_color='#1e8b1e', command=self._guardar_servicio)
        boton_submit.pack(side='right', ipadx=5, ipady=5)
        boton_submit.bind('<Enter>', lambda event: color_fg(event, boton=boton_submit, color='#125412'))
        boton_submit.bind('<Leave>', lambda event: color_fg(event, boton=boton_submit, color='#1e8b1e'))