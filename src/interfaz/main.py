import sys
from pathlib import Path
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)
from tkinter import Tk, Label, Button
from tkinter.messagebox import showerror, showinfo
from frameOpciones import frameOpciones
from frameSimulacion import frameSimulacion
from frameTabla import frameTabla
from frameMatplotLib import frameMatplotlib   
from logica.classes import ProgramGUIVariables
from logica.functions import simular, exportarDatos
import traceback


def report_callback_exception(self, exc, val, tb):
    """Función para sobreescribir las excepciones ocurridas durante la ejecución del programa
    """
    if isinstance(exc, KeyboardInterrupt):
        # Si se interrumpe el programa, se cierra el programa
        self.destroy()
        sys.exit()
    elif exc.__name__ == 'InvalidParameters':
        # Muestra la excepción que ocurrió como forma de errorbox
        showerror("Error", message=str(val))
    else:
        print(traceback.print_tb(tb))
        print(val)

def main():
    # Crear la ventana principal
    ventana = Tk()
    ventana.title("Proyecto Programación Científica")
    ventana.geometry("1300x800")
    ventana.configure(background='#f0f0f0') #f0f0f0
    ventana.resizable(0, 0)

    # Crear una instancia para guardar las variables de la interfaz
    datosInterfaz = ProgramGUIVariables()

    # Crear el frame de matplotlib
    canvas, subplot = frameMatplotlib(ventana)
    datosInterfaz.setMatplotlib(canvas, subplot)

    # Crear el frame de las opciones
    metodo1Var, metodo2Var, metodo3Var, metodo4Var, metodo5Var, variableV, variableU, paramABox, paramBBox, paramCBox, paramDBox, dropdown = frameOpciones(ventana)
    datosInterfaz.setMetodos(metodo1Var, metodo2Var, metodo3Var, metodo4Var, metodo5Var)
    datosInterfaz.setVariables(variableV, variableU)
    datosInterfaz.setParametros(paramABox, paramBBox, paramCBox, paramDBox)
    datosInterfaz.setDropdownOpciones(dropdown)

    # Crear el frame de la simulación
    estimulacionScrollbar, paramTiempo, paramTiempoInicio, paramTiempoFin = frameSimulacion(ventana, datosInterfaz)
    datosInterfaz.setEstimulacion(estimulacionScrollbar, paramTiempo, paramTiempoInicio, paramTiempoFin)

    # Crear el frame de la tabla
    tabla = frameTabla(ventana)
    datosInterfaz.setTabla(tabla)

    # Crear titulo de la ventana
    titulo = Label(ventana, text='Modelo Neuronal de Izhikevich',  font=("Segoe UI Bold", 20), width=500, height=1)
    titulo.pack()

    # Crear el botón de cerrar
    botonCerrar = Button(ventana, text="X", command=ventana.destroy, height=2, width=4)
    botonCerrar.place(x=1250, y=0)

    # Crear botones de simular y exportar
    # Crear botón de simular
    botonSimular = Button(ventana, text="Simular", command= lambda: simular(datosInterfaz), height=2, width=20)
    botonSimular.place(x=850, y=700)

    # Crear botón de exportar
    botonExportar = Button(ventana, text="Exportar", command=guardarDatos, height=2, width=20)
    botonExportar.place(x=1010, y=700)

    # Sobreescribir el método de atrapada de excepciones por defecto
    Tk.report_callback_exception = report_callback_exception
    ventana.mainloop()

def guardarDatos():
    # Exportar los datos al archivo binario
    exportarDatos()
    # Llamar a un popup para informar que se exportaron los datos
    showinfo("Archivo exportado", "Los datos se exportaron correctamente")


if __name__ == "__main__":
    main()