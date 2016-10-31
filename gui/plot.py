import tkinter as tk
import constants as CONST

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import matplotlib.pyplot as plt
import numpy as np

class plotGUI(tk.Frame):
    def __init__(self, parent):
        canvas = tk.Canvas(parent, bg = "blue", width = CONST.plotWindow.width, height = CONST.plotWindow.height)
        fig = plt.Figure()
        plotCanvas = FigureCanvasTkAgg(fig, master = canvas)
        #toolbar = NavigationToolbar2TkAgg(plotCanvas, canvas) # weird error, assumes canvas is pack?
        plotCanvas.get_tk_widget().grid(row = 0, column = 0)
        #toolbar.grid(row = 1, column = 0)
        canvas.grid(row = 0, column = 1)

        x = np.arange(0, 2 * np.pi, 0.01)
        ax = fig.add_subplot(111)
        line, = ax.plot(x, np.sin(x))

