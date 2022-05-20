import numpy as np
import scipy.integrate as inte

def eulerAdelante(v0:float, u0:float, t0:float, tf:float, h:float, f1, f2, solution)->tuple:
    """Función que calcula la solución de una ecuación diferencial mediante el método de Euler Adelante.

    Args:
        v0 (float): Valor inicial de la función V(t).
        u0 (float): Valor inicial de la función U(t).
        t0 (float): Valor inicial del tiempo.
        tf (float): Valor final del tiempo.
        h (float): Incremento de tiempo.
        f1 (function): Función que representa la ecuación diferencial de V(t).
        f2 (function): Función que representa la ecuación diferencial de U(t).

    Returns:
        tuple: Tupla con los valores de la función en cada instante de tiempo.
    """
    
    vectorT = np.arange(t0, tf+h, h)
    vForEuler = np.zeros(len(vectorT))
    vForEuler[0] = v0
    uForEuler = np.zeros(len(vectorT))
    uForEuler[0] = u0

    for i in range(1, len(vectorT)):
        if vForEuler[i-1] <= 30:
            vForEuler[i] = vForEuler[i-1] + h*f1(vectorT[i-1], vForEuler[i-1], uForEuler[i-1])
            uForEuler[i] = uForEuler[i-1] + h*f2(uForEuler[i-1], vForEuler[i-1])
        else:
            vForEuler[i] = solution.c
            uForEuler[i] = uForEuler[i-1] + solution.d


    return vectorT, vForEuler, uForEuler

def rungeKutta2(v0:float, u0:float, t0:float, tf:float, h:float, f1, f2, solution)->tuple:
    """Función que calcula la solución de una ecuación diferencial mediante el método de Runge-Kutta2.

    Args:
        y0 (float): Valor inicial de la función.
        t0 (float): Valor inicial del tiempo.
        tf (float): Valor final del tiempo.
        h (float): Incremento de tiempo.
        f1 (_type_): Función que representa la ecuación diferencial.

    Returns:
        tuple: Tupla con los valores de la función en cada instante de tiempo.
    """   

    vectorT = np.arange(t0, tf+h, h)
    vrk2 = np.zeros(len(vectorT))
    vrk2[0] = v0

    urk2 = np.zeros(len(vectorT))
    urk2[0] = u0

    for i in range(1, len(vectorT)):

        if vrk2[i-1] <= 30:
            k1 = f1(vectorT[i-1], vrk2[i-1], urk2[i-1])
            k3 = f2(urk2[i-1], vrk2[i-1])
            k2 = f1(vectorT[i-1] + h, vrk2[i-1] + h * k3, urk2[i-1] + h * k1)
            k4 = f2(urk2[i-1] + h * k1, vrk2[i-1] + h * k3)

            vrk2[i] = vrk2[i-1] + (h/2) * (k1 + k2)
            urk2[i] = urk2[i-1] + (h/2) * (k3 + k4)
        else:
            vrk2[i] = solution.c
            urk2[i] = urk2[i-1] + solution.d

    return vectorT, vrk2, urk2


def rungeKutta4(v0:float, u0:float, t0:float, tf:float, h:float, f1, f2, solution)->tuple:
    """Función que calcula la solución de una ecuación diferencial mediante el método de Runge-Kutta2.

    Args:
        y0 (float): Valor inicial de la función.
        t0 (float): Valor inicial del tiempo.
        tf (float): Valor final del tiempo.
        h (float): Incremento de tiempo.
        f1 (_type_): Función que representa la ecuación diferencial.

    Returns:
        tuple: Tupla con los valores de la función en cada instante de tiempo.
    """   

    vectorT = np.arange(t0, tf+h, h)
    vrk4 = np.zeros(len(vectorT))
    vrk4[0] = v0

    urk4 = np.zeros(len(vectorT))
    urk4[0] = u0

    for i in range(1, len(vectorT)):

        if vrk4[i-1] <= 30:
            # Arreglar
            k1 = f1(vectorT[i-1], vrk4[i-1], urk4[i-1])
            k5 = f2(urk4[i-1], vrk4[i-1])

            k2 = f1(vectorT[i-1] + 0.5*h, vrk4[i-1] + 0.5*h*k5, urk4[i-1] + 0.5*h*k1)
            k3 = f1(vectorT[i-1] + 0.5*h, vrk4[i-1] + 0.5*h*k5, urk4[i-1] + 0.5*h*k1)
            k4 = f1(vectorT[i-1] + h, vrk4[i-1] + h*k5, urk4[i-1] + h*k1)
            vrk4[i] = vrk4[i-1] + (h/6) * (k1+2*k2+2*k3+k4)

            k6 = f2(urk4[i-1] + 0.5*h*k5, vrk4[i-1] + 0.5*h*k5)
            k7 = f2(urk4[i-1] + 0.5*h*k6, vrk4[i-1] + 0.5*h*k6)
            k8 = f2(urk4[i-1] + h*k7, vrk4[i-1] + h*k7)
            urk4[i] = urk4[i-1] + (h/6) * (k5+2*k6+2*k7+k8)
        else:
            vrk4[i] = solution.c
            urk4[i] = urk4[i-1] + solution.d

    return vectorT, vrk4, urk4

def solveIVP(v0, u0, t0, tf, h, FSystem):
    vectorT = np.arange(t0, tf+h, h)
    solivp = inte.solve_ivp(FSystem, [t0, tf], [v0, u0], t_eval=vectorT, method='RK45')
    return solivp