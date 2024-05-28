from tkinter import ttk
from customtkinter import *
from PIL import Image, ImageTk
from Modelo.Data_Base import obtener_refacciones

class FrameCataRefacciones(CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        CTkLabel(self, text='Catálogo de Refacciones', font=('arial', 25, 'bold')).pack(pady=(10, 0))

        self.texto_buscar = StringVar()
        self._elementos_herramientas()
        self._elementos_tabla()
        self._cargar_datos()

    def _elementos_herramientas(self):
        def buscar(e):
            if self.texto_buscar.get() == 'Buscar':
                self.texto_buscar.set('')

        def placeholder(e):
            if self.texto_buscar.get() == '':
                self.texto_buscar.set('Buscar')

        cont_herramientas = CTkFrame(self, fg_color='#dbdbdb')
        cont_herramientas.pack(fill='x', pady=10, padx=10)

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
        cont_tabla.pack(fill='both', padx=10, pady=(0, 20), expand=True)

        style = ttk.Style()
        style.configure('Treeview.Heading', background='blue', foreground='white', font=('arial', 16, 'bold'), padding=8)
        style.configure('Treeview', font=('arial', 16))

        scrollbar = ttk.Scrollbar(cont_tabla)
        scrollbar.pack(side='right', fill='y')
        self.serv = ttk.Treeview(cont_tabla, yscrollcommand=scrollbar.set)
        self.serv.pack(fill='both', expand=True)
        scrollbar.config(command=self.serv.yview)

        self.serv['columns'] = ('1', '2', '3', '4', '5')
        self.serv.column('#0', width=50, anchor=CENTER)
        self.serv.column('1', anchor=CENTER, width=40, minwidth=50)
        self.serv.column('2', anchor=CENTER, width=160)
        self.serv.column('3', anchor=CENTER, width=90)
        self.serv.column('4', anchor=CENTER, width=160)
        self.serv.column('5', anchor=CENTER, width=160)

        self.serv.heading('#0', text=' ')
        self.serv.heading('1', text='ID')
        self.serv.heading('2', text='Nombre')
        self.serv.heading('3', text='Modelo')
        self.serv.heading('4', text='Cantidad')
        self.serv.heading('5', text='Costo')

        self.images = {
            '1': ImageTk.PhotoImage(Image.open("../media/bombagasolinachevroler.png").resize((60, 95), Image.Resampling.LANCZOS)),
            '37': ImageTk.PhotoImage(Image.open("../media/bombagasolinaford550.png").resize((60, 95), Image.Resampling.LANCZOS)),
            '2': ImageTk.PhotoImage(Image.open("../media/bujiaschevrolet2012.png").resize((100, 95), Image.Resampling.LANCZOS)),
            '3': ImageTk.PhotoImage(Image.open("../media/cableschevrolet2012.png").resize((100, 90), Image.Resampling.LANCZOS)),
            '4': ImageTk.PhotoImage(Image.open("../media/valvulajackchevrolet2012.png").resize((60, 90), Image.Resampling.LANCZOS)),
            '5': ImageTk.PhotoImage(Image.open("../media/valvulapcvchevrolet2012.png").resize((100, 90), Image.Resampling.LANCZOS)),
            '6': ImageTk.PhotoImage(Image.open("../media/vmpassat2012.png").resize((90, 90), Image.Resampling.LANCZOS)),
            '8': ImageTk.PhotoImage(Image.open("../media/bmwmini2013.png").resize((120, 90), Image.Resampling.LANCZOS)),
            '22': ImageTk.PhotoImage(Image.open("../media/jeepwrangler2016.png").resize((90, 100), Image.Resampling.LANCZOS)),
            '26': ImageTk.PhotoImage(Image.open("../media/dodgeram2021.png").resize((110, 60), Image.Resampling.LANCZOS)),
            '47': ImageTk.PhotoImage(Image.open("../media/fordfiesta2016.png").resize((110, 60), Image.Resampling.LANCZOS)),
            '52': ImageTk.PhotoImage(Image.open("../media/mazda32018.png").resize((110, 60), Image.Resampling.LANCZOS)),
            '7': ImageTk.PhotoImage(Image.open("../media/balatasvwpassat2012.png").resize((120, 100), Image.Resampling.LANCZOS)),
            '9': ImageTk.PhotoImage(Image.open("../media/amortiguadoresnissanversa2014.png").resize((60, 90), Image.Resampling.LANCZOS)),
            '10': ImageTk.PhotoImage(Image.open("../media/depositoanticongelantechevroletspark2012.png").resize((80, 100), Image.Resampling.LANCZOS)),
            '15': ImageTk.PhotoImage(Image.open("../media/bieletasnissanversa2014.png").resize((107, 100), Image.Resampling.LANCZOS)),
            '17': ImageTk.PhotoImage(Image.open("../media/mangueramazda32010.png").resize((120, 60), Image.Resampling.LANCZOS)),
            '20': ImageTk.PhotoImage(Image.open("../media/jtofordfocussport2010.png").resize((120, 80), Image.Resampling.LANCZOS)),
            '30': ImageTk.PhotoImage(Image.open("../media/boostervwtransporter2015.png").resize((95, 95), Image.Resampling.LANCZOS)),
            '33': ImageTk.PhotoImage(Image.open("../media/terminalesnissanversa2014.png").resize((110, 90), Image.Resampling.LANCZOS)),
            '38': ImageTk.PhotoImage(Image.open("../media/cacahuatesnissanversa2014.png").resize((90, 90), Image.Resampling.LANCZOS)),
            '40': ImageTk.PhotoImage(Image.open("../media/aceitemineral.png").resize((60, 90), Image.Resampling.LANCZOS)),
            '42': ImageTk.PhotoImage(Image.open("../media/aceitesintetico.png").resize((60, 90), Image.Resampling.LANCZOS)),
            '61': ImageTk.PhotoImage(Image.open("../media/bobinanissanversa2014.png").resize((100, 100), Image.Resampling.LANCZOS)),
            '70': ImageTk.PhotoImage(Image.open("../media/rotulasnissanversa2014.png").resize((90, 90), Image.Resampling.LANCZOS)),
            '90': ImageTk.PhotoImage(Image.open("../media/anticongelanteverde.png").resize((80, 90), Image.Resampling.LANCZOS)),
            '91': ImageTk.PhotoImage(Image.open("../media/anticongelantenaranja.png").resize((60, 90), Image.Resampling.LANCZOS)),
            '92': ImageTk.PhotoImage(Image.open("../media/anticongelanteamarillo.png").resize((80, 90), Image.Resampling.LANCZOS)),
            '93': ImageTk.PhotoImage(Image.open("../media/anticongelanteturquesa.png").resize((80, 90), Image.Resampling.LANCZOS)),
            '94': ImageTk.PhotoImage(Image.open("../media/anticongelanterosa.png").resize((60, 90), Image.Resampling.LANCZOS)),
            '95': ImageTk.PhotoImage(Image.open("../media/anticongelantepurpura.png").resize((80, 90), Image.Resampling.LANCZOS))
        }

    def _cargar_datos(self):
        refacciones = obtener_refacciones()
        agrupar_refacciones = {}

        for refaccion in refacciones:
            nombre = refaccion[1]
            if nombre not in agrupar_refacciones:
                agrupar_refacciones[nombre] = []
            agrupar_refacciones[nombre].append(refaccion)

        for nombre, refacciones in agrupar_refacciones.items():
            parent_id = self.serv.insert('', 'end', text='', values=('', nombre, '', '', ''))
            for refaccion in refacciones:
                id_ = refaccion[0]
                modelo = refaccion[2]
                cantidad = refaccion[3]
                costo = refaccion[4]
                img_key = str(id_)
                image = self.images.get(img_key)

                if image is None:
                    self.serv.insert(parent_id, 'end', text='', values=(id_, '', modelo, cantidad, costo), tags=('nested',))
                else:
                    self.serv.insert(parent_id, 'end', text='', image=image, values=(id_, '', modelo, cantidad, costo), tags=('nested',))

        self.serv.tag_configure('nested', background='#F3F3F3')

#if __name__ == '__main__':
#    root = CTk()
#    frame = FrameCataRefacciones(root)
#    frame.pack(fill='both', expand=True)
#    root.mainloop()
