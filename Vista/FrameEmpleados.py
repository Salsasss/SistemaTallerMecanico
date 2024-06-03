from tkinter import ttk
from customtkinter import *
from Controlador.ctrlFunciones import *
from Data_Base import session, Empleado
from Vista.FrameRegisEmpleado import FrameRegisEmpleado
from Vista.MensajeEmergente import MensajeEmergente

class FrameEmpleados(CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root

        # Variables del filtro
        self.texto_buscar = StringVar()
        self.buscar_por = StringVar()
        self.estados = ['Inactivo', 'Activo']

        self._elementos_herramientas()
        self._elementos_tabla()
        self.actualizar_treeview()

    def accion_empleado(self, accion, rfc=''):
        ventana_nuevo_empleado = FrameRegisEmpleado(self, accion, rfc)
        ventana_nuevo_empleado.geometry(f'+{(self.winfo_screenwidth()-1500 // 2)}+{(self.winfo_screenheight()-1500 // 2)}')
        ventana_nuevo_empleado.grab_set()
        ventana_nuevo_empleado.bind('<Destroy>', self.actualizar_treeview)

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
        self.buscar.bind('<KeyPress>', quitar_placeholder)
        self.buscar.bind('<Button-1>', quitar_placeholder)
        self.buscar.bind('<KeyRelease>', poner_placeholder)
        self.texto_buscar.set('Buscar')

        self.select_buscar = CTkOptionMenu(cont_herramientas, width=170, variable=self.buscar_por, fg_color='blue', text_color='white', font=('arial', 16, 'bold'), values=['RFC', 'Nombre', 'Apellido Paterno', 'Apellido Materno', 'Teléfono', 'Tipo', 'Activo', 'Inactivo'])
        self.select_buscar.pack(fill='x', side='left', ipady=5, padx=(0, 10))

        self.boton_reportes = CTkButton(cont_herramientas, text='Nuevo Empleado', text_color='white', font=('arial', 16, 'bold'), fg_color='#1e8b1e', command=lambda: self.accion_empleado(0))
        self.boton_reportes.pack(fill='x', side='left', ipady=5)
        self.boton_reportes.bind('<Enter>', lambda event: color_fg(event, boton=self.boton_reportes, color='#125412'))
        self.boton_reportes.bind('<Leave>', lambda event: color_fg(event, boton=self.boton_reportes, color='#1e8b1e'))

    def accion_doble_click(self, e): # Editar empleado
        if self.serv.item(self.serv.selection()[0], 'text') == 'Activo': # Solo si el empleado esta Activo
            ans = MensajeEmergente(self, 'Acciones', '¿Editar Empleado?')
            ans.mensaje_pregunta()
            self.wait_window(ans)
            if ans.ans:
                rfc = self.serv.item(self.serv.selection()[0], 'values')[0]
                self.accion_empleado(1, rfc)
        else:
            MensajeEmergente(self, 'Error', 'Empleado dado de baja').mensaje_error()

    def _elementos_tabla(self):
        def actualizar_busqueda(*args):
            self.actualizar_treeview()

        cont_tabla = CTkFrame(self)
        cont_tabla.pack(fill='both', padx=10, pady=(0, 50), expand=True)

        style = ttk.Style()
        style.theme_use('default')
        style.configure('Treeview.Heading', background='blue', foreground='white', font=('arial', 16, 'bold'), padding=8)
        style.configure('Treeview', font=('arial', 16), rowheight=35)

        self.serv = ttk.Treeview(cont_tabla)
        self.serv.pack(fill='both', expand=True)
        self.serv.bind('<Double-Button-1>', self.accion_doble_click)

        # Colores de las filas
        self.serv.tag_configure('verde', background='#aaeeaa')
        self.serv.tag_configure('rojo', background='#f4a4a6')

        vscroll = ttk.Scrollbar(self.serv, orient='vertical', command=self.serv.yview)
        vscroll.pack(side='right', fill='y')
        self.serv.configure(yscrollcommand=vscroll.set)

        self.serv['columns'] = ('1', '2', '3', '4', '5', '6')
        self.serv.column('#0', anchor=CENTER, width=120)
        self.serv.column('1', anchor=CENTER, width=100)
        self.serv.column('2', anchor=CENTER, width=100)
        self.serv.column('3', anchor=CENTER, width=160)
        self.serv.column('4', anchor=CENTER, width=160)
        self.serv.column('5', anchor=CENTER, width=100)
        self.serv.column('6', anchor=CENTER, width=100)

        self.serv.heading('#0', text='Estado')
        self.serv.heading('1', text='RFC')
        self.serv.heading('2', text='Nombre')
        self.serv.heading('3', text='Apellido Paterno')
        self.serv.heading('4', text='Apellido Materno')
        self.serv.heading('5', text='Teléfono')
        self.serv.heading('6', text='Tipo')

        self.texto_buscar.trace('w', actualizar_busqueda)
        self.buscar_por.trace('w', actualizar_busqueda)

        CTkLabel(self, text='ℹ️Doble click para editar empleado', font=('arial', 18, 'bold')).pack(fill='x', side='left', padx=10, pady=5)

    def actualizar_treeview(self, e=None):
        # Vaciando el Treeview de datos anteriores
        for item in self.serv.get_children():
            self.serv.delete(item)

        if self.texto_buscar.get() == 'Buscar':
            if self.buscar_por.get() == 'Activo':
                empleados = session.query(Empleado).filter(Empleado.Estado==1)
            elif self.buscar_por.get() == 'Inactivo':
                empleados = session.query(Empleado).filter(Empleado.Estado==0)
            else:
                empleados = session.query(Empleado).all()
        else:
            if self.buscar_por.get() == 'Estado':
                empleados = session.query(Empleado).filter(Empleado.Estado.like(f'%{self.texto_buscar.get()}%'))
            if self.buscar_por.get() =='RFC':
                empleados = session.query(Empleado).filter(Empleado.RFC.like(f'%{self.texto_buscar.get()}%'))
            elif self.buscar_por.get() =='Nombre':
                empleados = session.query(Empleado).filter(Empleado.Nombre.like(f'%{self.texto_buscar.get()}%'))
            elif self.buscar_por.get() == 'Apellido Paterno':
                empleados = session.query(Empleado).filter(Empleado.Apellido_Paterno.like(f'%{self.texto_buscar.get()}%'))
            elif self.buscar_por.get() == 'Apellido Materno':
                empleados = session.query(Empleado).filter(Empleado.Apellido_Materno.like(f'%{self.texto_buscar.get()}%'))
            elif self.buscar_por.get() == 'Teléfono':
                empleados = session.query(Empleado).filter(Empleado.Telefono.like(f'%{self.texto_buscar.get()}%'))
            elif self.buscar_por.get() == 'Tipo':
                empleados = session.query(Empleado).filter(Empleado.Tipo.like(f'%{self.texto_buscar.get()}%'))
            elif self.buscar_por.get() == 'Activo':
                empleados = session.query(Empleado).filter(Empleado.Estado == 1)
            elif self.buscar_por.get() == 'Inactivo':
                empleados = session.query(Empleado).filter(Empleado.Estado == 0)
            elif self.buscar_por.get() == '':
                empleados = session.query(Empleado).all()

        for empleado in empleados:
            if empleado.Estado==1: #Empleado Activo
                self.serv.insert('', 'end', text=f'{self.estados[empleado.Estado]}', values=(empleado.RFC, empleado.Nombre, empleado.Apellido_Paterno, empleado.Apellido_Materno, empleado.Telefono, empleado.Tipo), tags=['verde'])
            elif empleado.Estado==0: #Empleado Inactivo
                self.serv.insert('', 'end', text=f'{self.estados[empleado.Estado]}', values=(empleado.RFC, empleado.Nombre, empleado.Apellido_Paterno, empleado.Apellido_Materno, empleado.Telefono, empleado.Tipo), tags=['rojo'])
