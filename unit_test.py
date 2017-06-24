import unittest
import constants
# sys.path.append("./gui")
# import main_gui as gui  # noqa


class GUI(unittest.TestCase):

    def test_windowSizeTest(self):
        mainWin = constants.mainWindow

        simuWin = constants.simulationWindow
        buttWin = constants.buttonsWindow
        textWin = constants.textWindow
        plotWin = constants.plotWindow

        totalWidth1 = simuWin.width + plotWin.width
        totalWidth2 = textWin.width + buttWin.width

        totalHeight1 = textWin.height + plotWin.height
        totalHeight2 = simuWin.height + buttWin.height

        self.assertEqual(mainWin.width, totalWidth1)
        self.assertEqual(mainWin.height, totalHeight1)
        self.assertEqual(mainWin.width, totalWidth2)
        self.assertEqual(mainWin.height, totalHeight2)


if __name__ == '__main__':
    unittest.main()
