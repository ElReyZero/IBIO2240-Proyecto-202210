from .solveMethods import eulerAdelante, rungeKutta2, rungeKutta4, eulerBackwards, eulerModificado ,solveIVP
from dataclasses import dataclass
from .exceptions import InvalidParameters
import pickle
import numpy as np

class ProgramGUIVariables:
    """
    Clase que contiene todas las variables de la interfaz gráfica que contienen información
    """
    def __init__(self):
        # Definimos diccionarios específicos donde almacenar cada variable
        self.ventana = None

        self.matplotlib = {}
        self.matplotlib['canvas'] = None
        self.matplotlib['subplot'] = None

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

        self.tabla = {}
        self.tabla['tabla'] = None
        self.tabla['size'] = 0
        self.tabla['recordedDataAmount'] = 0

        self.barraProgreso = None
        self.cargandoLabel = None

    # Setters
    def setVentana(self, ventana):
        self.ventana = ventana

    def setMatplotlib(self, canvas, subplot):
        self.matplotlib['canvas'] = canvas
        self.matplotlib['subplot'] = subplot

    def setMetodos(self, metodo1, metodo2, metodo3, metodo4, metodo5, metodo6):
        self.opciones['metodos']['Runge_Kutta_2'] = metodo1
        self.opciones['metodos']['Runge_Kutta_4'] = metodo2
        self.opciones['metodos']['Euler_Adelante'] = metodo3
        self.opciones['metodos']['Euler_Atras'] = metodo4
        self.opciones['metodos']['Euler_Modificado'] = metodo5
        self.opciones['metodos']['SolveIVP'] = metodo6
    
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

    def setEstimulacion(self, scrollbarEstimulacion, tiempoSimulacion, tiempoInicio, tiempoFinal):
        self.simulacion['ScrollbarEstimulacion'] = scrollbarEstimulacion
        self.simulacion['tiempoSimulacion'] = tiempoSimulacion
        self.simulacion['tiempoInicio'] = tiempoInicio
        self.simulacion['tiempoFinal'] = tiempoFinal

    def setTabla(self, tabla):
        self.tabla['tabla'] = tabla

    def setTablaSize(self, size):
        self.tabla['size'] = size

    def setTablaRecordedDataAmount(self, amount):
        self.tabla['recordedDataAmount'] = amount

    def setBarraProgreso(self, barraProgreso):
        self.barraProgreso = barraProgreso

    def setCargandoLabel(self, cargandoLabel):
        self.cargandoLabel = cargandoLabel

    ## Getters
    def getVentana(self):
        return self.ventana

    def getMatplotlib(self):
        return [self.matplotlib["canvas"], self.matplotlib["subplot"]]
    
    def getOpciones(self):
        return self.opciones

    def getSimulacionData(self):
        try:
            scrollBarEstimulacion = float(self.simulacion['ScrollbarEstimulacion'].get())
            tiempoSimulacion = float(self.simulacion['tiempoSimulacion'].get())
            tiempoInicio = float(self.simulacion['tiempoInicio'].get())
            tiempoFinal = float(self.simulacion['tiempoFinal'].get())
            return [scrollBarEstimulacion, tiempoSimulacion, tiempoInicio, tiempoFinal]
        except ValueError:
            raise InvalidParameters("Los parámetros de simulación no son válidos")

    def getTabla(self):
        return self.tabla["tabla"]

    def getTablaSize(self):
        return self.tabla['size']

    def getTablaRecordedDataAmount(self):
        return self.tabla['recordedDataAmount']
    
    def getSelectedMethods(self):
        rungeKutta2 = self.opciones['metodos']['Runge_Kutta_2'].get()
        rungeKutta4 = self.opciones['metodos']['Runge_Kutta_4'].get()
        eulerAdelante = self.opciones['metodos']['Euler_Adelante'].get()
        eulerAtras = self.opciones['metodos']['Euler_Atras'].get()
        eulerModificado = self.opciones['metodos']['Euler_Modificado'].get()
        solveIVP = self.opciones['metodos']['SolveIVP'].get()
        return [rungeKutta2, rungeKutta4, eulerAdelante, eulerAtras, eulerModificado, solveIVP]

    def getSelectedVariables(self):
        V = self.opciones['variables']['V'].get()
        U = self.opciones['variables']['U'].get()
        return [V, U]

    def getSelectedParameters(self):
        a = self.opciones['parametros']['a'].get()
        b = self.opciones['parametros']['b'].get()
        c = self.opciones['parametros']['c'].get()
        d = self.opciones['parametros']['d'].get()
        return [a, b, c, d]

    def getComboboxInfo(self):
        return self.opciones['dropdown'].get()
        
    def getBarraProgreso(self):
        return self.barraProgreso
    
    def getCargandoLabel(self):
        return self.cargandoLabel

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

    # Parámetros de la simulación
    tiempoSimulacion: float
    tiempoInicio: float
    tiempoFinal: float
    valorEstimulacion: float
    
    def paramsToFloat(self):
        """Función auxiliar que revisa que una variable sea del tipo correcto"""
        try:
            self.a = float(self.a)
            self.b = float(self.b)
            self.c = float(self.c)
            self.d = float(self.d)
        except ValueError:
            raise InvalidParameters("Los parámetros a, b, c y d deben ser números")

    def checkTimeValidity(self):
        """Función auxiliar que revisa que el tiempo de simulación sea válido"""
        if self.tiempoSimulacion <= 0:
            raise InvalidParameters("El tiempo de simulación debe ser mayor a 0")
        elif self.tiempoInicio < 0 or self.tiempoFinal < 0:
            raise InvalidParameters("El tiempo de inicio y final debe ser mayor o igual a 0")
        elif self.tiempoInicio >= self.tiempoFinal:
            raise InvalidParameters("El tiempo de inicio debe ser menor al tiempo final")
        elif self.tiempoInicio >= self.tiempoSimulacion:
            raise InvalidParameters("El tiempo de inicio debe ser menor al tiempo de simulación")

    def I(self, t):
        if t > self.tiempoInicio and t < self.tiempoFinal:
            I = self.valorEstimulacion
        else:
            I = 0.0
        return I

    def functionV(self, t, v, u):
        return (0.04*v**2) + 5*v + 140 - u + self.I(t)

    def functionU(self, u, v):
        return self.a*(self.b*v - u)

    def FSystem(self, t, y):
        return [self.functionV(t, y[0], y[1]), self.functionU(y[1], y[0])]

    def FEulerBackRoot(self, yt2, t1, t2, y1t1, y2t1,h):
        def F1Multi(t, v, u):
            return (0.04*v**2) + 5*v + 140 - u + self.I(t)
        # Definimos la función F2
        def F2Multi(u, v):
            return self.a*(self.b*v - u)
        
        return [y1t1 + h * (F1Multi(t2, yt2[0], yt2[1])) - yt2[0], 
                y2t1 + h * (F2Multi(yt2[1], yt2[0])) - yt2[1]]

    def FEulerModRoot(self, yt2, t1, t2, y1t1, y2t1, h):
        def F1Multi(t, v, u):
            return (0.04*v**2) + 5*v + 140 - u + self.I(t)
        # Definimos la función F2
        def F2Multi(u, v):
            return self.a*(self.b*v - u)

        return [y1t1 + (h / 2.0) * (F1Multi(t1, y1t1, y2t1) + F1Multi(t2, yt2[0], yt2[1])) - yt2[0], 
                y2t1 + (h / 2.0) * (F2Multi(y2t1, y1t1) + F2Multi(yt2[1], yt2[0])) - yt2[1]]

    def solveEulerForward(self, v0=-65.0, u0=-14.0):
        return eulerAdelante(v0, u0, 0.0, self.tiempoSimulacion, 0.01, self.functionV, self.functionU, self) 


    def solveEulerBackward(self, v0=-65.0, u0=-14.0):
        return eulerBackwards(v0, u0, 0.0, self.tiempoSimulacion, 0.01, self.FEulerBackRoot, self)

    def solveEulerModified(self, v0=-65.0, u0=-14.0):
        return eulerModificado(v0, u0, 0.0, self.tiempoSimulacion, 0.01, self.FEulerModRoot, self)

    def solveRungeKutta2(self, v0=-65.0, u0=-14.0):
        return rungeKutta2(v0, u0, 0.0, self.tiempoSimulacion, 0.01, self.functionV, self.functionU, self)

    def solveRungeKutta4(self, v0=-65.0, u0=-14.0):
        return rungeKutta4(v0, u0, 0.0, self.tiempoSimulacion, 0.01, self.functionV, self.functionU, self)

    def solveIVP(self, v0=-65.0, u0=-14.0):
        return solveIVP(v0, u0, 0.0, self.tiempoSimulacion, 0.01, self.FSystem)

@dataclass
class SaveData:
    """
    Clase para guardar los datos de una gráfica en un archivo bin.
    """
    tiempo : np.array
    tiempoIVP : np.array
    vFor : np.array
    uFor : np.array
    vBack : np.array
    uBack : np.array
    vMod : np.array
    uMod : np.array
    vRK2 : np.array
    uRK2 : np.array
    vRK4 : np.array
    uRK4 : np.array
    vIVP : np.array
    uIVP : np.array

    def save(self, fileName):
        pickle.dump(self, open(fileName, 'wb'), pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def load(fileName):
        data =  pickle.load(open(fileName, 'rb'))
        return data

    def asList(self):
        return [self.tiempo, self.tiempoIVP, self.vFor, self.uFor, self.vBack, self.uBack, self.vMod, self.uMod, self.vRK2, self.uRK2, self.vRK4, self.uRK4, self.vIVP, self.uIVP]
    
    def asDict(self):
        return {'tiempo': self.tiempo, 'vFor': self.vFor, 'uFor': self.uFor, 'vBack': self.vBack, 'uBack': self.uBack, 'vMod': self.vMod, 'uMod': self.uMod, 'vRK2': self.vRK2, 'uRK2': self.uRK2, 'vRK4': self.vRK4, 'uRK4': self.uRK4, 'vIVP': self.vIVP, 'uIVP': self.uIVP}
