import tkinter as TK
import constants as CONST
import circle


class Example(TK.Frame):
    def __init__(self, parent):
        TK.Frame.__init__(self, parent, background = CONST.window.background)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title(CONST.window.title)
        self.pack(fill = TK.BOTH, expand = 1)

        canvas = TK.Canvas(self)
        for _ in range(5):
            obj = circle.Circle()
            x, y = obj.pos
            r = obj.radius
            canvas.create_oval(x - r, y - r, x + r, y + r, outline = "red", fill = "green")
        canvas.pack(fill = TK.BOTH, expand = 1)


def startGUI():
    root = TK.Tk()
    root.geometry(str(CONST.window.width) + "x" + str(CONST.window.height))
    app = Example(root)
    root.mainloop()
