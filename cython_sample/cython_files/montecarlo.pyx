# disutils: language = c++
# disutils: sources = ../cpp_files/MonteCarlo.cpp

#from libc.stdlib cimport stdlib
from libc.time cimport time
#from libcpp.vector cimport vector
#from libcpp.iterator cimport iterator

cdef extern from "../cpp_files/MonteCarlo.h" namespace "monteCarlo_NS":
    cdef cppclass MonteCarlo:
        MonteCarlo() except +
        MonteCarlo(int) except +
        void calculate()
        double getResult()

cdef class PyMonteCarlo:
    cdef MonteCarlo cppMonte
    def __cinit__(self):
        self.cppMonte = MonteCarlo()
    def __cinit__(self, int sampleNo):
        self.cppMonte = MonteCarlo(sampleNo)
    def calculate(self):
        self.cppMonte.calculate()
    def getResult(self):
        return self.cppMonte.getResult()

