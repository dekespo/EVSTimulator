import tkinter as tk
import constants 

class generationTextGUI(tk.Frame):
    def __init__(self, parent):
        const = constants.textWindow
        generationFrame = tk.Frame(master = parent, bg = const.background, width = const.width, height = const.height)
        #text = tk.StringVar()
        #label = tk.Label(generationFrame, textvariable = text)
        #text.set("Generation Text")
        #label.pack(anchor = tk.CENTER)
        generationFrame.grid(row = const.rowOrder, column = const.colOrder, sticky = "nesw")
