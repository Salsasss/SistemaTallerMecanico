from customtkinter import *
from tkinter import ttk, messagebox
from PIL import Image
from Modelo.Data_Base import Refacciones, session

class FrameRefaccionesAdmi(CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        CTkLabel(self, text='Agregar Refacción', font=('arial', 25, 'bold')).pack(pady=(0, 5), ipady=10)

        self.id_refaccion = StringVar()
        self.nombre_refaccion = StringVar()
        self.modelo = StringVar()
        self.cantidad = StringVar()
        self.costo = StringVar()

        self._elementos_refaccion()
        self._boton_submit()
        self._crear_treeview()
        self._cargar_datos()

    def _elementos_refaccion(self):
        img_path = "../media/carpeta.png"
        image = CTkImage(Image.open(img_path), size=(100, 100))

        info_refaccion = CTkFrame(self)
        info_refaccion.pack(fill='x', padx=10, pady=(0, 10), ipady=15, expand=False)

        CTkLabel(info_refaccion, text='Datos de la Refacción', font=('arial', 18, 'bold')).grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        CTkLabel(info_refaccion, width=135, text='ID Refacción: ', font=('arial', 16, 'bold'), anchor='e').grid(row=1, column=0, padx=5, pady=5)
        CTkEntry(info_refaccion, width=200, font=('arial', 16), textvariable=self.id_refaccion).grid(row=1, column=1, padx=(0, 10))

        CTkLabel(info_refaccion, width=135, text='Modelo: ', font=('arial', 16, 'bold'), anchor='e').grid(row=2, column=0, padx=5, pady=5)
        CTkEntry(info_refaccion, width=200, font=('arial', 16), textvariable=self.modelo).grid(row=2, column=1, padx=(0, 10))

        CTkLabel(info_refaccion, width=135, text='Costo: ', font=('arial', 16, 'bold'), anchor='e').grid(row=3, column=0, padx=5, pady=5)
        CTkEntry(info_refaccion, width=200, font=('arial', 16), textvariable=self.costo).grid(row=3, column=1, padx=(0, 10))

        CTkLabel(info_refaccion, width=135, text='Nombre Refacción: ', font=('arial', 16, 'bold'), anchor='e').grid(row=4, column=0, padx=5, pady=5)
        CTkEntry(info_refaccion, width=200, font=('arial', 16), textvariable=self.nombre_refaccion).grid(row=4, column=1, padx=(0, 10))

        CTkLabel(info_refaccion, width=135, text='Cantidad: ', font=('arial', 16, 'bold'), anchor='e').grid(row=1, column=2, padx=5, pady=5)
        CTkEntry(info_refaccion, width=200, font=('arial', 16), textvariable=self.cantidad).grid(row=1, column=3,)

        CTkLabel(info_refaccion, text='', image=image, padx=50).grid(row=2, column=3, rowspan=3, columnspan=2)

    def _boton_submit(self):
        buttons_frame = CTkFrame(self)
        buttons_frame.pack(fill='x', padx=10, pady=(0, 10), expand=False)

        CTkButton(buttons_frame, text='Guardar', text_color='white', fg_color='green', font=('arial', 16, 'bold'), command=self._guardar_refaccion).pack(side='left', padx=10, pady=5)
        CTkButton(buttons_frame, text='Modificar', text_color='white', fg_color='orange', font=('arial', 16, 'bold'), command=self._modificar_refaccion).pack(side='left', padx=10, pady=5)
        CTkButton(buttons_frame, text='Eliminar', text_color='white', fg_color='red', font=('arial', 16, 'bold'), command=self._eliminar_refaccion).pack(side='left', padx=10, pady=5)

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
            self.id_refaccion.set(values[0])
            self.nombre_refaccion.set(values[1])
            self.modelo.set(values[2])
            self.cantidad.set(values[3])
            self.costo.set(values[4])

    def _guardar_refaccion(self):
        try:
            existing_refaccion = session.query(Refacciones).filter_by(ID_refacciones=int(self.id_refaccion.get())).first()
            if existing_refaccion:
                messagebox.showerror("Error", "El ID de la refacción ya existe.")
            else:
                nueva_refaccion = Refacciones(
                    ID_refacciones=int(self.id_refaccion.get()),
                    NombreRefacciones=self.nombre_refaccion.get(),
                    Modelo=self.modelo.get(),
                    Cantidad=int(self.cantidad.get()),
                    Costo=float(self.costo.get())
                )
                session.add(nueva_refaccion)
                session.commit()
                messagebox.showinfo("Éxito", "Refacción guardada exitosamente.")
                self._cargar_datos()
        except Exception as e:
            session.rollback()
            messagebox.showerror("Error", f"Error al guardar: {e}")
        finally:
            self._limpiar_campos()

    def _modificar_refaccion(self):
        try:
            refaccion = session.query(Refacciones).filter_by(ID_refacciones=int(self.id_refaccion.get())).first()
            if refaccion:
                refaccion.NombreRefacciones = self.nombre_refaccion.get()
                refaccion.Modelo = self.modelo.get()
                refaccion.Cantidad = int(self.cantidad.get())
                refaccion.Costo = float(self.costo.get())
                session.commit()
                messagebox.showinfo("Éxito", "Refacción modificada exitosamente.")
                self._cargar_datos()
            else:
                messagebox.showerror("Error", "Refacción no encontrada.")
        except Exception as e:
            session.rollback()
            messagebox.showerror("Error", f"Error al modificar: {e}")
        finally:
            self._limpiar_campos()

    def _eliminar_refaccion(self):
        try:
            refaccion = session.query(Refacciones).filter_by(ID_refacciones=int(self.id_refaccion.get())).first()
            if refaccion:
                session.delete(refaccion)
                session.commit()
                messagebox.showinfo("Éxito", "Refacción eliminada exitosamente.")
                self._cargar_datos()
            else:
                messagebox.showerror("Error", "Refacción no encontrada.")
        except Exception as e:
            session.rollback()
            messagebox.showerror("Error", f"Error al eliminar: {e}")
        finally:
            self._limpiar_campos()

    def _limpiar_campos(self):
        self.id_refaccion.set("")
        self.nombre_refaccion.set("")
        self.modelo.set("")
        self.cantidad.set("")
        self.costo.set("")

#if __name__ == '__main__':
#    root = CTk()
#    frame = FrameRefaccionesAdmi(root)
#    frame.pack(fill='both', expand=True)
#    root.mainloop()
