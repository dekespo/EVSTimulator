import tkinter as tk
import constants as CONST

class buttonGUI(tk.Frame):
    def __init__(self, parent):
        buttonFrame = tk.Frame(master = parent, bg = "yellow", width = CONST.buttonsWindow.width, height = CONST.buttonsWindow.height)
        #text = tk.StringVar()
        #label = tk.Label(buttonFrame, textvariable = text)
        #text.set("Buttons Part")
        #label.pack(anchor = tk.CENTER)
        buttonFrame.grid(row = 1, column = 0, sticky = "nesw")
