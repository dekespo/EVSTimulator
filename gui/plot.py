import tkinter as tk
import constants

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2TkAgg
)
import matplotlib.pyplot as plt
import numpy as np


class plotGUI(tk.Frame):
    def __init__(self, parent):
        const = constants.plotWindow

        frame = tk.Frame(parent, bg=const.background,
                         width=const.width, height=const.height)

        canvas = tk.Canvas(frame, bg=const.background,
                           width=const.width, height=const.height)

        # Not sure if it is safe enough ie. valid for all screens?
        pixelOverInche = 80
        fig = plt.Figure(figsize=(frame.winfo_reqwidth() / pixelOverInche,
                                  frame.winfo_reqheight() / pixelOverInche))

        plotCanvas = FigureCanvasTkAgg(fig, master=canvas)
        # We might need to make the toolbar smaller in future
        toolbar = NavigationToolbar2TkAgg(plotCanvas, canvas)
        toolbar.update()
        plotCanvas._tkcanvas.pack()

        x = np.arange(0, 2 * np.pi, 0.01)
        ax = fig.add_subplot(211)
        line, = ax.plot(x, np.sin(x))
        ax = fig.add_subplot(212)
        line, = ax.plot(x, np.cos(x))

        canvas.grid()
        frame.grid(row=const.rowOrder, column=const.colOrder,
                   sticky=const.sticky)
