from .classes import Solution, SaveData
from .exceptions import InvalidParameters
from  datetime import datetime

# Variable global que almacena la última gráfica por si se quiere guardar
LATEST_PLOT= None

def graficar(solucion, subplot, canvas, V, U, eulerAdelante, eulerAtras, eulerModificado, rungeKutta2, rungeKutta4):
    # Se limpia el canvas
    subplot.clear()

    # Se guardan variables para la posible persistencia de los datos
    vFor = None
    uFor = None
    vBack = None
    uBack = None
    vMod = None
    uMod = None
    vRK2 = None
    uRK2 = None
    vRK4 = None
    uRK4 = None

    if eulerAdelante:
        tiempo, vFor, uFor = solucion.solveEulerForward()
        if V:
            subplot.plot(tiempo, vFor, label='Euler Adelante - V(t)')
        if U:
            subplot.plot(tiempo, uFor, label='Euler Adelante - U(t)')
        if not V and not U:
            raise InvalidParameters("Es necesario seleccionar una función para resolver")
    if eulerAtras:
        pass
        #tiempo, vBack, uBack = solucion.solveEulerBackward()
        #if V:
            #subplot.plot(tiempo, vBack, label='Euler Atras - V(t)')
        #if U:
            #subplot.plot(tiempo, uBack, label='Euler Atras - U(t)')
        #if not V and not U:
            #raise InvalidParameters("Es necesario seleccionar una función para resolver")
    if eulerModificado:
        pass
        #tiempo, vMod, uMod = solucion.solveEulerModified()
        #if V:
            #subplot.plot(tiempo, vMod, label='Euler Modificado - V(t)')
        #if U:
            #subplot.plot(tiempo, uMod, label='Euler Modificado - U(t)')
        #if not V and not U:
            #raise InvalidParameters("Es necesario seleccionar una función para resolver")
    if rungeKutta2:
        pass
        #tiempo, vRK2, uRK2 = solucion.solveRungeKutta2()
        #if V:
            #subplot.plot(tiempo, vRK2, label='Runge Kutta 2 - V(t)')
        #if U:
            #subplot.plot(tiempo, uRK2, label='Runge Kutta 2 - U(t)')
        #if not V and not U:
            #raise InvalidParameters("Es necesario seleccionar una función para resolver")
    if rungeKutta4:
        pass
        #tiempo, vRK4, uRK4 = solucion.solveRungeKutta4()
        #if V:
            #subplot.plot(tiempo, vRK4, label='Runge Kutta 4 - V(t)')
        #if U:
            #subplot.plot(tiempo, uRK4, label='Runge Kutta 4 - U(t)')
        #if not V and not U:
            #raise InvalidParameters("Es necesario seleccionar una función para resolver")
    if not eulerAdelante and not eulerAtras and not eulerModificado and not rungeKutta2 and not rungeKutta4:
        raise InvalidParameters("No se seleccionó ningún método")
    subplot.legend()
    canvas.draw()

    # Se guarda la gráfica en una variable por si el usuario la quiere persistir
    global LATEST_PLOT
    LATEST_PLOT = SaveData(tiempo, vFor, uFor, vBack, uBack, vMod, uMod, vRK2, uRK2, vRK4, uRK4)
    


def createSolucion(datos, a, b, c, d, V, U, tiempoSimulacion, tiempoInicio, tiempoFinal, valorEstimulacion):
    # Se crea una instancia de la clase Solution con los valores obtenidos
    solucion = Solution(a, b, c, d, V, U, tiempoSimulacion, tiempoInicio, tiempoFinal, valorEstimulacion)
    solucion.paramsToFloat()
    solucion.checkTimeValidity()
    canvas, subplot = datos.getMatplotlib()
    return solucion, canvas, subplot

def simular(datos):
    """
    Función que simula los datos de la ecuación diferencial.
    """
    # Se obtiene la información del combobox de opciones
    defaultParams = datos.getComboboxInfo()

    # Se obtienen los los métodos seleccionados por el usuario
    metodos = datos.getSelectedMethods()
    rungeKutta2 = metodos[0]
    rungeKutta4 = metodos[1]
    eulerAdelante = metodos[2]
    eulerAtras = metodos[3]
    eulerModificado = metodos[4]

    # Se obtienen las variables seleccionadas por el usuario
    variables = datos.getSelectedVariables()
    V = variables[0]
    U = variables[1]

    # Se obtienen los parámetros de la simulación
    simulacion = datos.getSimulacionData()
    tiempoSimulacion = simulacion[1]
    tiempoInicio = simulacion[2]
    tiempoFinal = simulacion[3]
    valorEstimulacion = simulacion[0]

    # Se obtienen los parámetros a, b, c y d seleccionados por el usuario
    params = datos.getSelectedParameters()
    a = params[0]
    b = params[1]
    c = params[2]
    d = params[3]

    if defaultParams == 'None' or defaultParams == "":
        
        # Se crea una instancia de la clase Solution con los valores obtenidos
        solucion, canvas, subplot = createSolucion(datos, a, b, c, d, V, U, tiempoSimulacion, tiempoInicio, tiempoFinal, valorEstimulacion)
        
        # Se grafica la solución
        graficar(solucion, subplot, canvas, V, U, eulerAdelante, eulerAtras, eulerModificado, rungeKutta2, rungeKutta4)
        
    elif defaultParams == 'Regular Spiking':
        # Se ejecuta una simulación con el ajuste predeterminado de Regular Spiking
        c = -65.0
        d = 8.0

        # Se crea una instancia de la clase Solution con los valores obtenidos
        solucion, canvas, subplot = createSolucion(datos, a, b, c, d, V, U, tiempoSimulacion, tiempoInicio, tiempoFinal, valorEstimulacion)
        # Se grafica la solución
        graficar(solucion, subplot, canvas, V, U, eulerAdelante, eulerAtras, eulerModificado, rungeKutta2, rungeKutta4)
    elif defaultParams == 'Intrinsic Bursting':
        # Se ejecuta una simulación con el ajuste predeterminado de Intrinsic Bursting
        c = -55.0
        d = 4.0

        # Se crea una instancia de la clase Solution con los valores obtenidos
        solucion, canvas, subplot = createSolucion(datos, a, b, c, d, V, U, tiempoSimulacion, tiempoInicio, tiempoFinal, valorEstimulacion)
        graficar(solucion, subplot, canvas, V, U, eulerAdelante, eulerAtras, eulerModificado, rungeKutta2, rungeKutta4)

    elif defaultParams == 'Chattering':
        # Se ejecuta una simulación con el ajuste predeterminado de Chattering
        c = -50.0
        d = 2.0

        # Se crea una instancia de la clase Solution con los valores obtenidos
        solucion, canvas, subplot = createSolucion(datos, a, b, c, d, V, U, tiempoSimulacion, tiempoInicio, tiempoFinal, valorEstimulacion)

        graficar(solucion, subplot, canvas, V, U, eulerAdelante, eulerAtras, eulerModificado, rungeKutta2, rungeKutta4)
    elif defaultParams == 'Fast Spiking':
        # Se ejecuta una simulación con el ajuste predeterminado de Fast Spiking
        a = 0.1

        # Se crea una instancia de la clase Solution con los valores obtenidos
        solucion, canvas, subplot = createSolucion(datos, a, b, c, d, V, U, tiempoSimulacion, tiempoInicio, tiempoFinal, valorEstimulacion)
        graficar(solucion, subplot, canvas, V, U, eulerAdelante, eulerAtras, eulerModificado, rungeKutta2, rungeKutta4)
    elif defaultParams == 'Talamo-Cortical':
        # Se ejecuta una simulación con el ajuste predeterminado de Talamo-Cortical
        valorEstimulacion = -60.0

        # Se crea una instancia de la clase Solution con los valores obtenidos
        solucion, canvas, subplot = createSolucion(datos, a, b, c, d, V, U, tiempoSimulacion, tiempoInicio, tiempoFinal, valorEstimulacion)
        graficar(solucion, subplot, canvas, V, U, eulerAdelante, eulerAtras, eulerModificado, rungeKutta2, rungeKutta4)
    elif defaultParams == 'Resonador':
        # Se ejecuta una simulación con el ajuste predeterminado de Resonador
        a = 0.1
        b = 0.26

        # Se crea una instancia de la clase Solution con los valores obtenidos
        solucion, canvas, subplot = createSolucion(datos, a, b, c, d, V, U, tiempoSimulacion, tiempoInicio, tiempoFinal, valorEstimulacion)
        graficar(solucion, subplot, canvas, V, U, eulerAdelante, eulerAtras, eulerModificado, rungeKutta2, rungeKutta4)

    else:
        raise InvalidParameters("El valor predeterminado elegido no es válido")
    
    # Se actualiza la tabla
    tabla = datos.getTabla()
    tablaSize = datos.getTablaSize()

    # Para evitar overflow de la tabla se revisa si llegó a su máximo tamaño
    if tablaSize <8:
        if tablaSize % 2 == 0:
            tabla.insert("", "end", values=(tiempoInicio, tiempoFinal, valorEstimulacion), tags=('evenrow',))

        else:
            tabla.insert("", "end", values=(tiempoInicio, tiempoFinal, valorEstimulacion), tags=('oddrow',)) 
        tablaSize += 1
        datos.setTablaSize(tablaSize)
        tabla.config(height=tablaSize)
        datos.setTablaRecordedDataAmount(tablaSize)
    else:
        tabla.delete(tabla.get_children()[0])
        cantidadDatos = datos.getTablaRecordedDataAmount()
        if cantidadDatos % 2 == 0:
            tabla.insert("", "end", values=(tiempoInicio, tiempoFinal, valorEstimulacion), tags=('evenrow',))
        else:
            tabla.insert("", "end", values=(tiempoInicio, tiempoFinal, valorEstimulacion), tags=('oddrow',)) 
        datos.setTablaRecordedDataAmount(cantidadDatos + 1)



def exportarDatos():
    if LATEST_PLOT:
        LATEST_PLOT.save("PlotFile_"+str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))+".bin")
    else:
        raise InvalidParameters("No se han generado datos para exportar")

def cargarDatos(fileName, datosInterfaz):
    if not fileName == "":
        # Se cargan los datos usando el método load de SaveData
        datos = SaveData.load(fileName)
        # Se transforman los datos a lista
        listaCargada = datos.asList()
        
        # Se obtienen el tiempo de la lista cargada
        tiempo = listaCargada[0]
        # Se obtienen los datos de la interfaz
        interfaz = datosInterfaz.getMatplotlib()
        canvas = interfaz[0]
        subplot = interfaz[1]

        # Se limpia el canvas
        subplot.clear()

        for elemento in range(1, len(listaCargada)):
            # Se grafica cada elemento que no sea nulo
            if listaCargada[elemento] is not None:
                subplot.plot(tiempo, listaCargada[elemento])
        canvas.draw()

