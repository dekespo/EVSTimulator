import tkinter as tk
import constants as CONST

class plotGUI(tk.Frame):
    def __init__(self, parent):
        canvas = tk.Canvas(parent, bg = "blue", width = CONST.plotWindow.width, height = CONST.plotWindow.height)
        #text = tk.StringVar()
        #label = tk.Label(canvas, textvariable = text)
        #text.set("Plot Part")
        #label.pack(anchor = tk.CENTER)
        canvas.grid(row = 0, column = 1, sticky = "nesw")
