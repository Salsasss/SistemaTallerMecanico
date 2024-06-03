from tkinter.ttk import Treeview
from tkinter import messagebox, ttk
from customtkinter import *
from tkinter import *

from Controlador.ctrlFunciones import color_fg
from Vista.FrameAutomoviles import FrameAutomoviles
from Vista.MensajeEmergente import MensajeEmergente

class FramePagar(CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        CTkLabel(self, text='Pagar', font=('arial', 25, 'bold')).pack(fill='x', pady=(10, 0))
        #CTkLabel(self, text='Pagar', font=('arial', 25, 'bold')).grid(row=0, column=0)
        self.txt_compra = StringVar()

        cont_herramientas = CTkFrame(self, fg_color='#dbdbdb')
        cont_herramientas.pack(fill='x', padx=10)

        self.entry_buscar = CTkEntry(cont_herramientas, font=('arial', 16), border_width=2, border_color='blue', corner_radius=10, justify=CENTER)
        #self.entry_buscar.grid(row=1, column=0, sticky=EW, padx=10, pady=10, ipady=5)
        self.entry_buscar.pack(fill='x', side='left', expand=True, padx=(0, 10), pady=10, ipady=5)

        #CTkButton(self, fg_color='blue', text='Buscar', font=('arial', 16, 'bold')).grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5)
        CTkButton(cont_herramientas, fg_color='blue', text='Buscar', font=('arial', 16, 'bold')).pack(fill='x', side='left', pady=5, ipadx=5, ipady=5)

        style = ttk.Style()
        style.configure('Treeview.Heading', background='blue', foreground='white', font=('arial', 16, 'bold'), padding=8)
        style.configure('Treeview', font=('arial', 16), rowheight=22)

        #Treeview 1
        cont_tree1 = CTkFrame(self)
        #cont_tree1.grid(row=2, column=0, sticky=EW, padx=5, pady=5, columnspan=2)
        cont_tree1.pack(fill='x', padx=10, pady=(0, 5))

        scrollbar = ttk.Scrollbar(cont_tree1)
        scrollbar.pack(side='right', fill='y')
        self.tree_productos = ttk.Treeview(cont_tree1, columns=('producto', 'cantidad', 'precio'), yscrollcommand=scrollbar.set)
        self.tree_productos.pack(fill='both', expand=True)
        scrollbar.config(command=self.tree_productos.yview)

        #Treeview 2
        cont_tree2 = CTkFrame(self)
        #cont_tree2.grid(row=3, column=0, sticky=EW, padx=5, pady=5, columnspan=2)
        cont_tree2.pack(fill='x', padx=10, pady=(0, 5))

        scrollbar = ttk.Scrollbar(cont_tree2)
        scrollbar.pack(side='right', fill='y')
        self.tree_servicios = Treeview(cont_tree2, columns=('servicio', 'descuento', 'precio'), yscrollcommand=scrollbar.set)
        self.tree_servicios.pack(fill='both', expand=True)
        scrollbar.config(command=self.tree_servicios.yview)

        headings_productos = [('#0', 'ID'), ('producto', 'Productos'), ('cantidad', 'Cantidad'), ('precio', 'Precio')]
        headings_servicios = [('#0', 'ID'), ('servicio', 'Servicios'), ('descuento', 'Descuento'), ('precio', 'Precio')]

        for heading in headings_productos:
            self.tree_productos.heading(heading[0], text=heading[1])
            self.tree_productos.column(heading[0], anchor=CENTER, width=200)

        for heading in headings_servicios:
            self.tree_servicios.heading(heading[0], text=heading[1])
            self.tree_servicios.column(heading[0], anchor=CENTER, width=200)

        listaUsers = [('Yerimua', 'Traakaaa', '3'), ('BellaKat', 'Kbonitos0J0s', '3'), ('Tochika', 'Tokio0J0s', '3'), ('LunaBella', 'LuNabella69', '3'),('Yerimua', 'Traakaaa', '3'), ('BellaKat', 'Kbonitos0J0s', '3'), ('Tochika', 'Tokio0J0s', '3'), ('LunaBella', 'LuNabella69', '3'),('Yerimua', 'Traakaaa', '3'), ('BellaKat', 'Kbonitos0J0s', '3'), ('Tochika', 'Tokio0J0s', '3'), ('LunaBella', 'LuNabella69', '3')]

        cont = 0
        for user in listaUsers:
            cont += 1
            self.tree_productos.insert('', END, text=str(cont), values=(user[0], user[1], user[2]))
            self.tree_servicios.insert('', END, text=str(cont), values=(user[0], user[1], user[2]))

        #CTkLabel(self, text='Total de la compra', font=('arial', 16, 'bold')).grid(row=4, column=0, sticky=NSEW, padx=5, pady=5, columnspan=2)
        #CTkEntry(self, justify=CENTER, state=DISABLED, textvariable=self.txt_compra, font=('arial', 16), border_width=2, border_color='blue', corner_radius=10).grid(row=5, column=0, sticky=EW, padx=5, pady=5, ipady=5, columnspan=2)

        CTkLabel(self, text='Total de la compra', font=('arial', 16, 'bold')).pack(fill='x', padx=5, pady=5)
        CTkEntry(self, justify=CENTER, state=DISABLED, textvariable=self.txt_compra, font=('arial', 16), border_width=2, border_color='blue', corner_radius=10).pack(fill='x', padx=5, pady=5, ipady=5)

        self.txt_compra.set('20')

        cont_botones = CTkFrame(self, fg_color='#dbdbdb')
        #cont_botones.grid(row=6, column=0, padx=5, pady=5, columnspan=2)
        cont_botones.pack(padx=5, pady=5)

        boton_cancelar = CTkButton(cont_botones, text='Cancelar', fg_color='#b8161b', font=('arial', 16, 'bold'), command=self.cancel)
        boton_cancelar.bind('<Enter>', lambda event: color_fg(event, boton=boton_cancelar, color='#891014'))
        boton_cancelar.bind('<Leave>', lambda event: color_fg(event, boton=boton_cancelar, color='#b8161b'))
        boton_cancelar.grid(row=0, column=0, padx=15, pady=5, ipadx=5, ipady=5)

        boton_completar = CTkButton(cont_botones, text='Completar Compra', fg_color='#1e8b1e', font=('arial', 16, 'bold'), command=self.pagar)
        boton_completar.grid(row=0, column=1, padx=15, pady=5, ipadx=5, ipady=5)
        boton_completar.bind('<Enter>', lambda event: color_fg(event, boton=boton_completar, color='#125412'))
        boton_completar.bind('<Leave>', lambda event: color_fg(event, boton=boton_completar, color='#1e8b1e'))

    def pagar(self):
        ans = MensajeEmergente(self, 'Concretar Pago', '¿Desea concretar la compra?')
        ans.mensaje_pregunta()
        self.wait_window(ans)
        if ans.ans:
            MensajeEmergente(self, 'Pago', 'Compra finalizada con exito!!').mensaje_correcto()

    def cancel(self):
        ans = MensajeEmergente(self, 'Cancelar Pago', '¿Desea cancelar la compra?')
        ans.mensaje_pregunta()
        self.wait_window(ans)
        if ans.ans:
            for widget in self.root.pack_slaves():
                widget.pack_forget()

            FrameAutomoviles(self.root).pack(padx=10, pady=10, fill='both', expand=True)
