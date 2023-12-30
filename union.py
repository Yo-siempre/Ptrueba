## https://www.youtube.com/watch?v=hTUJC8HsC2I
## pluma icono cambio logo
from tkinter import*


raiz=Tk()


raiz.title("Ventana de Prueba")
raiz.iconbitmap("ELPROGRAMADOR.ico")



##raiz.mainloop()


from datetime import datetime
import tkinter as tk
INTERVALO_REFRESCO_RELOJ = 300  # En milisegundos


def obtener_hora_actual():
    return datetime.now().strftime("%H:%M:%S")


def refrescar_reloj():
##    print("Refrescando!")
    variable_hora_actual.set(obtener_hora_actual())
    raiz.after(INTERVALO_REFRESCO_RELOJ, refrescar_reloj)


raiz = tk.Tk()
variable_hora_actual = tk.StringVar(raiz, value=obtener_hora_actual())
raiz.etiqueta = tk.Label(
    raiz, textvariable=variable_hora_actual, font=f"Consolas 60")
raiz.etiqueta.pack(side="top")
app = tk.Frame()
raiz.title("Este Reloj, fue Creado en Python.")


raiz.iconbitmap("ELPROGRAMADOR.ico")


refrescar_reloj()
app.pack()
app.mainloop()


raiz.mainloop()
