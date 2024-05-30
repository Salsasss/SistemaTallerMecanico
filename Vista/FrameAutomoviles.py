from tkinter import ttk
from customtkinter import *
from Modelo.Data_Base import session, Vehiculo
from Vista.FrameCataRefacciones import FrameCataRefacciones
from Vista.MensajeEmergente import MensajeEmergente

class FrameAutomoviles(CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        CTkLabel(self, text='Automoviles', font=('arial', 25, 'bold')).pack(pady=(10, 0))
        self.root = root

        # Variables del filtro
        self.texto_buscar = StringVar()
        self.buscar_por = StringVar()

        self._elementos_herramientas()
        self._elementos_tabla()
        self.actualizar_treeview()

    def _elementos_herramientas(self):
        def quitar_placeholder(e):
            if self.texto_buscar.get() == 'Buscar':
                self.texto_buscar.set('')

        def poner_placeholder(e):
            if self.texto_buscar.get() == '':
                self.texto_buscar.set('Buscar')

        def actualizar_busqueda(*args):
            self.actualizar_treeview()

        # Barra de busqueda
        cont_herramientas = CTkFrame(self, fg_color='#dbdbdb')
        cont_herramientas.pack(fill='x', padx=10, pady=10)

        self.buscar = CTkEntry(cont_herramientas, width=400, textvariable=self.texto_buscar, font=('arial', 16), border_width=2, border_color='blue', corner_radius=10)
        self.buscar.pack(fill='x', side='left', expand=True, ipady=5, padx=(0, 10))
        self.buscar.bind('<Button-1>', quitar_placeholder)
        self.buscar.bind('<KeyPress>', quitar_placeholder)
        self.buscar.bind('<KeyRelease>', poner_placeholder)
        self.texto_buscar.set('Buscar')

        self.select_buscar = CTkOptionMenu(cont_herramientas, width=170, variable=self.buscar_por, fg_color='blue', text_color='white', font=('arial', 16, 'bold'), values=['RFC Cliente', 'VIN', 'Marca', 'Año', 'Kilometraje', 'Placa', 'Modelo', 'Motor', 'Estatus'])
        self.select_buscar.pack(fill='x', side='left', ipady=5, padx=(0, 10))

        self.boton_reportes = CTkButton(cont_herramientas, text='Generar Reporte', text_color='white', font=('arial', 16, 'bold'), fg_color='blue')
        self.boton_reportes.pack(fill='x', side='left', ipady=5)

    def accion_doble_click(self, e):
        ans = MensajeEmergente(self, 'Servicio', '¿Desea completar el servicio?')
        ans.mensaje_pregunta()
        self.wait_window(ans)
        if ans.ans:
            #Borrar todo del frame
            for widget in self.root.pack_slaves():
                widget.pack_forget()
            vin = self.serv.item(self.serv.selection()[0], 'text')
            print(vin)
            FrameCataRefacciones(self.root).pack(padx=10, pady=10, fill='both', expand=True)

    def _elementos_tabla(self):
        def actualizar_busqueda(*args):
            self.actualizar_treeview()

        cont_tabla = CTkFrame(self)
        cont_tabla.pack(fill='both', padx=10, pady=(0, 50), expand=True)

        style = ttk.Style()
        style.theme_use('default')
        style.configure('Treeview.Heading', background='blue', foreground='white', font=('arial', 16, 'bold'))
        style.configure('Treeview', font=('arial', 16), rowheight=35)

        self.serv = ttk.Treeview(cont_tabla)
        self.serv.pack(fill='both', expand=True)
        self.serv.bind('<Double-Button-1>', self.accion_doble_click)

        vscroll = ttk.Scrollbar(self.serv, orient='vertical', command=self.serv.yview)
        vscroll.pack(side='right', fill='y')
        self.serv.configure(yscrollcommand=vscroll.set)

        self.serv['columns'] = ('1', '2', '3', '4', '5', '6', '7', '8')
        self.serv.column('#0', anchor=CENTER, width=120)
        self.serv.column('1', anchor=CENTER, width=120)
        self.serv.column('2', anchor=CENTER, width=40)
        self.serv.column('3', anchor=CENTER, width=40)
        self.serv.column('4', anchor=CENTER, width=100)
        self.serv.column('5', anchor=CENTER, width=100)
        self.serv.column('6', anchor=CENTER, width=100)
        self.serv.column('7', anchor=CENTER, width=100)
        self.serv.column('8', anchor=CENTER, width=100)

        self.serv.heading('#0', text='RFC Cliente')
        self.serv.heading('1', text='VIN')
        self.serv.heading('2', text='Marca')
        self.serv.heading('3', text='Año')
        self.serv.heading('4', text='Kilometraje')
        self.serv.heading('5', text='Placa')
        self.serv.heading('6', text='Modelo')
        self.serv.heading('7', text='Motor')
        self.serv.heading('8', text='Estatus')

        self.texto_buscar.trace('w', actualizar_busqueda)
        self.buscar_por.trace('w', actualizar_busqueda)

    def actualizar_treeview(self):
        # Vaciando el Treeview de datos anteriores
        for item in self.serv.get_children():
            self.serv.delete(item)

        if self.texto_buscar.get() == 'Buscar':
            vehiculos = session.query(Vehiculo).all()
        else:
            if self.buscar_por.get() == 'RFC Cliente':
                vehiculos = session.query(Vehiculo).filter(Vehiculo.RFC_Cliente.like(f'%{self.texto_buscar.get()}%'))
            if self.buscar_por.get() == 'VIN':
                vehiculos = session.query(Vehiculo).filter(Vehiculo.VIN.like(f'%{self.texto_buscar.get()}%'))
            elif self.buscar_por.get() == 'Marca':
                vehiculos = session.query(Vehiculo).filter(Vehiculo.Marca.like(f'%{self.texto_buscar.get()}%'))
            elif self.buscar_por.get() == 'Año':
                vehiculos = session.query(Vehiculo).filter(Vehiculo.Anio.like(f'%{self.texto_buscar.get()}%'))
            elif self.buscar_por.get() == 'Kilometraje':
                vehiculos = session.query(Vehiculo).filter(Vehiculo.Kilometraje.like(f'%{self.texto_buscar.get()}%'))
            elif self.buscar_por.get() == 'Placa':
                vehiculos = session.query(Vehiculo).filter(Vehiculo.Placa.like(f'%{self.texto_buscar.get()}%'))
            elif self.buscar_por.get() == 'Modelo':
                vehiculos = session.query(Vehiculo).filter(Vehiculo.Modelo.like(f'%{self.texto_buscar.get()}%'))
            elif self.buscar_por.get() == 'Motor':
                vehiculos = session.query(Vehiculo).filter(Vehiculo.Motor.like(f'%{self.texto_buscar.get()}%'))
            elif self.buscar_por.get() == '':
                vehiculos = session.query(Vehiculo).all()

        for vehiculo in vehiculos:
            self.serv.insert('', 'end', text=f'{vehiculo.RFC_Cliente}', values=(vehiculo.VIN, vehiculo.Marca, vehiculo.Anio, vehiculo.Kilometraje, vehiculo.Placa, vehiculo.Modelo, vehiculo.Motor))