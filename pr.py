import tkinter as tk


class CustomLabelFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.title = kwargs.get('title', 'LabelFrame')

        # Crear un borde y un título usando un Label
        self.border_label = tk.Label(self, text=self.title, relief="groove", bd=2)
        self.border_label.pack(side="top", fill="x")

        # Espacio para agregar otros widgets
        self.inner_frame = tk.Frame(self)
        self.inner_frame.pack(fill="both", expand=True)

    def add_widget(self, widget):
        widget.pack(in_=self.inner_frame, padx=5, pady=5)


# Ejemplo de uso
root = tk.Tk()
root.title("Ejemplo de CustomLabelFrame")

# Crear un CustomLabelFrame con un título personalizado
custom_label_frame = CustomLabelFrame(root)
custom_label_frame.pack(padx=10, pady=10)

# Agregar widgets al CustomLabelFrame
label = tk.Label(custom_label_frame.inner_frame, text="Este es un label dentro del CustomLabelFrame")
button = tk.Button(custom_label_frame.inner_frame, text="Este es un botón dentro del CustomLabelFrame")

custom_label_frame.add_widget(label)
custom_label_frame.add_widget(button)

root.mainloop()
