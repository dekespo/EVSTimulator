import tkinter as tk
import constants 

class generationTextGUI(tk.Frame):
    def __init__(self, parent):
        const = constants.textWindow

        generationFrame = tk.Frame(master = parent, bg = const.background, width = const.width, height = const.height)
        generationFrame.grid(row = const.rowOrder, column = const.colOrder, sticky = const.sticky)

        clickNo = 0
        label = tk.Label(generationFrame, text = "Click here\n. The number is #%s" % clickNo)
        label.pack()
        self.label = label
        self.clickNo = clickNo

        generationFrame.bind("<Button-1>", self.click)

    def click(self, event):
        self.clickNo += 1
        self.label["text"] = "Click here\n. The number is %s" % self.clickNo

