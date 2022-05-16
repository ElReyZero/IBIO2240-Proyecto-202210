from .classes import Solution
from .exceptions import InvalidParameters
import numpy as np 

def simular(datos):
    """
    Función que simula los datos de la ecuación diferencial.
    """
    # Se obtiene la información del combobox de opciones
    defaultParams = datos.getComboboxInfo()

    if defaultParams == 'None' or defaultParams == "":
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

        # Se obtienen los parámetros a, b, c y d seleccionados por el usuario
        params = datos.getSelectedParameters()
        a = params[0]
        b = params[1]
        c = params[2]
        d = params[3]

        # Se crea una instancia de la clase Solution con los valores obtenidos
        solucion = Solution(a, b, c, d, V, U, rungeKutta2, rungeKutta4, eulerAdelante, eulerAtras, eulerModificado)
        print(solucion)


    elif defaultParams == 'Regular Spiking':
        # Se ejecuta una simulación con el ajuste predeterminado de Regular Spiking
        pass
    elif defaultParams == 'Intrinsic Bursting':
        # Se ejecuta una simulación con el ajuste predeterminado de Intrinsic Bursting
        pass
    elif defaultParams == 'Chattering':
        # Se ejecuta una simulación con el ajuste predeterminado de Chattering
        pass
    elif defaultParams == 'Fast Spiking':
        # Se ejecuta una simulación con el ajuste predeterminado de Fast Spiking
        pass
    elif defaultParams == 'Talamo-Cortical':
        # Se ejecuta una simulación con el ajuste predeterminado de Talamo-Cortical
        pass
    elif defaultParams == 'Resonador':
        # Se ejecuta una simulación con el ajuste predeterminado de Resonador
        pass
    else:
        raise InvalidParameters("El valor predeterminado elegido no es válido")


def eulerAdelante(y0:float, t0:float, tf:float, h:float, f1, f2, solution)->tuple:
    """Función que calcula la solución de una ecuación diferencial mediante el método de Euler Adelante.

    Args:
        y0 (float): Valor inicial de la función.
        t0 (float): Valor inicial del tiempo.
        tf (float): Valor final del tiempo.
        h (float): Incremento de tiempo.
        f (_type_): Función que representa la ecuación diferencial.

    Returns:
        tuple: Tupla con los valores de la función en cada instante de tiempo.
    """
    
    vectorT = np.arange(t0, tf+h, h)
    vForEuler = np.zeros(len(vectorT))
    vForEuler[0] = y0
    uForEuler = np.zeros(len(vectorT))
    uForEuler[0] = y0

    for i in range(1, len(vectorT)):
        
        if vForEuler[i-1] < 30:
            vForEuler[i] = vForEuler[i-1] + h*f1(vectorT[i-1], vForEuler[i-1], uForEuler[i-1])
            uForEuler[i] = uForEuler[i-1] + h*f2(vectorT[i-1], uForEuler[i-1], vForEuler[i-1])
        else:
            vForEuler[i] = solution.c
            uForEuler[i] = uForEuler[i-1] + solution.d


    return vectorT, vForEuler, uForEuler