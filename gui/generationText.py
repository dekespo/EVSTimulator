import tkinter as tk
import constants as CONST

class generationTextGUI(tk.Frame):
    def __init__(self, parent):
        generationFrame = tk.Frame(master = parent, bg = "purple", width = CONST.textWindow.width, height = CONST.textWindow.height)
        #text = tk.StringVar()
        #label = tk.Label(generationFrame, textvariable = text)
        #text.set("Generation Text")
        #label.pack(anchor = tk.CENTER)
        generationFrame.grid(row = 1, column = 1, sticky = "nesw")
