from tkinter import *

from frameOpciones import frameOpciones
from frameSimulacion import frameSimulacion
from frameTabla import frameTabla


def main():
    # Crear la ventana principal
    ventana = Tk()
    ventana.title("Proyecto Programación Científica")
    ventana.geometry("1300x700")
    ventana.configure(background='#ffffff') #f0f0f0
    ventana.resizable(0, 0)

    # Crear titulo de la ventana
    titulo = Label(ventana, text='Modelo Neuronal de Izhikevich',  font=("Lato bold", 12))
    titulo.pack()

    # Crear el frame de matplotlib
    frameMatplot = Frame(ventana, width=600, height=300)
    frameMatplot.place(x=50, y=50)

    # Crear el frame de las opciones
    frameOpciones(ventana)

    # Crear el frame de la simulación
    frameSimulacion(ventana)
    
    # Crear el botón de cerrar
    botonCerrar = Button(ventana, text="X", command=ventana.destroy, height=2, width=4)
    botonCerrar.place(x=1250, y=0)

    ventana.mainloop()

if __name__ == "__main__":
    main()