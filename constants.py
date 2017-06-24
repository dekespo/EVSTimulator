class mainWindow:
    width, height = 800, 600
    title = "EVSTimulator"
    resizeX, resizeY = False, False


class simulationWindow:
    width = round(mainWindow.width * 2 / 3)
    height = round(mainWindow.height * 4 / 5)
    rowOrder, colOrder = 0, 0
    background = "black"
    sticky = "nsew"


class buttonsWindow:
    width = round(mainWindow.width * 4 / 5)
    height = round(mainWindow.height * 1 / 5)
    rowOrder, colOrder = 1, 0
    background = "yellow"
    sticky = "nsew"


class textWindow:
    width = round(mainWindow.width * 1 / 5)
    height = round(mainWindow.height * 1 / 5)
    rowOrder, colOrder = 1, 1
    background = "purple"
    sticky = "nsew"


class plotWindow:
    width = round(mainWindow.width * 1 / 3)
    height = round(mainWindow.height * 4 / 5)
    rowOrder, colOrder = 0, 1
    background = "blue"
    sticky = "nsew"


class bubbles:
    numberOfCircles = 25
