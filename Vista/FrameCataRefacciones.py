from tkinter import ttk, messagebox
from customtkinter import *
from PIL import Image, ImageTk

from Controlador.ctrlFunciones import color_fg
from Data_Base import obtener_refacciones, obtener_servicios
from Data_Base import session, Refacciones,Contenido, Servicios

class FrameCataRefacciones(CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        CTkLabel(self, text='Servicios Realizados al Vehiculo', font=('arial', 25, 'bold')).pack(pady=(10, 0))

        style = ttk.Style()
        style.configure('Treeview.Heading', background='blue', foreground='white', font=('arial', 16, 'bold'), padding=8)
        style.configure('Treeview', font=('arial', 16), rowheight=35)

        self.texto_buscar = StringVar()
        self.refacciones_carrito = []

        self._elementos_herramientas()
        self._elementos_tabla()
        self._cargar_catalago()
        self._elementos_carrito()
        self._boton_submit()

    def _boton_submit(self):
        def ir_pagar():
            for widget in self.root.pack_slaves():
                widget.pack_forget()
            from Vista.FramePagar import FramePagar
            FramePagar(self.root, self.refacciones_carrito).pack(padx=10, pady=10, fill='both', expand=True)

        boton_submit = CTkButton(self, text='Ir a Pagar', font=('arial', 16, 'bold'), fg_color='#1e8b1e', command=ir_pagar)
        boton_submit.pack(side='right', padx=10, pady=(0, 10), ipadx=5, ipady=5)
        boton_submit.bind('<Enter>', lambda event: color_fg(event, boton=boton_submit, color='#125412'))
        boton_submit.bind('<Leave>', lambda event: color_fg(event, boton=boton_submit, color='#1e8b1e'))

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

    def _elementos_tabla(self):
        cont_tabla = CTkFrame(self)
        cont_tabla.pack(fill='x', padx=10, pady=(0, 20), expand=False)

        scrollbar = ttk.Scrollbar(cont_tabla)
        scrollbar.pack(side='right', fill='y')
        self.catalago = ttk.Treeview(cont_tabla, height=8, yscrollcommand=scrollbar.set)
        self.catalago.pack(fill='both', expand=True)
        scrollbar.config(command=self.catalago.yview)

        self.catalago['columns'] = ('1', '2', '3', '4', '5', '6')
        self.catalago.column('#0', width=50, anchor=CENTER)
        self.catalago.column('1', anchor=CENTER, width=100)
        self.catalago.column('2', anchor=CENTER, width=80)
        self.catalago.column('3', anchor=CENTER, width=100)
        self.catalago.column('4', anchor=CENTER, width=160)
        self.catalago.column('5', anchor=CENTER, width=100)
        self.catalago.column('6', anchor=CENTER, width=100)

        self.catalago.heading('#0', text='')
        self.catalago.heading('1', text='Servicio')
        self.catalago.heading('2', text='ID')
        self.catalago.heading('3', text='Nombre')
        self.catalago.heading('4', text='Modelo')
        self.catalago.heading('5', text='Cantidad')
        self.catalago.heading('6', text='Costo')
        self.catalago.bind("<Double-1>", self.on_double_click)
        self.seleccionados = []

        self.images = {
            '65': ImageTk.PhotoImage(Image.open(
                "../media/bombagasolinachevroler.png").resize((60, 95), Image.Resampling.LANCZOS)),
            '58': ImageTk.PhotoImage(Image.open(
                "../media/bateria.png").resize((60, 95), Image.Resampling.LANCZOS)),
            '6': ImageTk.PhotoImage(Image.open(
                "../media/bujiaschevrolet2012.png").resize((100, 95), Image.Resampling.LANCZOS)),
            '10': ImageTk.PhotoImage(Image.open(
                "../media/cableschevrolet2012.png").resize((100, 90), Image.Resampling.LANCZOS)),
            '9': ImageTk.PhotoImage(Image.open(
                "../media/valvulajackchevrolet2012.png").resize((60, 90), Image.Resampling.LANCZOS)),
            '12': ImageTk.PhotoImage(Image.open(
                "../media/frenos.png").resize((100, 90), Image.Resampling.LANCZOS)),
            '72': ImageTk.PhotoImage(Image.open(
                "../media/vmpassat2012.png").resize((90, 90), Image.Resampling.LANCZOS)),
            '2': ImageTk.PhotoImage(Image.open(
                "../media/bmwmini2013.png").resize((120, 90), Image.Resampling.LANCZOS)),
            '81': ImageTk.PhotoImage(Image.open(
                "../media/jeepwrangler2016.png").resize((90, 100), Image.Resampling.LANCZOS)),
            '48': ImageTk.PhotoImage(Image.open(
                "../media/dodgeram2021.png").resize((110, 60), Image.Resampling.LANCZOS)),
            '1': ImageTk.PhotoImage(Image.open(
                "../media/fordfiesta2016.png").resize((110, 60), Image.Resampling.LANCZOS)),
            '57': ImageTk.PhotoImage(Image.open(
                "../media/ventilador.png").resize((110, 60), Image.Resampling.LANCZOS)),
            '31': ImageTk.PhotoImage(Image.open(
                "../media/balatasvwpassat2012.png").resize((120, 100), Image.Resampling.LANCZOS)),
            '19': ImageTk.PhotoImage(Image.open(
                "../media/amortiguadoresnissanversa2014.png").resize((60, 90), Image.Resampling.LANCZOS)),
            '55': ImageTk.PhotoImage(Image.open(
                "../media/depositoanticongelantechevroletspark2012.png").resize((80, 100), Image.Resampling.LANCZOS)),
            '20': ImageTk.PhotoImage(Image.open(
                "../media/bieletasnissanversa2014.png").resize((107, 100), Image.Resampling.LANCZOS)),
            '53': ImageTk.PhotoImage(Image.open(
                "../media/mangueramazda32010.png").resize((120, 60), Image.Resampling.LANCZOS)),
            '7': ImageTk.PhotoImage(Image.open(
                "../media/jtofordfocussport2010.png").resize((120, 80), Image.Resampling.LANCZOS)),
            '18': ImageTk.PhotoImage(Image.open(
                "../media/boostervwtransporter2015.png").resize((95, 95), Image.Resampling.LANCZOS)),
            '21': ImageTk.PhotoImage(Image.open(
                "../media/terminalesnissanversa2014.png").resize((110, 90), Image.Resampling.LANCZOS)),
            '17': ImageTk.PhotoImage(Image.open(
                "../media/cacahuatesnissanversa2014.png").resize((90, 90), Image.Resampling.LANCZOS)),
            '3': ImageTk.PhotoImage(Image.open(
                "../media/aceitemineral.png").resize((60, 90), Image.Resampling.LANCZOS)),
            '4': ImageTk.PhotoImage(Image.open(
                "../media/aceitesintetico.png").resize((60, 90), Image.Resampling.LANCZOS)),
            '68': ImageTk.PhotoImage(Image.open(
                "../media/bobinanissanversa2014.png").resize((100, 100), Image.Resampling.LANCZOS)),
            '16': ImageTk.PhotoImage(Image.open(
                "../media/rotulasnissanversa2014.png").resize((90, 90), Image.Resampling.LANCZOS)),
            '15': ImageTk.PhotoImage(Image.open(
                "../media/embrague.png").resize((80, 90), Image.Resampling.LANCZOS)),
            '5': ImageTk.PhotoImage(Image.open(
                "../media/anticongelantenaranja.png").resize((60, 90), Image.Resampling.LANCZOS)),
            '56': ImageTk.PhotoImage(Image.open(
                "../media/anticongelantepurpura.png").resize((80, 90), Image.Resampling.LANCZOS))
        }

    def _elementos_carrito(self):
        cont_tabla = CTkFrame(self)
        cont_tabla.pack(fill='x', padx=10, pady=(0, 20), expand=False)

        scrollbar = ttk.Scrollbar(cont_tabla)
        scrollbar.pack(side='right', fill='y')
        self.carrito = ttk.Treeview(cont_tabla, height=7, yscrollcommand=scrollbar.set)
        self.carrito.pack(fill='both', expand=True)
        scrollbar.config(command=self.carrito.yview)

        self.carrito['columns'] = ('1', '2')
        self.carrito.column('#0', anchor=CENTER, width=80)
        self.carrito.column('1', anchor=CENTER, width=160)
        self.carrito.column('2', anchor=CENTER, width=90)

        self.carrito.heading('#0', text='ID')
        self.carrito.heading('1', text='Servicio')
        self.carrito.heading('2', text='Costo')

    def on_double_click(self, event):
        item = self.catalago.focus()
        servicio = self.catalago.item(item,'values')
        response = messagebox.askquestion("Agregar Servicio?", f"Servicio: {servicio[0]}")
        if response == "yes":
            find_service = session.query(Servicios).where(Servicios.Tipo_Servicio.like(f"{servicio[0]}")).first()
            self.refacciones_carrito.append(find_service.ID_servicio)
            self.carrito.insert('','end', text=find_service.ID_servicio, values=(find_service.Tipo_Servicio,find_service.Costo_Servicio))

    def _cargar_catalago(self):
        # Realizar la consulta y obtener los resultados
        consulta = session.query(Servicios.Tipo_Servicio, Refacciones). \
            join(Contenido, Servicios.ID_servicio == Contenido.ID_Servicios). \
            join(Refacciones, Refacciones.ID_refacciones == Contenido.ID_Refacciones).all()

        # Limpiar el Treeview existente
        for item in self.catalago.get_children():
            self.catalago.delete(item)

        # Agrupar refacciones por servicio
        agrupar_refacciones = {}
        for servicio, refaccion in consulta:
            nombre = servicio
            if nombre not in agrupar_refacciones:
                agrupar_refacciones[nombre] = []
            agrupar_refacciones[nombre].append(refaccion)

        # Insertar datos en el Treeview
        for servicio, refacciones in agrupar_refacciones.items():
            parent_id = self.catalago.insert('', 'end', text='', values=(servicio, '', '', '', '', ''))
            print(servicio)
            for refaccion in refacciones:
                id_refaccion = refaccion.ID_refacciones
                nombre_refaccion = refaccion.NombreRefacciones
                modelo = refaccion.Modelo
                cantidad = refaccion.Cantidad
                costo_refaccion = refaccion.Costo
                img_key = str(id_refaccion)
                image = self.images.get(img_key)

                if image is None:
                    self.catalago.insert(parent_id, 'end', text='', values=('', id_refaccion, nombre_refaccion, modelo, cantidad, costo_refaccion), tags=('nested',))
                else:
                    self.catalago.insert(parent_id, 'end', text='', image=image, values=('', id_refaccion, nombre_refaccion, modelo, cantidad, costo_refaccion), tags=('nested',))

        self.catalago.tag_configure('nested', background='#F3F3F3')
