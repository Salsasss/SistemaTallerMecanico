from tkinter import ttk
from customtkinter import *
from Modelo.Data_Base import session, Cliente

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

        self.select_buscar = CTkOptionMenu(cont_herramientas, width=170, variable=self.buscar_por, fg_color='blue', text_color='white', font=('arial', 16, 'bold'), values=['RFC', 'Nombre', 'Apellido Paterno', 'Apellido Materno', 'Teléfono'])
        self.select_buscar.pack(fill='x', side='left', ipady=5, padx=(0, 10))

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

        vscroll = ttk.Scrollbar(self.serv, orient='vertical', command=self.serv.yview)
        vscroll.pack(side='right', fill='y')
        self.serv.configure(yscrollcommand=vscroll.set)

        self.serv['columns'] = ('1', '2', '3', '4')
        self.serv.column('#0', width=40, minwidth=100)
        self.serv.column('1', anchor=CENTER, width=100)
        self.serv.column('2', anchor=CENTER, width=160)
        self.serv.column('3', anchor=CENTER, width=160)
        self.serv.column('4', anchor=CENTER, width=100)

        self.serv.heading('#0', text='RFC')
        self.serv.heading('1', text='Nombre')
        self.serv.heading('2', text='Apellido Paterno')
        self.serv.heading('3', text='Apellido Materno')
        self.serv.heading('4', text='Teléfono')

        self.texto_buscar.trace('w', actualizar_busqueda)
        self.buscar_por.trace('w', actualizar_busqueda)

    def actualizar_treeview(self):
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
            elif self.buscar_por.get() == '':
                clientes = session.query(Cliente).all()

        #print(self.texto_buscar.get())
        #print(self.buscar_por.get())
        for cliente in clientes:
            self.serv.insert('', 'end', text=cliente.RFC, values=(cliente.Nombre, cliente.Apellido_Paterno, cliente.Apellido_Materno, cliente.Telefono))