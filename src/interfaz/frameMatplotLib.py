from tkinter import Frame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def frameMatplotlib(ventana):
    frameMatplot = Frame(ventana, width=650, height=550)
    frameMatplot.place(x=0, y=0)
    figure = plt.Figure(figsize=(6,5))
    subplot = figure.add_subplot(111)
    subplot.plot()
    canvas = FigureCanvasTkAgg(figure, master=frameMatplot)
    canvas.get_tk_widget().place(x=0, y=0)
    canvas.draw()
    return canvas, subplot