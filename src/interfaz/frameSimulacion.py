from tkinter import *

def frameSimulacion(ventana):
    # Crear el frame con las opciones de simulación
    frameSimulacion = Frame(ventana, width=600, height=300)
    frameSimulacion.place(x=650, y=50)

    # Crear label y scrollbar de estimulación
    labelEstimulacion = Label(frameSimulacion, text="Estimulación:", font=("Segoe UI", 12))
    labelEstimulacion.place(x=20, y=0)

    # Crear scrollbar
    estimulacionScrollbar = Scrollbar(frameSimulacion, orient='horizontal')
    estimulacionScrollbar.place(x=20, y=30)

    # Crear labels y opciones de estimulación
    # Tiempo de simulación
    labelTiempo = Label(frameSimulacion, text="Tiempo de Simulación:", font=("Segoe UI", 12))
    labelTiempo.place(x=20, y=60)

    paramTiempo = StringVar(None)
    paramTiempo = Entry(frameSimulacion, textvariable=paramTiempo, width=7)
    paramTiempo.place(x=240, y=65)

    labelMsTiempo = Label(frameSimulacion, text="ms", font=("Segoe UI", 12))
    labelMsTiempo.place(x=265, y=60)

    # Tiempo de inicio de estimulación
    labelTiempoInicio = Label(frameSimulacion, text="Tiempo de Inicio Estimulación:", font=("Segoe UI", 12))
    labelTiempoInicio.place(x=20, y=90)

    paramTiempoInicio = StringVar(None)
    paramTiempoInicio = Entry(frameSimulacion, textvariable=paramTiempoInicio, width=4)
    paramTiempoInicio.place(x=240, y=95)

    labelMsTiempoInicio = Label(frameSimulacion, text="ms", font=("Segoe UI", 12))
    labelMsTiempoInicio.place(x=265, y=90)