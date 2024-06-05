from customtkinter import *
from tkinter import ttk, messagebox
from PIL import Image
from Data_Base import Refacciones, Servicios, Contenido, session
from Vista.MensajeEmergente import MensajeEmergente


class FrameRefaccionesAdmi(CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        CTkLabel(self, text='Refacciones', font=('arial', 25, 'bold')).pack(pady=(0, 5), ipady=10)

        self.id_refaccion = StringVar()
        self.nombre_refaccion = StringVar()
        self.modelo = StringVar()
        self.cantidad = StringVar()
        self.costo = StringVar()
        self.menu = StringVar()

        self._elementos_refaccion()
        self._boton_submit()
        self._crear_treeview()
        self._cargar_datos()

    def _elementos_refaccion(self):
        img_path = "../media/carpeta.png"

        opciones = []
        for x in session.query(Servicios.Tipo_Servicio):
            opciones.append(x.Tipo_Servicio)

        info_refaccion = CTkFrame(self)
        info_refaccion.pack(fill='x', padx=10, ipady=15, expand=False)

        CTkLabel(info_refaccion, text='Datos de la Refacción', font=('arial', 18, 'bold')).grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        CTkLabel(info_refaccion, width=135, text='ID Refacción: ', font=('arial', 16, 'bold'), anchor='e').grid(row=1, column=0, padx=5, pady=5)
        self.id_entry = CTkEntry(info_refaccion, width=200, font=('arial', 16), textvariable=self.id_refaccion)
        self.id_entry.grid(row=1, column=1, padx=(0, 10))
        self.id_entry.configure(state=DISABLED, fg_color='#dbdbdb')
        CTkLabel(info_refaccion, width=135, text='Nombre Refacción: ', font=('arial', 16, 'bold'), anchor='e').grid(row=2, column=0, padx=5, pady=5)
        CTkEntry(info_refaccion, width=200, font=('arial', 16), textvariable=self.nombre_refaccion).grid(row=2, column=1, padx=(0, 10))

        CTkLabel(info_refaccion, width=135, text='Modelo: ', font=('arial', 16, 'bold'), anchor='e').grid(row=3, column=0, padx=5, pady=5)
        CTkEntry(info_refaccion, width=200, font=('arial', 16), textvariable=self.modelo).grid(row=3, column=1, padx=(0, 10))

        CTkLabel(info_refaccion, width=135, text='Costo: ', font=('arial', 16, 'bold'), anchor='e').grid(row=4, column=0, padx=5, pady=5)
        CTkEntry(info_refaccion, width=200, font=('arial', 16), textvariable=self.costo).grid(row=4, column=1, padx=(0, 10))

        CTkLabel(info_refaccion, width=135, text='Cantidad: ', font=('arial', 16, 'bold'), anchor='e').grid(row=1, column=2, padx=5, pady=5)
        CTkEntry(info_refaccion, width=200, font=('arial', 16), textvariable=self.cantidad).grid(row=1, column=3)

        CTkLabel(info_refaccion, width=135, text='Servicio: ', font=('arial', 16, 'bold'), anchor='e').grid(row=2, column=2, padx=5, pady=5)
        CTkOptionMenu(info_refaccion, width=300, fg_color='blue', variable=self.menu, text_color='white', font=('arial', 16, 'bold'), values=opciones).grid(row=2, column=3, padx=5, pady=5)

    def _boton_submit(self):
        buttons_frame = CTkFrame(self, fg_color='#dbdbdb')
        buttons_frame.pack(fill='x', pady=5, expand=False)

        self.boton_guardar = CTkButton(buttons_frame, text='Guardar', text_color='white', fg_color='green', font=('arial', 16, 'bold'), command=self._guardar_refaccion)
        self.boton_guardar.pack(side='left', padx=10, pady=5)

        self.boton_eliminar = CTkButton(buttons_frame, text='Eliminar', text_color='white', fg_color='#4d4d4d', font=('arial', 16, 'bold'), state=DISABLED, command=self._eliminar_refaccion)
        self.boton_eliminar.pack(side='left', padx=10, pady=5)

    def _crear_treeview(self):
        style = ttk.Style()
        style.configure('Treeview.Heading', background='blue', foreground='white', font=('arial', 16, 'bold'), padding=8)
        style.configure('Treeview', font=('arial', 16), rowheight=35)

        treeview_frame = CTkFrame(self)
        treeview_frame.pack(fill='both', padx=10, pady=(0, 10), expand=False)

        self.treeview = ttk.Treeview(treeview_frame, columns=('ID', 'Nombre', 'Modelo', 'Cantidad', 'Costo'), show='headings')

        self.treeview.column('#0', width=50)
        self.treeview.column('Nombre', anchor=CENTER, width=160)
        self.treeview.column('Modelo', anchor=CENTER, width=160)
        self.treeview.column('Cantidad', anchor=CENTER, width=50)
        self.treeview.column('Costo', anchor=CENTER, width=50)

        self.treeview.heading('ID', text='ID')
        self.treeview.heading('Nombre', text='Nombre')
        self.treeview.heading('Modelo', text='Modelo')
        self.treeview.heading('Cantidad', text='Cantidad')
        self.treeview.heading('Costo', text='Costo')
        self.treeview.pack(side='left', fill='both', expand=True)

        self.treeview.bind('<ButtonRelease-1>', self._seleccionar_fila)

        vscroll = ttk.Scrollbar(treeview_frame, orient='vertical', command=self.treeview.yview)
        vscroll.pack(side='right', fill='y')
        self.treeview.configure(yscrollcommand=vscroll.set)

        CTkLabel(self, text='ℹ️Click para cargar refacción', font=('arial', 18, 'bold')).pack(fill='x', side='left', padx=10, pady=5)

    def _cargar_datos(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        refacciones = session.query(Refacciones).all()
        for refaccion in refacciones:
            self.treeview.insert('', 'end', values=(refaccion.ID_refacciones, refaccion.NombreRefacciones, refaccion.Modelo, refaccion.Cantidad, refaccion.Costo))

    def _seleccionar_fila(self, event):
        selected_item = self.treeview.focus()
        if selected_item:
            values = self.treeview.item(selected_item, 'values')
            content_finder = session.query(Contenido).filter_by(ID_Refacciones = values[0]).first()
            services_finder = session.query(Servicios).filter_by(ID_servicio= content_finder.ID_Servicios).first()
            self.id_refaccion.set(values[0])
            self.nombre_refaccion.set(values[1])
            self.modelo.set(values[2])
            self.cantidad.set(values[3])
            self.costo.set(values[4])
            self.menu.set(services_finder.Tipo_Servicio)

            self.boton_guardar.configure(text='Editar', command=self._modificar_refaccion)
            self.boton_eliminar.configure(state=NORMAL, fg_color='red')

    def _guardar_refaccion(self):
        #Revisar que todos los campos esten llenos
        datos = [self.nombre_refaccion.get(), self.modelo.get(), self.costo.get(), self.costo.get(), self.menu.get()]

        for dato in datos:
            if dato == '':
                MensajeEmergente(self, 'Error', 'Por favor. Llene todos los campos').mensaje_error()
                return

        try:
            existing_refaccion = session.query(Refacciones).filter_by(ID_refacciones=self.id_refaccion.get()).first()
            service_finder = session.query(Servicios).where(Servicios.Tipo_Servicio.like(f"{self.menu.get()}")).first()
            if existing_refaccion:
                MensajeEmergente(self, 'Error', 'El ID de la refacción ya existe').mensaje_error()
            else:
                nueva_refaccion = Refacciones(
                    f"{self.nombre_refaccion.get()}",
                    f"{self.modelo.get()}",
                    int(self.cantidad.get()),
                    float(self.costo.get())
                )
                session.add(nueva_refaccion)
                session.commit()

                refaction_finder = session.query(Refacciones).where(Refacciones.NombreRefacciones.like(f"{self.nombre_refaccion.get()}")).first()
                nueva_relacion = Contenido(
                    ID_Servicios=service_finder.ID_servicio,
                    ID_Refacciones=refaction_finder.ID_refacciones
                )
                session.add(nueva_relacion)
                session.commit()

                MensajeEmergente(self, 'Éxito', 'Refacción guardada exitosamente').mensaje_correcto()
                self._cargar_datos()
                self._limpiar_campos()
        except Exception as e:
            session.rollback()
            MensajeEmergente(self, 'Error', 'Error al guardar la refacción. Por favor revise los campos').mensaje_error()

    def _modificar_refaccion(self):
        try:
            refaccion = session.query(Refacciones).filter_by(ID_refacciones=int(self.id_refaccion.get())).first()
            if refaccion:
                refaccion.NombreRefacciones = self.nombre_refaccion.get()
                refaccion.Modelo = self.modelo.get()
                refaccion.Cantidad = int(self.cantidad.get())
                refaccion.Costo = float(self.costo.get())
                session.commit()

                service_finder = session.query(Servicios).filter_by(Tipo_Servicio=self.menu.get()).first()
                existing_content = session.query(Contenido).filter_by(ID_Refacciones=self.id_refaccion.get()).first()
                existing_content.ID_Servicios = int(service_finder.ID_servicio)
                session.commit()

                MensajeEmergente(self, 'Éxito', "Refacción modificada exitosamente.").mensaje_correcto()
                self._cargar_datos()
            else:
                MensajeEmergente(self, 'Error', 'Refacción no encontrada.').mensaje_error()
        except Exception as e:
            session.rollback()
            MensajeEmergente(self, 'Error', f"Error al modificar: {e}").mensaje_error()
        finally:
            self._limpiar_campos()

    def _eliminar_refaccion(self):
        try:
            refaccion = session.query(Refacciones).filter_by(ID_refacciones=int(self.id_refaccion.get())).first()
            contenido = session.query(Contenido).filter_by(ID_Refacciones=int(self.id_refaccion.get())).first()
            if refaccion and contenido:
                session.delete(refaccion)
                session.delete(contenido)
                session.commit()

                MensajeEmergente(self, 'Éxito', 'Refacción eliminada exitosamente.').mensaje_correcto()
                self._cargar_datos()
            else:
                MensajeEmergente(self, 'Error', 'Refacción no encontrada.').mensaje_error()
        except Exception as e:
            session.rollback()
            MensajeEmergente(self, 'Error', f'Error al eliminar: {e}.').mensaje_error()
        finally:
            self._limpiar_campos()

    def _limpiar_campos(self):
        self.id_refaccion.set("")
        self.nombre_refaccion.set("")
        self.modelo.set("")
        self.cantidad.set("")
        self.costo.set("")