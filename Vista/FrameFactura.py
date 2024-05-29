from tkinter.ttk import Treeview
from tkinter import messagebox, ttk
from customtkinter import *
from tkinter import *

from Vista.MensajeEmergente import MensajeEmergente


class FrameFactura(CTkFrame):
    def __init__(self, root):
        super().__init__(root)

        self.entry_buscar = CTkEntry(self, width=590, justify=CENTER, font=('arial', 16), border_width=2, border_color='blue', corner_radius=10)
        self.entry_buscar.grid(row=0, column=0, padx=5, pady=5, ipady=5)

        bnt_buscarCliente = CTkButton(self, text="Buscar", fg_color='blue', font=('arial', 16, 'bold'))
        bnt_buscarCliente.grid(row=0, column=1, padx=5, pady=5, ipadx=5, ipady=5)

        style = ttk.Style()
        style.configure('Treeview.Heading', background='blue', foreground='white', font=('arial', 16, 'bold'), padding=8)
        style.configure('Treeview', font=('arial', 16), rowheight=35)

        self.tree_cliente = Treeview(self, columns=("nombre", "direccion", "telefono"))
        self.tree_compra = Treeview(self, columns=("s/p", "cantidad", "precio"))

        headings_clientes = [("#0", "ID"), ("nombre", "NOMBRE"), ("direccion", "DIRECCION"), ("telefono", "Telfono")]
        headings_compra = [("#0", "ID"), ("s/p", "REFACCIONES O SERVICIOS"), ("cantidad", "CANTIDAD"), ("precio", "PRECIO")]

        for heading in headings_clientes:
            self.tree_cliente.heading(heading[0], text=heading[1])
            self.tree_cliente.column(heading[0], anchor=CENTER, width=200)

        for heading in headings_compra:
            self.tree_compra.heading(heading[0], text=heading[1])
            self.tree_compra.column(heading[0], anchor=CENTER, width=200)

        listaUsers = [("Yerimua", "Traakaaa", "3"), ("BellaKat", "Kbonitos0J0s", "3"), ("Tochika", "Tokio0J0s", "3"), ("LunaBella", "LuNabella69", "3")]

        cont = 0
        for user in listaUsers:
            cont += 1
            self.tree_cliente.insert("", END, text=str(cont), values=(user[0], user[1], user[2]))
            self.tree_compra.insert("", END, text=str(cont), values=(user[0], user[1], user[2]))

        cont = 0
        for user in listaUsers:
            cont += 1
            self.tree_cliente.insert("", END, text=str(cont), values=(user[0], user[1], user[2]))
            self.tree_compra.insert("", END, text=str(cont), values=(user[0], user[1], user[2]))

        self.tree_cliente.grid(row=1, column=0, sticky=EW, padx=10, pady=5, columnspan=2)

        self.entry_buscarCliente = CTkEntry(self, width=590, justify=CENTER, font=('arial', 16), border_width=2, border_color='blue', corner_radius=10)
        self.entry_buscarCliente.grid(row=2, column=0, padx=5, pady=5, ipady=5)

        bnt_buscarOrden = CTkButton(self, text="Buscar", fg_color='blue', font=('arial', 16, 'bold'))
        bnt_buscarOrden.grid(row=2, column=1, padx=5, pady=5, ipadx=5, ipady=5)

        self.tree_compra.grid(row=3, column=0, sticky=EW, padx=10, pady=5, columnspan=2)

        cont_botones = CTkFrame(self, fg_color='#dbdbdb')
        cont_botones.grid(row=4, column=0, padx=5, pady=5, columnspan=2)

        btn_cancelar = CTkButton(cont_botones, text="Cancelar", fg_color='blue', font=('arial', 16, 'bold'), command=self.cancel)
        btn_cancelar.grid(row=4, column=0, padx=15, pady=5, ipadx=5, ipady=5)

        btn_factura = CTkButton(cont_botones, text="Facturar", fg_color='blue', font=('arial', 16, 'bold'), command=self.facturar)
        btn_factura.grid(row=4, column=1, padx=15, pady=5, ipadx=5, ipady=5)

    def facturar(self):
        ans = MensajeEmergente(self, 'Factura', '¿Desea concretar la factura?')
        ans.mensaje_pregunta()
        self.wait_window(ans)
        if ans.ans:
            MensajeEmergente(self, 'Factura', 'Factura terminada con exito!').mensaje_correcto()

    def cancel(self):
        ans = MensajeEmergente(self, 'Cancelar', '¿Desea cancelar la factura?')
        ans.mensaje_pregunta()
        self.wait_window(ans)
        if ans.ans:
            MensajeEmergente(self, 'Cancelar', 'Factura cancelada con exito!').mensaje_correcto()
