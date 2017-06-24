import tkinter as tk
import constants

from simulation import simulationGUI
from generationText import generationTextGUI
from plot import plotGUI
from buttons import buttonGUI


class GUI():
    def __init__(self, backendObj):
        self.const = constants.mainWindow
        self.backendObj = backendObj
        self.root = tk.Tk()
        self.root.title(self.const.title)
        self.root.resizable(self.const.resizeX, self.const.resizeY)
        self.centeriseWindow()
        simulationApp = simulationGUI(self.root, self.backendObj)
        generationTextApp = generationTextGUI(self.root, self.backendObj)
        plotApp = plotGUI(self.root)
        buttonsApp = buttonGUI(self.root)
        self.root.mainloop()

    def centeriseWindow(self):
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()
        winWidth = self.const.width
        winHeigth = self.const.height
        startPosX = screenWidth // 2 - winWidth // 2
        startPosY = screenHeight // 2 - winHeigth // 2
        self.root.geometry("+%d+%d" % (startPosX, startPosY))
