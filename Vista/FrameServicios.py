from tkinter import ttk
from customtkinter import *

class FrameServicios(CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        CTkLabel(self, text='Servicios', font=('arial', 25, 'bold')).pack(pady=(10, 0))

        self.texto_buscar = StringVar()

        self._elementos_herramientas()
        self._elementos_tabla()
        self.insertar_servicios()

    def _elementos_herramientas(self):
        def buscar(e):
            if self.texto_buscar.get()=='Buscar':
                self.texto_buscar.set('')

        def placeholder(e):
            if self.texto_buscar.get()=='':
                self.texto_buscar.set('Buscar')

        # Barra de busqueda
        cont_herramientas = CTkFrame(self, fg_color='#dbdbdb')
        cont_herramientas.pack(fill='x', padx=10, pady=10)

        self.buscar = CTkEntry(cont_herramientas, width=400, textvariable=self.texto_buscar, font=('arial', 16), border_width=2, border_color='blue', corner_radius=10)
        self.buscar.pack(fill='x', side='left', expand=True, ipady=5, padx=(0, 10))
        self.buscar.bind('<Button-1>', buscar)
        self.buscar.bind('<KeyRelease>', placeholder)
        self.texto_buscar.set('Buscar')

        self.select_buscar = CTkOptionMenu(cont_herramientas, width=170, fg_color='blue', text_color='white', font=('arial', 16, 'bold'), values=['Nombre', 'Apellido Paterno', 'Apellido Materno', 'Edad'])
        self.select_buscar.pack(fill='x', side='left', ipady=5, padx=(0, 10))

        self.boton_reportes = CTkButton(cont_herramientas, text='Generar Reporte', text_color='white', font=('arial', 16, 'bold'), fg_color='blue')
        self.boton_reportes.pack(fill='x', side='left', ipady=5)


    def _elementos_tabla(self):
        cont_tabla = CTkFrame(self)
        cont_tabla.pack(fill='both', padx=10, pady=(0, 50), expand=True)

        style = ttk.Style()
        style.theme_use('default')
        style.configure('Treeview.Heading', background='blue', foreground='white', font=('arial', 16, 'bold'), padding=8)
        style.configure('Treeview', font=('arial', 16))

        self.serv = ttk.Treeview(cont_tabla)
        self.serv.pack(fill='both', expand=True)

        vscroll = ttk.Scrollbar(self.serv, orient='vertical', command=self.serv.yview)
        vscroll.pack(side='right', fill='y')
        self.serv.configure(yscrollcommand=vscroll.set)

        self.serv['columns'] = ('1', '2', '3', '4', '5', '6', '7')
        self.serv.column('#0', anchor=CENTER, width=120)
        self.serv.column('1', anchor=CENTER, width=100)
        self.serv.column('2', anchor=CENTER, width=40)
        self.serv.column('3', anchor=CENTER, width=100)
        self.serv.column('4', anchor=CENTER, width=100)
        self.serv.column('5', anchor=CENTER, width=100)
        self.serv.column('6', anchor=CENTER, width=100)
        self.serv.column('7', anchor=CENTER, width=100)

        self.serv.heading('#0', text='VIN')
        self.serv.heading('1', text='Marca')
        self.serv.heading('2', text='Año')
        self.serv.heading('3', text='Kilometraje')
        self.serv.heading('4', text='Placa')
        self.serv.heading('5', text='Modelo')
        self.serv.heading('6', text='Motor')
        self.serv.heading('7', text='Estatus')

    def insertar_servicios(self):
        def completar_servicio(e):
            item = self.serv.selection()
            item_text = self.serv.item(item, "text")
            print(item_text)

        # Aqui se conectaria con la base de datos metiendo los clientes con un for
        
        self.serv.bind('<Button-1>', completar_servicio)