from tkinter import Tk, Label, Button

from frameOpciones import frameOpciones
from frameSimulacion import frameSimulacion
from frameTabla import frameTabla
from frameMatplotLib import frameMatplotlib      

def main():
    # Crear la ventana principal
    ventana = Tk()
    ventana.title("Proyecto Programación Científica")
    ventana.geometry("1300x800")
    ventana.configure(background='#f0f0f0') #f0f0f0
    ventana.resizable(0, 0)

    # Crear el frame de matplotlib
    frameMatplotlib(ventana)

    # Crear el frame de las opciones
    frameOpciones(ventana)

    # Crear el frame de la simulación
    frameSimulacion(ventana)

    # Crear el frame de la tabla
    frameTabla(ventana)
    
    # Crear titulo de la ventana
    titulo = Label(ventana, text='Modelo Neuronal de Izhikevich',  font=("Segoe UI Bold", 20), width=500, height=1)
    titulo.pack()

    # Crear el botón de cerrar
    botonCerrar = Button(ventana, text="X", command=ventana.destroy, height=2, width=4)
    botonCerrar.place(x=1250, y=0)

    # Crear botones de simular y exportar
    # Crear botón de simular
    botonSimular = Button(ventana, text="Simular", command=None, height=2, width=20)
    botonSimular.place(x=850, y=700)

    # Crear botón de exportar
    botonExportar = Button(ventana, text="Exportar", command=None, height=2, width=20)
    botonExportar.place(x=1010, y=700)

    ventana.mainloop()

if __name__ == "__main__":
    main()