import numpy as np

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
            uForEuler[i] = uForEuler[i-1] + h*f2(vectorT[i-1], uForEuler[i-1], vForEuler[i-1])
        else:
            vForEuler[i] = solution.c
            uForEuler[i] = uForEuler[i-1] + solution.d


    return vectorT, vForEuler, uForEuler