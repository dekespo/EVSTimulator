import tkinter as tk
import constants 

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import matplotlib.pyplot as plt
import numpy as np

class plotGUI(tk.Frame):
    def __init__(self, parent):
        const = constants.plotWindow
        canvas = tk.Canvas(parent, bg = const.background, width = const.width, height = const.height)
        fig = plt.Figure()
        plotCanvas = FigureCanvasTkAgg(fig, master = canvas)
        #toolbar = NavigationToolbar2TkAgg(plotCanvas, canvas) # weird error, assumes canvas is pack?
        plotCanvas.get_tk_widget().grid(row = 0, column = 0)
        #toolbar.grid(row = 1, column = 0)
        canvas.grid(row = const.rowOrder, column = const.colOrder)

        x = np.arange(0, 2 * np.pi, 0.01)
        ax = fig.add_subplot(111)
        line, = ax.plot(x, np.sin(x))

