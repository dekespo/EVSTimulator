class mainWindow:
    width, height = 800, 600
    title = "EVSTimulator"


class simulationWindow:
    width, height = mainWindow.width * 2 // 3, mainWindow.height * 4 // 5
    rowOrder, colOrder = 0, 0
    background = "black"
    sticky = "nsew"


class buttonsWindow:
    width, height = mainWindow.width * 4 // 5, mainWindow.height * 1 // 5
    rowOrder, colOrder = 1, 0
    background = "yellow"
    sticky = "nsew"


class textWindow:
    width, height = mainWindow.width * 1 // 5, mainWindow.height * 1 // 5
    rowOrder, colOrder = 1, 1
    background = "purple"
    sticky = "nsew"


class plotWindow:
    width, height = mainWindow.width * 1 // 3, mainWindow.height * 4 // 5
    rowOrder, colOrder = 0, 1
    background = "blue"
    sticky = "nsew"


class bubbles:
    numberOfCircles = 25
