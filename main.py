import sys
sys.path.append("./gui")
import main_gui as gui  # noqa
sys.path.append("./evolution_algorithms")
import sampleClass  # noqa


def main():
    backendObj = sampleClass.IncreasingValue()
    obj = gui.GUI(backendObj)

if __name__ == '__main__':
    main()
