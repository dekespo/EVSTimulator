import tkinter as tk
import constants as CONST
import circle, utils

class simulationGUI(tk.Frame):
    def __init__(self, parent):
        #tk.Frame.__init__(self, parent)

        self.canvas = tk.Canvas(parent, width = CONST.simulationWindow.width)
        self.placeTheCircles()
        self.canvas.pack(side = tk.LEFT, fill = tk.BOTH)

        # For the interactive gui
        #def callback(event):
        #    self.focus_set()
        #    print("clicked at", event.x, event.y)

        #self.parent.bind("<Button-1>", callback)
        #self.pack()

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

class generationTextGUI(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        generationFrame = tk.Frame(master = parent, bg = "purple", width = CONST.textWindow.width)
        generationFrame.pack(side = tk.RIGHT, fill = tk.Y)

def resizeWindow(root):
    root.geometry(str(CONST.mainWindow.width) + "x" + str(CONST.mainWindow.height))

def startGUI():
    root = tk.Tk()
    resizeWindow(root)
    root.title(CONST.mainWindow.title)
    simulationApp = simulationGUI(root)
    generationTextApp = generationTextGUI(root)
    root.mainloop()
