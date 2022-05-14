from .classes import Solution
from .exceptions import InvalidParameters

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