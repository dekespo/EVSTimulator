import sys
sys.path.append("./dynamic_libraries")
sys.path.append("./cython_files")
import montecarlo  # noqa


class MonteCarlo():
    def __init__(self, sampleNo=10000):
        self.monteCarloObj = montecarlo.PyMonteCarlo(sampleNo)
        self.monteCarloObj.calculate()

    def __repr__(self):
        return "Monte Carlo Average Result = " + \
                str(self.monteCarloObj.getResult())

    def __str__(self):
        return self.__repr__()


myObj = MonteCarlo()
print(myObj)
