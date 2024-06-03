from tkinter.ttk import Treeview
from tkinter import messagebox, ttk
from customtkinter import *
from tkinter import *
from PIL import Image, ImageTk

from Controlador.ctrlFunciones import color_fg
from Vista.Data_Base import session, Servicios, Contenido, Refacciones
from Vista.FrameAutomoviles import FrameAutomoviles
from Vista.MensajeEmergente import MensajeEmergente

class FramePagar(CTkFrame):
    def __init__(self, root, refacciones_carrito):
        super().__init__(root)
        self.root = root
        self.refacciones_carrito = refacciones_carrito
        CTkLabel(self, text='Total a Pagar', font=('arial', 25, 'bold')).pack(fill='x', pady=10)
        self.txt_compra = StringVar()

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

        # Agregando las refacciones al carrito
        self._cargar_catalago()

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

    def _cargar_catalago(self):
        # Realizar la consulta y obtener los resultados
        consulta = session.query(Servicios.Tipo_Servicio, Refacciones). \
            join(Contenido, Servicios.ID_servicio == Contenido.ID_Servicios). \
            join(Refacciones, Refacciones.ID_refacciones == Contenido.ID_Refacciones).where(Servicios.ID_servicio.in_(self.refacciones_carrito)).all()

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
