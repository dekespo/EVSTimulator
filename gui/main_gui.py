import tkinter as tk
import constants

from simulation import simulationGUI
from generationText import generationTextGUI
from plot import plotGUI
from buttons import buttonGUI

class GUI():
    def __init__(self):
        self.const = constants.mainWindow
        self.root = tk.Tk()
        self.root.title(self.const.title)
        simulationApp = simulationGUI(self.root)
        generationTextApp = generationTextGUI(self.root)
        plotApp = plotGUI(self.root)
        buttonsApp = buttonGUI(self.root)
        self.root.mainloop()
