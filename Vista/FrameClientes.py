from tkinter import ttk
from customtkinter import *
from Data_Base import session, Cliente
from Vista.FrameRegisAutomovil import FrameRegisAutomovil
from Vista.MensajeEmergente import MensajeEmergente

class FrameClientes(CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        CTkLabel(self, text='Clientes', font=('arial', 25, 'bold')).pack(pady=(10, 0))

        # Variables del filtro
        self.texto_buscar = StringVar()
        self.buscar_por = StringVar()

        self._elementos_herramientas()
        self._elementos_tabla()
        self.actualizar_treeview()

    def _elementos_herramientas(self):
        def quitar_placeholder(e):
            if self.texto_buscar.get()=='Buscar':
                self.texto_buscar.set('')

        def poner_placeholder(e):
            if self.texto_buscar.get()=='':
                self.texto_buscar.set('Buscar')

        #Barra de busqueda
        cont_herramientas = CTkFrame(self, fg_color='#dbdbdb')
        cont_herramientas.pack(fill='x', padx=10, pady=10)

        self.buscar = CTkEntry(cont_herramientas, width=400, textvariable=self.texto_buscar, font=('arial', 16), border_width=2, border_color='blue', corner_radius=10)
        self.buscar.pack(fill='x', side='left', expand=True, ipady=5, padx=(0, 10))
        self.buscar.bind('<Button-1>', quitar_placeholder)
        self.buscar.bind('<KeyPress>', quitar_placeholder)
        self.buscar.bind('<KeyRelease>', poner_placeholder)
        self.texto_buscar.set('Buscar')

        self.select_buscar = CTkOptionMenu(cont_herramientas, width=170, variable=self.buscar_por, fg_color='blue', text_color='white', font=('arial', 16, 'bold'), values=['RFC', 'Nombre', 'Apellido Paterno', 'Apellido Materno', 'Teléfono', 'Estado', 'Ciudad', 'C.P.', 'Colonia', 'Calle', 'N. Ext.', 'N. Int.'])
        self.select_buscar.pack(fill='x', side='left', ipady=5, padx=(0, 10))

    def accion_automovil(self, rfc):
        ventana_nuevo_auto = FrameRegisAutomovil(self, rfc)
        ventana_nuevo_auto.geometry(f'+{(self.winfo_screenwidth()-1500 // 2)}+{(self.winfo_screenheight()-1500 // 2)}')
        ventana_nuevo_auto.resizable(False, False)
        ventana_nuevo_auto.grab_set()
        ventana_nuevo_auto.bind('<Destroy>', self.actualizar_treeview)

    def accion_doble_click(self, e): # Editar empleado
        ans = MensajeEmergente(self, 'Acciones', '¿Desea agregar un Automovil al cliente?')
        ans.mensaje_pregunta()
        self.wait_window(ans)
        if ans.ans:
            rfc = self.serv.item(self.serv.selection()[0], 'text')
            self.accion_automovil(rfc)

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

        # Scroll vertical
        vscroll = ttk.Scrollbar(self.serv, orient='vertical', command=self.serv.yview)
        vscroll.pack(side='right', fill='y')

        # Scroll horizontal
        vscroll = ttk.Scrollbar(self.serv, orient='horizontal', command=self.serv.xview)
        vscroll.pack(side='bottom', fill='x')
        self.serv.configure(xscrollcommand=vscroll.set)

        self.serv['columns'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11')
        self.serv.column('#0', width=40, minwidth=100)
        self.serv.column('1', anchor=CENTER, width=100)
        self.serv.column('2', anchor=CENTER, width=160)
        self.serv.column('3', anchor=CENTER, width=160)
        self.serv.column('4', anchor=CENTER, width=100)
        self.serv.column('5', anchor=CENTER, width=100)
        self.serv.column('6', anchor=CENTER, width=100)
        self.serv.column('7', anchor=CENTER, width=100)
        self.serv.column('8', anchor=CENTER, width=100)
        self.serv.column('9', anchor=CENTER, width=100)
        self.serv.column('10', anchor=CENTER, width=100)
        self.serv.column('11', anchor=CENTER, width=100)

        self.serv.heading('#0', text='RFC')
        self.serv.heading('1', text='Nombre')
        self.serv.heading('2', text='Apellido Paterno')
        self.serv.heading('3', text='Apellido Materno')
        self.serv.heading('4', text='Teléfono')
        self.serv.heading('5', text='Estado')
        self.serv.heading('6', text='Ciudad')
        self.serv.heading('7', text='C.P.')
        self.serv.heading('8', text='Colonia')
        self.serv.heading('9', text='calle')
        self.serv.heading('10', text='N. Ext.')
        self.serv.heading('11', text='N. Int.')

        self.texto_buscar.trace('w', actualizar_busqueda)
        self.buscar_por.trace('w', actualizar_busqueda)

        CTkLabel(self, text='ℹ️Doble click para agregar auto al cliente', font=('arial', 18, 'bold')).pack(fill='x', side='left', padx=10, pady=5)

    def actualizar_treeview(self, e=None):
        #Vaciando el Treeview de datos anteriores
        for item in self.serv.get_children():
            self.serv.delete(item)

        if self.texto_buscar.get() == 'Buscar':
            clientes = session.query(Cliente).all()
        else:
            if self.buscar_por.get() =='RFC':
                clientes = session.query(Cliente).filter(Cliente.RFC.like(f'%{self.texto_buscar.get()}%'))
            elif self.buscar_por.get() =='Nombre':
                clientes = session.query(Cliente).filter(Cliente.Nombre.like(f'%{self.texto_buscar.get()}%'))
            elif self.buscar_por.get() == 'Apellido Paterno':
                clientes = session.query(Cliente).filter(Cliente.Apellido_Paterno.like(f'%{self.texto_buscar.get()}%'))
            elif self.buscar_por.get() == 'Apellido Materno':
                clientes = session.query(Cliente).filter(Cliente.Apellido_Materno.like(f'%{self.texto_buscar.get()}%'))
            elif self.buscar_por.get() == 'Teléfono':
                clientes = session.query(Cliente).filter(Cliente.Telefono.like(f'%{self.texto_buscar.get()}%'))
            elif self.buscar_por.get() == 'Estado':
                clientes = session.query(Cliente).filter(Cliente.Estado.like(f'%{self.texto_buscar.get()}%'))
            elif self.buscar_por.get() == 'Ciudad':
                clientes = session.query(Cliente).filter(Cliente.Ciudad.like(f'%{self.texto_buscar.get()}%'))
            elif self.buscar_por.get() == 'C.P.':
                clientes = session.query(Cliente).filter(Cliente.Codigo_Postal.like(f'%{self.texto_buscar.get()}%'))
            elif self.buscar_por.get() == 'Colonia':
                clientes = session.query(Cliente).filter(Cliente.Colonia.like(f'%{self.texto_buscar.get()}%'))
            elif self.buscar_por.get() == 'Calle':
                clientes = session.query(Cliente).filter(Cliente.Calle.like(f'%{self.texto_buscar.get()}%'))
            elif self.buscar_por.get() == 'N. Ext.':
                clientes = session.query(Cliente).filter(Cliente.no_exterior.like(f'%{self.texto_buscar.get()}%'))
            elif self.buscar_por.get() == 'N. Int.':
                clientes = session.query(Cliente).filter(Cliente.no_interior.like(f'%{self.texto_buscar.get()}%'))
            elif self.buscar_por.get() == '':
                clientes = session.query(Cliente).all()

        for cliente in clientes:
            self.serv.insert('', 'end', text=cliente.RFC, values=(cliente.Nombre, cliente.Apellido_Paterno, cliente.Apellido_Materno, cliente.Telefono, cliente.Estado, cliente.Ciudad, cliente.Codigo_Postal, cliente.Colonia, cliente.Calle, cliente.no_exterior, cliente.no_interior))