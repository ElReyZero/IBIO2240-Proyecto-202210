from tkinter import Frame, StringVar, Entry, Button, Scale, Label, HORIZONTAL

def frameSimulacion(ventana):
    # Crear el frame con las opciones de simulación
    xInicial = 100

    frameSimulacion = Frame(ventana, width=600, height=300)
    frameSimulacion.place(x=650, y=50)

    # Crear label y scrollbar de estimulación
    labelEstimulacion = Label(frameSimulacion, text="Estimulación:", font=("Segoe UI", 12))
    labelEstimulacion.place(x=xInicial, y=0)

    # Crear scrollbar
    label1Scrollbar = Label(frameSimulacion, text="-100mA", font=("Segoe UI", 12))
    label1Scrollbar.place(x=20, y=40)
    estimulacionScrollbar = Scale(frameSimulacion, from_=-100, to=100, orient=HORIZONTAL, length=270)
    estimulacionScrollbar.place(x=90, y=25)
    label2Scrollbar = Label(frameSimulacion, text="100mA", font=("Segoe UI", 12))
    label2Scrollbar.place(x=360, y=40)

    # Crear labels y opciones de estimulación
    # Tiempo de simulación
    labelTiempo = Label(frameSimulacion, text="Tiempo de Simulación:", font=("Segoe UI", 12))
    labelTiempo.place(x=xInicial, y=70)

    paramTiempo = StringVar(None)
    paramTiempo = Entry(frameSimulacion, textvariable=paramTiempo, width=7)
    paramTiempo.place(x=xInicial+220, y=75)

    labelMsTiempo = Label(frameSimulacion, text="ms", font=("Segoe UI", 12))
    labelMsTiempo.place(x=xInicial+245, y=70)

    # Tiempo de inicio de estimulación
    labelTiempoInicio = Label(frameSimulacion, text="Tiempo de Inicio Estimulación:", font=("Segoe UI", 12))
    labelTiempoInicio.place(x=xInicial, y=100)

    paramTiempoInicio = StringVar(None)
    paramTiempoInicio = Entry(frameSimulacion, textvariable=paramTiempoInicio, width=4)
    paramTiempoInicio.place(x=xInicial+220, y=105)

    labelMsTiempoInicio = Label(frameSimulacion, text="ms", font=("Segoe UI", 12))
    labelMsTiempoInicio.place(x=xInicial+245, y=100)

    # Tiempo de fin de estimulación
    labelTiempoFin = Label(frameSimulacion, text="Tiempo de Fin Estimulación:", font=("Segoe UI", 12))
    labelTiempoFin.place(x=xInicial, y=130)

    paramTiempoFin = StringVar(None)
    paramTiempoFin = Entry(frameSimulacion, textvariable=paramTiempoFin, width=4)
    paramTiempoFin.place(x=xInicial+220, y=135)

    labelMsTiempoFin = Label(frameSimulacion, text="ms", font=("Segoe UI", 12))
    labelMsTiempoFin.place(x=xInicial+245, y=130)

    # Valor de la estimulación
    labelValor = Label(frameSimulacion, text="Valor de la Estimulación:", font=("Segoe UI", 12))
    labelValor.place(x=xInicial, y=160)

    paramValor = StringVar(None)
    paramValor = Entry(frameSimulacion, textvariable=paramValor, width=7)
    paramValor.place(x=xInicial+220, y=165)

    labelMaValor = Label(frameSimulacion, text="mA", font=("Segoe UI", 12))
    labelMaValor.place(x=xInicial+245, y=160)

    # Crear botón de carga de datos
    botonCargar = Button(frameSimulacion, text="Cargar Datos", command=None, height=2, width=20)
    botonCargar.place(x=400, y=230)

    # Retornar todas las variables
    return estimulacionScrollbar, paramTiempo, paramTiempoInicio, paramTiempoFin, paramValor