import tkinter as tk

def onFocusOut(event):
    print("La ventana ha perdido el foco.")

def onFocusIn(event):
    print("La ventana ha obtenido el foco.")

root = tk.Tk()
root.bind("<FocusOut>", onFocusOut)
root.bind("<FocusIn>", onFocusIn)

root.mainloop()
