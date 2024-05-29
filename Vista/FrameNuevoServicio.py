from customtkinter import *
from Vista.MensajeEmergente import MensajeEmergente
from Modelo.Data_Base import session, Cliente, Vehiculo

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
        datos = [self.nombre.get(), self.ap_paterno.get(), self.ap_materno.get(), self.telefono.get(), self.rfc.get(), self.estado.get(), self.ciudad.get(), self.colonia.get(), self.cp.get(), self.calle.get(), self.num_int.get(), self.num_ext.get(), self.marca.get(), self.modelo.get(), self.anio.get(), self.motor.get(), self.km.get(), self.vin.get(), self.placas.get()]
        if self.tipo_cliente.get()=='1':
            del datos[1]
            del datos[1]

        for dato in datos:
            if dato == '':
                MensajeEmergente(self, 'Error', 'Por favor. Llene todos los campos').mensaje_error()
                return

        # ---------------# Inserts #---------------

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

        self.Insert_into_car = Vehiculo(

            # -------------# Auto #-------------
            Marca=self.marca.get(),
            Modelo=self.modelo.get(),
            Anio=self.anio.get(),
            Motor=self.motor.get(),
            Kilometraje=self.km.get(),
            VIN=self.vin.get(),
            Placa=self.placas.get()
        )

        self.Insert_into_client.vehicle.append(self.Insert_into_car)
        session.add(self.Insert_into_client)
        session.commit()
        MensajeEmergente(self, 'Exito', 'Servicio registrado Correctamente').mensaje_correcto()

        entry_marca.delete(0, END)
        entry_modelo.delete(0, END)
        entry_anio.delete(0, END)
        entry_motor.delete(0, END)
        entry_km.delete(0, END)
        entry_vin.delete(0, END)
        entry_placas.delete(0, END)

    def _agregar_auto(self):
        datos = [self.marca.get(), self.modelo.get(), self.anio.get(), self.motor.get(), self.km.get(), self.vin.get(), self.placas.get()]
        for dato in datos:
            if dato == '':
                MensajeEmergente(self, 'Error', 'Por favor. Llene los campos del Auto').mensaje_error()
                return


        self.Insert_into_car = Vehiculo(

            # -------------# Auto #-------------
            Marca=self.marca.get(),
            Modelo=self.modelo.get(),
            Anio=self.anio.get(),
            Motor=self.motor.get(),
            Kilometraje=self.km.get(),
            VIN=self.vin.get(),
            Placa=self.placas.get()
        )

        self.add_car = session.query(Cliente).filter_by(RFC = self.rfc.get()).one_or_none()
        self.add_car.vehicle.append(self.Insert_into_car)
        session.add(self.add_car)
        session.commit()
        MensajeEmergente(self, 'Exito', 'Auto registrado Correctamente').mensaje_correcto()

        entry_marca.delete(0, END)
        entry_modelo.delete(0, END)
        entry_anio.delete(0, END)
        entry_motor.delete(0, END)
        entry_km.delete(0, END)
        entry_vin.delete(0, END)
        entry_placas.delete(0, END)

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
        global entry_marca, entry_modelo, entry_anio, entry_motor, entry_km, entry_vin, entry_placas
        info_auto_cont = CTkFrame(self)
        info_auto_cont.pack(fill='x', padx=10, pady=5, expand=False)

        info_auto= CTkFrame(info_auto_cont, fg_color='#dbdbdb')
        info_auto.pack(expand=False)

        CTkLabel(info_auto, text='Datos del Auto', font=('arial', 18, 'bold')).grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        CTkLabel(info_auto, width=135, text='Marca: ', font=('arial', 16, 'bold'), anchor='e').grid(row=1, column=0, padx=5, pady=5)
        entry_marca = CTkEntry(info_auto, width=200, font=('arial', 16), textvariable=self.marca)
        entry_marca.grid(row=1, column=1, padx=(0, 20))
        CTkLabel(info_auto, width=135, text='Modelo: ', font=('arial', 16, 'bold'), anchor='e').grid(row=1, column=2, padx=5, pady=5)
        entry_modelo = CTkEntry(info_auto, width=200, font=('arial', 16), textvariable=self.modelo)
        entry_modelo.grid(row=1, column=3, padx=(0,20))
        CTkLabel(info_auto, width=135, text='Año: ', font=('arial', 16, 'bold'), anchor='e').grid(row=2, column=0, padx=5, pady=5)
        entry_anio = CTkEntry(info_auto, width=200, font=('arial', 16), textvariable=self.anio)
        entry_anio.grid(row=2, column=1, padx=(0,20))
        CTkLabel(info_auto, width=135, text='Motor: ', font=('arial', 16, 'bold'), anchor='e').grid(row=2, column=2, padx=5, pady=5)
        entry_motor = CTkEntry(info_auto, width=200, font=('arial', 16), textvariable=self.motor)
        entry_motor.grid(row=2, column=3, padx=(0,20))
        CTkLabel(info_auto, width=135, text='Kilometraje: ', font=('arial', 16, 'bold'), anchor='e').grid(row=3, column=0, padx=5, pady=5)
        entry_km = CTkEntry(info_auto, width=200, font=('arial', 16), textvariable=self.km)
        entry_km.grid(row=3, column=1, padx=(0,20))
        CTkLabel(info_auto, width=135, text='VIN: ', font=('arial', 16, 'bold'), anchor='e').grid(row=3, column=2, padx=5, pady=5)
        entry_vin = CTkEntry(info_auto, width=200, font=('arial', 16), textvariable=self.vin)
        entry_vin.grid(row=3, column=3, padx=(0,20))
        CTkLabel(info_auto, width=135, text='Placas: ', font=('arial', 16, 'bold'), anchor='e').grid(row=4, column=0, padx=5, pady=5)
        entry_placas = CTkEntry(info_auto, width=200, font=('arial', 16), textvariable=self.placas)
        entry_placas.grid(row=4, column=1, padx=(0,20))

    def _boton_submit(self):
        frm_botones = CTkFrame(self)
        frm_botones.pack(fill='x', padx=10, pady=5, expand=False)
        CTkButton(frm_botones, text='Guardar Servicio', font=('arial', 16, 'bold'), fg_color='blue', command=self._guardar_servicio).grid(row=0, column=1, padx=10, ipadx=5, ipady=5, sticky=E)
        CTkButton(frm_botones, text='Agregar Auto', font=('arial', 16, 'bold'), fg_color='blue', command=self._agregar_auto).grid(row=0, column=0, padx=10, ipadx=5, ipady=5, sticky=E)