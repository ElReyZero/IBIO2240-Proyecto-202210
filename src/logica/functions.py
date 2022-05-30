from .classes import Solution, SaveData
from .exceptions import InvalidParameters
from  datetime import datetime
import time
from tkinter.messagebox import showinfo
# Variable global que almacena la última gráfica por si se quiere guardar
LATEST_PLOT= None

def graficar(carga, solucion, subplot, canvas, V, U, eulerAdelante, eulerAtras, eulerModificado, rungeKutta2, rungeKutta4, solveIVP, v0=-65.0, u0=-14.0):
    """ Función auxiliar que grafica la entrada de la interfaz
    """

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
    vIVP = None
    uIVP = None
    tiempoIVP = None
    contador = 0

    ventana = carga[0]
    barra = carga[1]
    cargandoLabel = carga[2]
    cargandoLabel.config(text="Cargando...")

    # Se ejecutan los métodos seleccionados y se grafican directamente en el canvas de la interfaz
    if eulerAdelante:
        tiempo, vFor, uFor = solucion.solveEulerForward(v0=v0, u0=u0)
        if V:
            subplot.plot(tiempo, vFor, label='Euler Adelante - V(t)')
        if U:
            subplot.plot(tiempo, uFor, label='Euler Adelante - U(t)')
        if not V and not U:
            raise InvalidParameters("Es necesario seleccionar una función para resolver")
        barra.step()
        ventana.update()
        contador += 1
    if eulerAtras:
        tiempo, vBack, uBack = solucion.solveEulerBackward()
        if V:
            subplot.plot(tiempo, vBack, label='Euler Atras - V(t)')
        if U:
            subplot.plot(tiempo, uBack, label='Euler Atras - U(t)')
        if not V and not U:
            raise InvalidParameters("Es necesario seleccionar una función para resolver")
        barra.step()
        ventana.update()
        contador += 1
    if eulerModificado:
        tiempo, vMod, uMod = solucion.solveEulerModified()
        if V:
            subplot.plot(tiempo, vMod, label='Euler Modificado - V(t)')
        if U:
            subplot.plot(tiempo, uMod, label='Euler Modificado - U(t)')
        if not V and not U:
            raise InvalidParameters("Es necesario seleccionar una función para resolver")
        barra.step()
        ventana.update()
        contador += 1
    if rungeKutta2:
        tiempo, vRK2, uRK2 = solucion.solveRungeKutta2(v0=v0, u0=u0)
        if V:
            subplot.plot(tiempo, vRK2, label='Runge Kutta 2 - V(t)')
        if U:
            subplot.plot(tiempo, uRK2, label='Runge Kutta 2 - U(t)')
        if not V and not U:
            raise InvalidParameters("Es necesario seleccionar una función para resolver")
        barra.step()
        ventana.update()
        contador += 1
    if rungeKutta4:
        tiempo, vRK4, uRK4 = solucion.solveRungeKutta4(v0=v0, u0=u0)
        if V:
            subplot.plot(tiempo, vRK4, label='Runge Kutta 4 - V(t)')
        if U:
            subplot.plot(tiempo, uRK4, label='Runge Kutta 4 - U(t)')
        if not V and not U:
            raise InvalidParameters("Es necesario seleccionar una función para resolver")
        barra.step()
        ventana.update()
        contador += 1
    if solveIVP:
        respuestaSolve = solucion.solveIVP()
        tiempoIVP = respuestaSolve.t
        vIVP = respuestaSolve.y[0]
        uIVP = respuestaSolve.y[1]
        if V:
            subplot.plot(tiempoIVP, vIVP, label='Solve IVP - V(t)')
        if U:
            subplot.plot(tiempoIVP, uIVP, label='Solve IVP - U(t)')
        if not V and not U:
            raise InvalidParameters("Es necesario seleccionar una función para resolver")
        barra.step()
        ventana.update()
        contador += 1
        showinfo("Solve IVP", "El método de Solve IVP no fue implementado con las restricciones del problema en mente, por lo que el resultado se verá alejado de la solución real")
    if not eulerAdelante and not eulerAtras and not eulerModificado and not rungeKutta2 and not rungeKutta4 and not solveIVP:
        raise InvalidParameters("No se seleccionó ningún método")

    # Se revisa si se llenó o no la barra de carga, de lo contrario, se llena
    if not contador == 6:
        for _ in range(contador, 5):
            barra.step()
            ventana.update()
            time.sleep(0.01)
        if barra['value'] != 0:
            barra['value'] = 0
            ventana.update()
    
    # Se termina graficando todo
    subplot.legend()
    canvas.draw()
    cargandoLabel.config(text="")

    # Se guarda la gráfica en una variable por si el usuario la quiere persistir
    global LATEST_PLOT
    LATEST_PLOT = SaveData(tiempo, tiempoIVP, vFor, uFor, vBack, uBack, vMod, uMod, vRK2, uRK2, vRK4, uRK4, vIVP, uIVP)
    del tiempo, vFor, uFor, vBack, uBack, vMod, uMod, vRK2, uRK2, vRK4, uRK4, vIVP, uIVP

def createSolucion(datos, a, b, c, d, V, U, tiempoSimulacion, tiempoInicio, tiempoFinal, valorEstimulacion):
    """ Función auxiliar que crea una solución, la revisa y devuelve su clase y el canvas de la interfaz
    """

    # Se crea una instancia de la clase Solution con los valores obtenidos
    solucion = Solution(a, b, c, d, V, U, tiempoSimulacion, tiempoInicio, tiempoFinal, valorEstimulacion)
    # Se pasan y revisan los parámetros a, b, c y d a números flotantes
    solucion.paramsToFloat()

    # Se revisa que los parámetros de tiempo sean válidos
    solucion.checkTimeValidity()
    
    # Se obtienen el canvas y subplot de la interfaz
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
    solveIVP = metodos[5]

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

    # Se obtienen los datos de la ventana, barra de progreso y label de cargando
    carga = list()
    carga.append(datos.getVentana())
    carga.append(datos.getBarraProgreso())
    carga.append(datos.getCargandoLabel())

    # Se revisa el si el usuario eligió alguna configuración predeterminada o no
    if defaultParams == 'None' or defaultParams == "":
        # Se crea una instancia de la clase Solution con los valores obtenidos
        solucion, canvas, subplot = createSolucion(datos, a, b, c, d, V, U, tiempoSimulacion, tiempoInicio, tiempoFinal, valorEstimulacion)
        
        # Se grafica la solución
        graficar(carga, solucion, subplot, canvas, V, U, eulerAdelante, eulerAtras, eulerModificado, rungeKutta2, rungeKutta4, solveIVP)
        
    elif defaultParams == 'Regular Spiking':
        # Se ejecuta una simulación con el ajuste predeterminado de Regular Spiking
        c = -65.0
        d = 8.0

        # Se crea una instancia de la clase Solution con los valores obtenidos
        solucion, canvas, subplot = createSolucion(datos, a, b, c, d, V, U, tiempoSimulacion, tiempoInicio, tiempoFinal, valorEstimulacion)
        # Se grafica la solución
        graficar(carga, solucion, subplot, canvas, V, U, eulerAdelante, eulerAtras, eulerModificado, rungeKutta2, rungeKutta4, solveIVP)
    elif defaultParams == 'Intrinsic Bursting':
        # Se ejecuta una simulación con el ajuste predeterminado de Intrinsic Bursting
        c = -55.0
        d = 4.0

        # Se crea una instancia de la clase Solution con los valores obtenidos
        solucion, canvas, subplot = createSolucion(datos, a, b, c, d, V, U, tiempoSimulacion, tiempoInicio, tiempoFinal, valorEstimulacion)
        graficar(carga, solucion, subplot, canvas, V, U, eulerAdelante, eulerAtras, eulerModificado, rungeKutta2, rungeKutta4, solveIVP)

    elif defaultParams == 'Chattering':
        # Se ejecuta una simulación con el ajuste predeterminado de Chattering
        c = -50.0
        d = 2.0

        # Se crea una instancia de la clase Solution con los valores obtenidos
        solucion, canvas, subplot = createSolucion(datos, a, b, c, d, V, U, tiempoSimulacion, tiempoInicio, tiempoFinal, valorEstimulacion)

        graficar(carga, solucion, subplot, canvas, V, U, eulerAdelante, eulerAtras, eulerModificado, rungeKutta2, rungeKutta4, solveIVP)
    elif defaultParams == 'Fast Spiking':
        # Se ejecuta una simulación con el ajuste predeterminado de Fast Spiking
        a = 0.1

        # Se crea una instancia de la clase Solution con los valores obtenidos
        solucion, canvas, subplot = createSolucion(datos, a, b, c, d, V, U, tiempoSimulacion, tiempoInicio, tiempoFinal, valorEstimulacion)
        graficar(carga, solucion, subplot, canvas, V, U, eulerAdelante, eulerAtras, eulerModificado, rungeKutta2, rungeKutta4, solveIVP)
    elif defaultParams == 'Talamo-Cortical':
        # Se ejecuta una simulación con el ajuste predeterminado de Talamo-Cortical
        # Se crea una instancia de la clase Solution con los valores obtenidos

        # Si la corriente suministrada es positiva, v está cerca de -60mV, de lo contrario, se acerca a -90mV
        if valorEstimulacion > 0:
            v = -60.0
        else:
            v = -90.0

        solucion, canvas, subplot = createSolucion(datos, a, b, c, d, V, U, tiempoSimulacion, tiempoInicio, tiempoFinal, valorEstimulacion)
        graficar(carga, solucion, subplot, canvas, V, U, eulerAdelante, eulerAtras, eulerModificado, rungeKutta2, rungeKutta4, solveIVP, v0=v)
    elif defaultParams == 'Resonador':
        # Se ejecuta una simulación con el ajuste predeterminado de Resonador
        a = 0.1
        b = 0.26

        # Se crea una instancia de la clase Solution con los valores obtenidos
        solucion, canvas, subplot = createSolucion(datos, a, b, c, d, V, U, tiempoSimulacion, tiempoInicio, tiempoFinal, valorEstimulacion)
        graficar(carga, solucion, subplot, canvas, V, U, eulerAdelante, eulerAtras, eulerModificado, rungeKutta2, rungeKutta4, solveIVP)
    else:
        raise InvalidParameters("El valor predeterminado elegido no es válido")
    
    # Se actualiza la tabla
    tabla = datos.getTabla()
    tablaSize = datos.getTablaSize()

    # Para evitar overflow de la tabla se revisa si llegó a su máximo tamaño
    # Se revisa también la resolución de la ventana para mirar el tamaño máximo de la tabla
    height = datos.getVentana().winfo_screenheight()
    maxTablaSize = 8
    if height < 800:
        maxTablaSize = 4

    if tablaSize < maxTablaSize:
        tablaSize += 1
        datos.setTablaSize(tablaSize)
        if tablaSize % 2 == 0:
            tabla.insert("", "end", text=tablaSize, values=(tiempoInicio, tiempoFinal, valorEstimulacion), tags=('evenrow',))

        else:
            tabla.insert("", "end", text=tablaSize, values=(tiempoInicio, tiempoFinal, valorEstimulacion), tags=('oddrow',)) 
        tabla.config(height=tablaSize)
        datos.setTablaRecordedDataAmount(tablaSize)
    else:
        tabla.delete(tabla.get_children()[0])
        cantidadDatos = datos.getTablaRecordedDataAmount()
        if cantidadDatos % 2 == 0:
            tabla.insert("", "end", text=cantidadDatos+1, values=(tiempoInicio, tiempoFinal, valorEstimulacion), tags=('oddrow',))
        else:
            tabla.insert("", "end", text=cantidadDatos+1, values=(tiempoInicio, tiempoFinal, valorEstimulacion), tags=('evenrow',)) 
        datos.setTablaRecordedDataAmount(cantidadDatos + 1)



def exportarDatos():
    """Función para exportar los datos de la simulación a un archivo binario

    Raises:
        InvalidParameters: En caso de que no hayan datos para exportar, se levanta esta excepción
    """

    # Si hay datos, se obtiene la variable que los almacena y se exportan a binario
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
        tiempoIVP = listaCargada[1]
        # Se limpia el canvas
        subplot.clear()
        for elemento in range(2, len(listaCargada)):
            # Se grafica cada elemento que no sea nulo
            if listaCargada[elemento] is not None and listaCargada[elemento].size == tiempo.size:
                subplot.plot(tiempo, listaCargada[elemento])
            # Se revisa que sea un método de solve ivp
            elif listaCargada[elemento] is not None:
                subplot.plot(tiempoIVP, listaCargada[elemento])
        canvas.draw()

