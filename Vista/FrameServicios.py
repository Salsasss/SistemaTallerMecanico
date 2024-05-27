from tkinter import ttk
from customtkinter import *

class FrameServicios(CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        CTkLabel(self, text='Servicios ', font=('arial', 25, 'bold')).pack(pady=10)

        self.texto_buscar = StringVar()

        self._elementos_herramientas()
        self._elementos_tabla()

    def _elementos_herramientas(self):
        def buscar(e):
            if self.texto_buscar.get()=='Buscar':
                self.texto_buscar.set('')

        def placeholder(e):
            if self.texto_buscar.get()=='':
                self.texto_buscar.set('Buscar')

        cont_herramientas = CTkFrame(self, fg_color='#dbdbdb')
        cont_herramientas.pack(fill='x', padx=10, pady=10)

        self.buscar = CTkEntry(cont_herramientas, width=400, textvariable=self.texto_buscar, font=('arial', 16), border_width=2, border_color='blue', corner_radius=10)
        self.buscar.grid(row=0, column=0, ipady=5, padx=(0, 10))
        self.buscar.bind('<Button-1>', buscar)
        self.buscar.bind('<KeyRelease>', placeholder)
        self.texto_buscar.set('Buscar')

        self.select_buscar = CTkOptionMenu(cont_herramientas, width=170, fg_color='blue', text_color='white', font=('arial', 16, 'bold'), values=['Nombre','Apellido Paterno', 'Apellido Materno', 'Edad'])
        self.select_buscar.grid(row=0, column=1, ipady=5, padx=(0, 10))

        self.boton_reportes = CTkButton(cont_herramientas, text='Generar Reporte', text_color='white', font=('arial', 16, 'bold'), fg_color='blue')
        self.boton_reportes.grid(row=0, column=2, ipady=5,)

    def _elementos_tabla(self):
        cont_tabla = CTkFrame(self)
        cont_tabla.pack(fill='both', padx=10, pady=(0, 50), expand=True)

        style = ttk.Style()
        style.theme_use('default')
        style.configure('Treeview.Heading', background='blue', foreground='white', font=('arial', 16, 'bold'), padding=8)
        style.configure('Treeview', font=('arial', 16))

        self.serv = ttk.Treeview(cont_tabla)
        self.serv.pack(fill='both', expand=True)

        self.serv['columns'] = ('1', '2', '3', '4', '5', '6')
        self.serv.column('#0', width=40, minwidth=50)
        self.serv.column('1', anchor=CENTER, width=100)
        self.serv.column('2', anchor=CENTER, width=160)
        self.serv.column('3', anchor=CENTER, width=160)
        self.serv.column('4', anchor=CENTER, width=100)
        self.serv.column('5', anchor=CENTER, width=100)
        self.serv.column('6', anchor=CENTER, width=100)

        self.serv.heading('#0', text='ID')
        self.serv.heading('1', text='Nombre')
        self.serv.heading('2', text='Apellido Paterno')
        self.serv.heading('3', text='Apellido Materno')
        self.serv.heading('4', text='RFC')
        self.serv.heading('5', text='Teléfono')
        self.serv.heading('6', text='Servicios')

        self.serv.insert('', END, text='Elemento 1', values=('1A', '1B', '1C', 's', '2'))
        self.serv.insert('', END, text='Elemento 1', values=('1A', '1B', '1C', 's', '2'))
        self.serv.insert('', END, text='Elemento 1', values=('1A', '1B', '1C', 's', '2'))
        self.serv.insert('', END, text='Elemento 1', values=('1A', '1B', '1C', 's', '2'))
        self.serv.insert('', END, text='Elemento 1', values=('1A', '1B', '1C', 's', '2'))
        self.serv.insert('', END, text='Elemento 2', values=('2A', '2B', '2C', 'x', 'w'))

