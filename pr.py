from tkinter import Tk
from Vista.MensajeEmergente import MensajeEmergente

root = Tk()
ans = MensajeEmergente(root, 'Error', 'Por favor. Llene todos los campos')
ans.mensaje_pregunta()
root.wait_window(ans)
print(ans.ans)
root.mainloop()
