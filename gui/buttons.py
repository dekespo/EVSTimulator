import tkinter as tk
import constants 

class buttonGUI(tk.Frame):
    def __init__(self, parent):
        const = constants.buttonsWindow
        buttonFrame = tk.Frame(master = parent, bg = const.background, width = const.width, height = const.height)
        #text = tk.StringVar()
        #label = tk.Label(buttonFrame, textvariable = text)
        #text.set("Buttons Part")
        #label.pack(anchor = tk.CENTER)
        buttonFrame.grid(row = const.rowOrder, column = const.colOrder, sticky = "nesw")
