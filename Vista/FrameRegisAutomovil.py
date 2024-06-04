from datetime import *
from customtkinter import *
from Data_Base import Vehiculo, session,Mantenimiento
from Vista.MensajeEmergente import MensajeEmergente

class FrameRegisAutomovil(CTkToplevel):
    def __init__(self, root, rfc):
        super().__init__(root)
        self.root = root
        self.rfc_cliente = rfc

        self.title('Nuevo Vehiculo')
        CTkLabel(self, text='Datos del Vehiculo', font=('arial', 25, 'bold')).pack(pady=(0, 5), ipady=10)

        self.marca = StringVar()
        self.modelo = StringVar()
        self.anio = StringVar()
        self.motor = StringVar()
        self.km = StringVar()
        self.vin = StringVar()
        self.placas = StringVar()

        self._elementos_automovil()
        self._boton_submit()

    def _elementos_automovil(self):
        info_auto = CTkFrame(self)
        info_auto.pack(padx=10)

        CTkLabel(info_auto, width=135, text='Marca: ', font=('arial', 16, 'bold'), anchor='e').grid(row=1, column=0, padx=5, pady=5)
        CTkEntry(info_auto, width=200, font=('arial', 16), textvariable=self.marca).grid(row=1, column=1, padx=(0, 5))

        CTkLabel(info_auto, width=135, text='Modelo: ', font=('arial', 16, 'bold'), anchor='e').grid(row=1, column=2, padx=5, pady=5)
        CTkEntry(info_auto, width=200, font=('arial', 16), textvariable=self.modelo).grid(row=1, column=3, padx=(0, 5))

        CTkLabel(info_auto, width=135, text='Año: ', font=('arial', 16, 'bold'), anchor='e').grid(row=2, column=0, padx=5, pady=5)
        CTkEntry(info_auto, width=200, font=('arial', 16), textvariable=self.anio).grid(row=2, column=1, padx=(0, 5))

        CTkLabel(info_auto, width=135, text='Motor: ', font=('arial', 16, 'bold'), anchor='e').grid(row=2, column=2, padx=5, pady=5)
        CTkEntry(info_auto, width=200, font=('arial', 16), textvariable=self.motor).grid(row=2, column=3, padx=(0, 5))

        CTkLabel(info_auto, width=135, text='Kilometraje: ', font=('arial', 16, 'bold'), anchor='e').grid(row=3, column=0, padx=5, pady=5)
        CTkEntry(info_auto, width=200, font=('arial', 16), textvariable=self.km).grid(row=3, column=1, padx=(0, 5))

        CTkLabel(info_auto, width=135, text='VIN: ', font=('arial', 16, 'bold'), anchor='e').grid(row=3, column=2, padx=5, pady=5)
        CTkEntry(info_auto, width=200, font=('arial', 16), textvariable=self.vin).grid(row=3, column=3, padx=(0, 5))

        CTkLabel(info_auto, width=135, text='Placas: ', font=('arial', 16, 'bold'), anchor='e').grid(row=4, column=0, padx=5, pady=5)
        CTkEntry(info_auto, width=200, font=('arial', 16), textvariable=self.placas).grid(row=4, column=1, padx=(0, 5))

    def _boton_submit(self):
        buttons_frame = CTkFrame(self, fg_color='#ebebeb')
        buttons_frame.pack(padx=10, pady=(0, 10), expand=True)

        CTkButton(buttons_frame, text='Guardar', text_color='white', fg_color='green', font=('arial', 16, 'bold'), command=self.guardar_automovil).pack(side='left', padx=10, pady=5)

    def guardar_automovil(self):
        #Revisar que todos los campos esten llenos
        datos = [self.marca.get(), self.modelo.get(), self.anio.get(), self.motor.get(), self.km.get(), self.vin.get(), self.placas.get()]

        for dato in datos:
            if dato == '':
                MensajeEmergente(self, 'Error', 'Por favor. Llene todos los campos').mensaje_error()
                return
        try:
            # Nuevo Automovil
            if session.query(Vehiculo).filter(Vehiculo.VIN == self.vin.get()).first():
                MensajeEmergente(self, 'Error', 'El Vehiculo ya existe').mensaje_error()
            else:
                self.datetime = datetime.now()
                part_1_1 = Mantenimiento(Fecha_inicio=date(self.datetime.year, self.datetime.month, self.datetime.day), Estatus=0)
                session.add(part_1_1)
                session.commit()

                new_vehiculo = Vehiculo(
                    Marca=self.marca.get(),
                    Modelo=self.modelo.get(),
                    Anio=self.anio.get(),
                    Motor=self.motor.get(),
                    Kilometraje=self.km.get(),
                    VIN=self.vin.get(),
                    Placa=self.placas.get(),
                    RFC_Cliente=self.rfc_cliente
                )
                new_vehiculo.Maintenance.append(part_1_1)
                session.add(new_vehiculo)
                session.commit()

                MensajeEmergente(self, 'Exito', '¡Vehiculo guardado con éxito!').mensaje_correcto()
                self.limpiar_campos()
        except Exception as e:
            session.rollback()
            MensajeEmergente(self, 'Error','Error al guardar el Automovil. Por favor revise los campos').mensaje_error()

    def limpiar_campos(self):
        self.marca.set('')
        self.modelo.set('')
        self.anio.set('')
        self.motor.set('')
        self.km.set('')
        self.vin.set('')
        self.placas.set('')

