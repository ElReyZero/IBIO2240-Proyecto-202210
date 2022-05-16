from dataclasses import dataclass
from .exceptions import InvalidParameters
from .functions import eulerAdelante

class ProgramGUIVariables:
    """
    Clase que contiene todas las variables de la interfaz gráfica que contienen información
    """
    def __init__(self):
        # Definimos diccionarios específicos donde almacenar cada variable
        self.matplotlib = {}
        self.matplotlib['canvas'] = None
        self.matplotlib['figure'] = None

        self.opciones = {}
        self.opciones['metodos'] = {}
        self.opciones['metodos']['Runge_Kutta_2'] = None
        self.opciones['metodos']['Runge_Kutta_4'] = None
        self.opciones['metodos']['Euler_Adelante'] = None
        self.opciones['metodos']['Euler_Atras'] = None
        self.opciones['metodos']['Euler_Modificado'] = None
        self.opciones['variables'] = {}
        self.opciones['variables']['V'] = None
        self.opciones['variables']['U'] = None
        self.opciones['parametros'] = {}
        self.opciones['parametros']['a'] = None
        self.opciones['parametros']['b'] = None
        self.opciones['parametros']['c'] = None
        self.opciones['parametros']['d'] = None
        self.opciones['dropdown'] = None

        self.simulacion = {}
        self.simulacion['ScrollbarEstimulacion'] = None
        self.simulacion['tiempoSimulacion'] = None
        self.simulacion['tiempoInicio'] = None
        self.simulacion['tiempoFinal'] = None
        self.simulacion['valorSimulacion'] = None

        self.tabla = {}
        self.tabla['tabla'] = None

    def setMatplotlib(self, canvas, figure):
        self.matplotlib['canvas'] = canvas
        self.matplotlib['figure'] = figure

    def setMetodos(self, metodo1, metodo2, metodo3, metodo4, metodo5):
        self.opciones['metodos']['Runge_Kutta_2'] = metodo1
        self.opciones['metodos']['Runge_Kutta_4'] = metodo2
        self.opciones['metodos']['Euler_Adelante'] = metodo3
        self.opciones['metodos']['Euler_Atras'] = metodo4
        self.opciones['metodos']['Euler_Modificado'] = metodo5
    
    def setVariables(self, V, U):
        self.opciones['variables']['V'] = V
        self.opciones['variables']['U'] = U

    def setParametros(self, a, b, c, d):
        self.opciones['parametros']['a'] = a
        self.opciones['parametros']['b'] = b
        self.opciones['parametros']['c'] = c
        self.opciones['parametros']['d'] = d

    def setDropdownOpciones(self, dropdown):
        self.opciones['dropdown'] = dropdown

    def setEstimulacion(self, scrollbarEstimulacion, tiempoSimulacion, tiempoInicio, tiempoFinal, valorSimulacion):
        self.simulacion['ScrollbarEstimulacion'] = scrollbarEstimulacion
        self.simulacion['tiempoSimulacion'] = tiempoSimulacion
        self.simulacion['tiempoInicio'] = tiempoInicio
        self.simulacion['tiempoFinal'] = tiempoFinal
        self.simulacion['valorSimulacion'] = valorSimulacion

    def setTabla(self, tabla):
        self.tabla['tabla'] = tabla

    def getMatplotlib(self):
        return self.matplotlib
    
    def getOpciones(self):
        return self.opciones

    def getSimulacion(self):
        return self.simulacion

    def getTabla(self):
        return self.tabla
    
    def getSelectedMethods(self):
        rungeKutta2 = self.opciones['metodos']['Runge_Kutta_2'].get()
        rungeKutta4 = self.opciones['metodos']['Runge_Kutta_4'].get()
        eulerAdelante = self.opciones['metodos']['Euler_Adelante'].get()
        eulerAtras = self.opciones['metodos']['Euler_Atras'].get()
        eulerModificado = self.opciones['metodos']['Euler_Modificado'].get()
        return [rungeKutta2, rungeKutta4, eulerAdelante, eulerAtras, eulerModificado]

    def getSelectedVariables(self):
        V = self.opciones['variables']['V'].get()
        U = self.opciones['variables']['U'].get()
        return [V, U]

    def getSelectedParameters(self):
        try:
            a = float(self.opciones['parametros']['a'].get())
            b = float(self.opciones['parametros']['b'].get())
            c = float(self.opciones['parametros']['c'].get())
            d = float(self.opciones['parametros']['d'].get())
            return [a, b, c, d]
        except ValueError:
            raise InvalidParameters("Los parámetros a, b, c y d deben ser números")

    def getComboboxInfo(self):
        return self.opciones['dropdown'].get()
        

@dataclass
class Solution:
    """
    Clase que representa una solución de un problema.
    """
    #Lista de parámetros
    a: float
    b: float
    c: float
    d: float

    # Variables usadas
    v: bool
    u: bool

    # Métodos de Solución
    rungeKutta2: bool = False
    rungeKutta4: bool = False
    eulerAdelante: bool = False
    eulerAtras: bool = False
    eulerModificado: bool = False

    def I(t):
        if t > 200 and t < 600:
            I = 10
        else:
            I = 0
        return I

    def equation1(self, t, v, u):
        return (0.04*v**2) + 4*v + 140 - u + self.I(t)

    def equation2(self, t, v, u):
        return self.a  * (self.b*v -u)

    def solveEulerForward():
        eulerAdelante()

    # Euler hacia atrás: Despejar función
