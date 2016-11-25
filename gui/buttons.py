import tkinter as tk
import constants


class buttonGUI(tk.Frame):
    def __init__(self, parent):
        const = constants.buttonsWindow

        self.parent = parent

        buttonFrame = tk.Frame(master=parent, bg=const.background,
                               width=const.width, height=const.height)
        buttonFrame.grid(row=const.rowOrder, column=const.colOrder,
                         sticky=const.sticky)

        buttonLeft = tk.Button(master=buttonFrame, text="Left",
                               command=self.clickLeftButton)
        buttonMiddle = tk.Button(master=buttonFrame, text="Middle",
                                 command=self.clickMiddleButton)
        buttonRight = tk.Button(master=buttonFrame, text="Right",
                                command=self.clickRightButton)

        buttonLeft.pack(side="left")
        buttonMiddle.pack(side="top")
        buttonRight.pack(side="right")

    def clickLeftButton(self):
        newWindow = tk.Toplevel(self.parent)
        label = tk.Label(newWindow,
                         text="This is Left button, my dear friend")
        label.pack()

    def clickMiddleButton(self):
        newWindow = tk.Toplevel(self.parent)
        label = tk.Label(newWindow,
                         text="This is Middle button, my dear friend")
        label.pack()

    def clickRightButton(self):
        newWindow = tk.Toplevel(self.parent)
        label = tk.Label(newWindow,
                         text="This is Right button, my dear friend")
        label.pack()
