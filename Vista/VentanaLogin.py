from customtkinter import *
from Controlador import ctrlFunciones
from Modelo.Data_Base import session, Empleado
from Vista.FrameMenuPrincipal import FrameMenuPrincipal
from Vista.MensajeEmergente import MensajeEmergente

class Login(CTk):
    def __init__(self):
        super().__init__()
        self.session_empleado = {}
        set_appearance_mode("light")

        self.configure(fg_color='blue')
        self.title('Sistema de Taller Mecánico')
        self.geometry(f'300x455+{((self.winfo_screenwidth()) // 2)}+{((self.winfo_screenheight() - 500) // 2)}')
        self.resizable(False, False)

        self.columnconfigure(0, weight=1)

        self.session_empleado['rfc'] = 'self.rfc.get()'
        self.session_empleado['nombre'] = 'empleado.Nombre'
        self.session_empleado['logeado'] = True

        self.withdraw()
        menu_principal = CTkToplevel()
        menu_principal.session_empleado = self.session_empleado
        menu_principal.title('Sistema Taller Mecánico')
        menu_principal.geometry(
            f'1200x700+{((self.winfo_screenwidth() - 1000) // 2)}+{((self.winfo_screenheight() - 760) // 2)}')
        FrameMenuPrincipal(menu_principal).pack(fill='both', expand=True)

        self.cont_login = CTkFrame(self, fg_color='blue', corner_radius=20)
        self.cont_login.grid(row=0, column=0, ipady=20, pady=(0, 20))

        self.rfc = StringVar()
        self.contra = StringVar()

        self.show = BooleanVar()

        self._elementos_login()

    def _loggearse(self):
        if self.rfc.get()!='' and self.contra.get()!='':
            empleado = session.query(Empleado).filter(Empleado.RFC==self.rfc.get(), Empleado.Contrasenia==self.contra.get(),).first()
            if empleado:
                # Guardando la sesion
                self.session_empleado['rfc'] = self.rfc.get()
                self.session_empleado['nombre'] = empleado.Nombre
                self.session_empleado['logeado'] = True

                # Iniciando sesion
                self.withdraw()
                menu_principal = CTkToplevel()
                menu_principal.session_empleado = self.session_empleado
                menu_principal.title('Sistema Taller Mecánico')
                menu_principal.geometry(f'1200x700+{((self.winfo_screenwidth() - 1000) // 2)}+{((self.winfo_screenheight() - 760) // 2)}')
                FrameMenuPrincipal(menu_principal).pack(fill='both', expand=True)
            else:
                MensajeEmergente(self, 'Error', 'RFC o contraseña Incorrectos').mensaje_error()
        else:
            MensajeEmergente(self, 'Error', 'Por favor, llene todos los campos').mensaje_error()

    def _elementos_login(self):
        def unshow(e):
            entry_passwd.configure(show='*')
            self.show.set(False)

        def show(e):
            entry_passwd.configure(show='')

        label_logo = CTkLabel(self.cont_login, text='', image=ctrlFunciones.leer_imagen('../media/logo.png', (170, 170)))
        label_logo.grid(row=0, column=0, pady=(10, 0), columnspan=2)

        CTkLabel(self.cont_login, text="RFC", text_color='#dbdbdb', anchor=W, font=('arial', 18, 'bold')).grid(row=1, column=0, padx=(5, 0), pady=(10, 5), columnspan=2, sticky=EW)
        CTkEntry(self.cont_login, width=260, textvariable=self.rfc, fg_color='#dbdbdb', font=('arial', 16), justify='center', border_width=1.5, border_color='black').grid(row=2, column=0, pady=(0, 20), ipady=5, columnspan=2)

        CTkLabel(self.cont_login, text="Contraseña", text_color='#dbdbdb', anchor=W, font=('arial', 18, 'bold')).grid(row=3, column=0, padx=(5, 0), pady=(10, 5), columnspan=2, sticky=EW)
        check_show = CTkCheckBox(self.cont_login, text='Mostrar', text_color='#dbdbdb', font=('arial', 16, 'bold'), variable=self.show)
        check_show.bind('<ButtonPress-1>', show)
        check_show.bind('<ButtonRelease-1>', unshow)
        check_show.grid(row=3, column=1, pady=(5, 0), sticky=E)

        entry_passwd = CTkEntry(self.cont_login, width=260, textvariable=self.contra, fg_color='#dbdbdb', font=('arial', 16), justify='center', border_width=1.5, border_color='black', show='*')
        entry_passwd.grid(row=4, column=0, pady=(0, 20), ipady=5, columnspan=2)

        boton_login = CTkButton(self.cont_login, text='Iniciar Sesión', font=('arial', 16, 'bold'), text_color='black', fg_color='white', command=self._loggearse)
        boton_login.grid(row=5, column=0, ipadx=10, ipady=10, pady=(15, 5), columnspan=2, sticky=EW)

Login().mainloop()
