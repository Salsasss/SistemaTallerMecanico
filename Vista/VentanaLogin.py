from customtkinter import *
from Controlador import ctrlFunciones
from Vista.FrameMenuPrincipal import FrameMenuPrincipal

class Login(CTk):
    def __init__(self):
        super().__init__()
        set_appearance_mode("light")

        self.configure(fg_color='white')
        self.title('Sistema de Taller Mecánico')
        self.geometry(f'300x450+{((self.winfo_screenwidth()) // 2)}+{((self.winfo_screenheight() - 500) // 2)}')

        self.columnconfigure(0, weight=1)

        self.cont_login = CTkFrame(self, fg_color='white', corner_radius=20)
        self.cont_login.grid(row=0, column=0, ipady=20, pady=(0, 20))

        self.show = BooleanVar()

        self._elementos_login()

    def _loggearse(self):
        '''''
        if usuario y contraseña correctos:
            pass
        else:
            MensajeEmergente(self, 'Error', 'Usuario o Contraseña Incorrectos').mensaje_error()
        '''''
        self.withdraw()
        menu_principal = CTkToplevel()
        menu_principal.geometry(f'1000x700+{((self.winfo_screenwidth() - 1000) // 2)}+{((self.winfo_screenheight() - 760) // 2)}')
        FrameMenuPrincipal(menu_principal).pack(fill='both', expand=True)

    def _elementos_login(self):
        def unshow(e):
            entry_passwd.configure(show='*')
            self.show.set(False)

        def show(e):
            entry_passwd.configure(show='')

        label_logo = CTkLabel(self.cont_login, image=ctrlFunciones.leer_imagen('../media/logo.jpg', (150, 150)))
        label_logo.grid(row=0, column=0, pady=10, columnspan=2)

        CTkLabel(self.cont_login, text="Empleado", text_color='black', anchor=W, font=('arial', 18, 'bold')).grid(row=1, column=0, padx=(5, 0), pady=(10, 5), columnspan=2, sticky=EW)
        CTkEntry(self.cont_login, width=260, fg_color='#dbdbdb', font=('arial', 16)).grid(row=2, column=0, pady=(0, 20), ipady=5, columnspan=2)

        CTkLabel(self.cont_login, text="Contraseña", text_color='black', anchor=W, font=('arial', 18, 'bold')).grid(row=3, column=0, padx=(5, 0), pady=(10, 5), columnspan=2, sticky=EW)
        check_show = CTkCheckBox(self.cont_login, text='Mostrar', font=('arial', 16, 'bold'), variable=self.show)
        check_show.bind('<ButtonPress-1>', show)
        check_show.bind('<ButtonRelease-1>', unshow)
        check_show.grid(row=3, column=1, pady=(5, 0), sticky=E)

        entry_passwd = CTkEntry(self.cont_login, width=260, fg_color='#dbdbdb', font=('arial', 16), show='*')
        entry_passwd.grid(row=4, column=0, pady=(0, 20), ipady=5, columnspan=2)

        CTkButton(self.cont_login, text='Iniciar Sesión', font=('arial', 16, 'bold'), fg_color='blue', command=self._loggearse).grid(row=5, column=0, ipadx=10, ipady=10, pady=(15, 5), columnspan=2, sticky=EW)

lg = Login()
lg.mainloop()
