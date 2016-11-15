import tkinter as tk
import constants 
import circle, utils

class simulationGUI(tk.Frame):
    def __init__(self, parent):
        const = constants.simulationWindow

        self.canvas = tk.Canvas(parent, bg = const.background, width = const.width, height = const.height)
        self.canvasSizes = (self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight())
        self.placeTheCircles()
        self.canvas.grid(row = const.rowOrder, column = const.colOrder, sticky = const.sticky)

        # For the interactive gui
        def click(event):
            print("clicked at", event.x, event.y)

        self.canvas.bind("<Button-1>", click)

    def addCircle(self, obj):
        x, y = obj.pos
        r = obj.radius
        self.canvas.create_oval(x - r, y - r, x + r, y + r, outline = "red", fill = "green")

    def placeTheCircles(self):
        placed, idx = [circle.Circle(self.canvasSizes)], 1
        while idx < constants.bubbles.numberOfCircles:
            newCircle = circle.Circle(self.canvasSizes)
            isOK = True
            for next in placed:
                if utils.circlesIsOverlapCheck(next, newCircle):
                    isOK = False
                    break
            if isOK:
                self.addCircle(newCircle)
                placed.append(newCircle)
                idx += 1
