from tkinter.ttk import Treeview
from tkinter import messagebox, ttk
from customtkinter import *
from tkinter import *

from Vista.MensajeEmergente import MensajeEmergente


class FramePagar(CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        self.txt_compra = StringVar()

        self.entry_buscar = CTkEntry(self, width=590, font=('arial', 16), justify=CENTER)
        self.entry_buscar.grid(row=0, column=0, padx=10, pady=10, ipady=5)

        CTkButton(self, fg_color='blue', text='Buscar', font=('arial', 16, 'bold')).grid(row=0, column=1, padx=5, pady=5, ipadx=5, ipady=5)

        style = ttk.Style()
        style.configure('Treeview.Heading', background='blue', foreground='white', font=('arial', 16, 'bold'), padding=8)
        style.configure('Treeview', font=('arial', 16))
        self.tree_productos = Treeview(self, columns=('producto', 'cantidad', 'precio'), )
        self.tree_servicios = Treeview(self, columns=('servicio', 'descuento', 'precio'), )

        headings_productos = [('#0', 'ID'), ('producto', 'PRODUCTOS'), ('cantidad', 'CANTIDAD'), ('precio', 'PRECIO')]
        headings_servicios = [('#0', 'ID'), ('servicio', 'SERVICIOS'), ('descuento', 'Descuento'), ('precio', 'PRECIO')]

        for heading in headings_productos:
            self.tree_productos.heading(heading[0], text=heading[1])
            self.tree_productos.column(heading[0], anchor=CENTER, width=200)

        for heading in headings_servicios:
            self.tree_servicios.heading(heading[0], text=heading[1])
            self.tree_servicios.column(heading[0], anchor=CENTER, width=200)

        listaUsers = [('Yerimua', 'Traakaaa', '3'), ('BellaKat', 'Kbonitos0J0s', '3'), ('Tochika', 'Tokio0J0s', '3'), ('LunaBella', 'LuNabella69', '3')]

        cont = 0
        for user in listaUsers:
            cont += 1
            self.tree_productos.insert('', END, text=str(cont), values=(user[0], user[1], user[2]))
            self.tree_servicios.insert('', END, text=str(cont), values=(user[0], user[1], user[2]))

        self.tree_productos.grid(row=1, column=0, sticky=EW, padx=5, pady=5, columnspan=2)
        self.tree_servicios.grid(row=2, column=0, sticky=EW, padx=5, pady=5, columnspan=2)

        CTkLabel(self, text='Total de la compra', font=('arial', 16, 'bold')).grid(row=3, column=0, sticky=NSEW, padx=5, pady=5, columnspan=2)
        CTkEntry(self, justify=CENTER, state=DISABLED, textvariable=self.txt_compra, font=('arial', 16)).grid(row=4, column=0, sticky=EW, padx=5, pady=5, ipady=5, columnspan=2)

        self.txt_compra.set('20')

        cont_botones = CTkFrame(self, fg_color='#dbdbdb')
        cont_botones.grid(row=5, column=0, padx=5, pady=5, columnspan=2)

        CTkButton(cont_botones, text='Cancelar', font=('arial', 16, 'bold'), fg_color='blue', command=self.cancel).grid(row=0, column=0, padx=15, pady=5, ipadx=5, ipady=5)
        CTkButton(cont_botones, text='Comprar', font=('arial', 16, 'bold'), fg_color='blue', command=self.pagar).grid(row=0, column=1, padx=15, pady=5, ipadx=5, ipady=5)
        CTkButton(cont_botones, text='Facturar', font=('arial', 16, 'bold'), fg_color='blue').grid(row=0, column=2, padx=5, pady=5, ipadx=15, ipady=5)

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
            MensajeEmergente(self, 'Pago', 'Compra cancelada!!').mensaje_correcto()
