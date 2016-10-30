import tkinter as tk
import constants as CONST

from simulation import simulationGUI
from generationText import generationTextGUI
from plot import plotGUI
from buttons import buttonGUI

class GUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(CONST.mainWindow.title)
        self.resizeWindow()
        simulationApp = simulationGUI(self.root)
        generationTextApp = generationTextGUI(self.root)
        plotApp = plotGUI(self.root)
        buttonsApp = buttonGUI(self.root)
        self.root.mainloop()

    def resizeWindow(self):
        self.root.geometry(str(CONST.mainWindow.width) + "x" + str(CONST.mainWindow.height))

