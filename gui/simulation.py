import tkinter as tk
import constants as CONST
import circle, utils

class simulationGUI(tk.Frame):
    def __init__(self, parent):

        self.canvas = tk.Canvas(parent, width = CONST.simulationWindow.width, height = CONST.simulationWindow.height)
        self.placeTheCircles()
        self.canvas.grid(row = 0, column = 0, sticky = "nesw")

        # For the interactive gui
        def click(event):
            print("clicked at", event.x, event.y)

        self.canvas.bind("<Button-1>", click)

    def addCircle(self, obj):
        x, y = obj.pos
        r = obj.radius
        self.canvas.create_oval(x - r, y - r, x + r, y + r, outline = "red", fill = "green")

    def placeTheCircles(self):
        placed, idx = [circle.Circle()], 1
        while idx < CONST.bubbles.numberOfCircles:
            newCircle = circle.Circle()
            isOK = True
            for next in placed:
                if utils.circlesIsOverlapCheck(next, newCircle):
                    isOK = False
                    break
            if isOK:
                self.addCircle(newCircle)
                placed.append(newCircle)
                idx += 1
