from tkinter import *
from tkinter import ttk


def frameOpciones(ventana):
    # Crear el frame de las opciones
    frameOpciones = Frame(ventana, width=600, height=300)
    frameOpciones.place(x=50, y=370)

    #Crear labels de los métodos de solución
    labelGeneral = Label(frameOpciones, text="Métodos de Solución:", font=("Lato", 12))
    labelGeneral.place(x=0, y=0)
    
    metodo1Var = IntVar()
    metodo1 = Checkbutton(frameOpciones, text="Range Kutta 2", variable=metodo1Var, font=("Lato bold", 12))
    metodo1.place(x=0, y=30)

    metodo2Var = IntVar()
    metodo2 = Checkbutton(frameOpciones, text="Range Kutta 4", variable=metodo2Var, font=("Lato bold", 12))
    metodo2.place(x=0, y=60)

    metodo3Var = IntVar()
    metodo3 = Checkbutton(frameOpciones, text="Euler Adelante", variable=metodo3Var, font=("Lato bold", 12))
    metodo3.place(x=0, y=90)

    metodo4Var = IntVar()
    metodo4 = Checkbutton(frameOpciones, text="Euler Atrás", variable=metodo4Var, font=("Lato bold", 12))
    metodo4.place(x=0, y=120)

    metodo5Var = IntVar()
    metodo5 = Checkbutton(frameOpciones, text="Euler Modificado", variable=metodo5Var, font=("Lato bold", 12))
    metodo5.place(x=0, y=150)

    # Crear labels de las variables
    labelGeneral = Label(frameOpciones, text="Variables:", font=("Lato", 12))
    labelGeneral.place(x=230, y=0)

    var1variable = IntVar()
    var1 = Checkbutton(frameOpciones, text="V(t)", variable=var1variable, font=("Lato bold", 12))
    var1.place(x=230, y=30)

    var2variable = IntVar()
    var2 = Checkbutton(frameOpciones, text="u(t)", variable=var2variable, font=("Lato bold", 12))
    var2.place(x=230, y=60)

    # Crear labels de parámetros
    labelGeneral = Label(frameOpciones, text="Parámetros:", font=("Lato", 12))
    labelGeneral.place(x=230, y=100)

    paramA = Label(frameOpciones, text="a", font=("Lato", 12))
    paramA.place(x=230, y=125)

    paramABox = StringVar(None)
    paramABox = Entry(frameOpciones, textvariable=paramABox, width=20)
    paramABox.place(x=250, y=130)

    paramB = Label(frameOpciones, text="b", font=("Lato", 12))
    paramB.place(x=230, y=155)

    paramBBox = StringVar(None)
    paramBBox = Entry(frameOpciones, textvariable=paramBBox, width=20)
    paramBBox.place(x=250, y=160)

    paramC = Label(frameOpciones, text="c", font=("Lato", 12))
    paramC.place(x=230, y=185)

    paramCBox = StringVar(None)
    paramCBox = Entry(frameOpciones, textvariable=paramCBox, width=20)
    paramCBox.place(x=250, y=190)

    paramD = Label(frameOpciones, text="d", font=("Lato", 12))
    paramD.place(x=230, y=215)

    paramDBox = StringVar(None)
    paramDBox = Entry(frameOpciones, textvariable=paramDBox, width=20)
    paramDBox.place(x=250, y=220)

    # Crear el dropdown con los valores predeterminados

    valoresLabel = Label(frameOpciones, text="Valores predeterminados:", font=("Lato", 12))
    valoresLabel.place(x=380, y=0)

    valoresPredeterminados = [None, "Regular Spiking", "Intrinsic Bursting", "Chattering", "Fast Spiking", "Talamo-Cortical", "Resonador"]
    dropdown = ttk.Combobox(frameOpciones, value=valoresPredeterminados)
    dropdown.place(x=380, y=30)


def main():
    # Crear la ventana principal
    ventana = Tk()
    ventana.title("Proyecto Programación Científica")
    ventana.geometry("1300x700")
    ventana.configure(background='#ffffff')

    # Crear el frame de matplotlib
    frameMatplot = Frame(ventana, width=600, height=300)
    frameMatplot.place(x=50, y=50)

    # Crear el frame de las opciones
    frameOpciones(ventana)
    
    

    ventana.mainloop()

if __name__ == "__main__":
    main()