import tkinter as TK
import constants as CONST
import circle, utils


class Example(TK.Frame):
    def __init__(self, parent):
        TK.Frame.__init__(self, parent, background = CONST.window.background)
        self.parent = parent
        self.canvas = TK.Canvas(self)
        self.initUI()


    def initUI(self):
        self.parent.title(CONST.window.title)
        self.pack(fill = TK.BOTH, expand = 1)

        self.placeTheCircles()

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
        self.canvas.pack(fill = TK.BOTH, expand = 1)



def startGUI():
    root = TK.Tk()
    root.geometry(str(CONST.window.width) + "x" + str(CONST.window.height))
    app = Example(root)
    root.mainloop()
