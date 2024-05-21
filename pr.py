from tkinter import *
from tkinter.ttk import Treeview

listaAmigosBellaKath=[
    ("PesoPluma","bailasola"),
    ("ElBogueto","boguetito"),
    ("KalyUchis","Uchisuchis"),
    ("Anita","takisconchile")
]

listaUsuarios=[("SantaFe","1234"),
               ("BellaKath","bellita"),
               ("DonOmar", "omarcin"),
               ("Belinda", "gokufase2"),
               ("TaylorSwift", "ganamosNFL"),
               ("DanyFlow", "ternurita"),
               ("Ozuna", "ojitosclaritos"),
               ]

def muestraSeleccion(evento):
    print("Mostrar seleccion")
    f=tv.focus_get().selection()
    print(f)
    elemento=f[0]
    print(tv.item(elemento)['values'])

root=Tk()
tv=Treeview(root,columns=("c1","c2"))
tv.heading("#0",text="ID")
tv.heading("c1",text="USUARIOS")
tv.heading("c2",text="PASSWORDS")
tv.tag_configure("azulito",background="light blue",font=("Arial",15))
tv.tag_configure("verdecito",background="light green",font=("Arial",15))
tv.pack()
contador=0
for item in listaUsuarios:
    contador+=1
    if contador%2==0:
        tv.insert("",END,text=str(contador),values=(item[0],item[1]),tags=['azulito'])
    else:
        tv.insert("", END, text=str(contador), values=(item[0], item[1]), tags=['verdecito'])

for item in listaAmigosBellaKath:
    contador+=1
    tv.insert("I002", END, text=str(contador), values=(item[0], item[1]))

listadoObjetos=tv.get_children()
print(listadoObjetos)
#tv.delete(listadoObjetos[2])

#for elemento in listadoObjetos:
#    tv.delete(elemento)
tv.selection_set(["I003","I004","I005"])
datosSeleccionados=tv.selection()
for valores in datosSeleccionados:
    print(tv.item(valores)['values'])

tv.bind("<<TreeviewSelect>>", muestraSeleccion)

root.mainloop()