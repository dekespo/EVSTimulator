class mainWindow:
    width, height = 800, 600
    title = "EVSTimulator"

class simulationWindow:
    width, height = mainWindow.width * 2 // 3, mainWindow.height * 4 // 5 

class buttonsWindow:
    width, height = mainWindow.width * 4 // 5, mainWindow.height * 1 // 5

class textWindow:
    width, height = mainWindow.width * 1 // 5, mainWindow.height * 1 // 5

class plotWindow:
    width, height = mainWindow.width * 1 // 3, mainWindow.height * 4 // 5

class bubbles:
    numberOfCircles = 25
