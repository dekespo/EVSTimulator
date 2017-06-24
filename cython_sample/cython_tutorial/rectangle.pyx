# distutils: language = c++
# distutils: sources = Rectangle.cpp

from libcpp.vector cimport vector

cdef extern from "Rectangle.h" namespace "shapes":
    cdef cppclass Rectangle:
        Rectangle() except +
        Rectangle(int, int, int, int) except +
        int x0, y0, x1, y1
        int getArea()
        void getSize(int* width, int* height)
        void libVectorStuff()
        void move(int, int)

cdef class PyRectangle:
    cdef Rectangle cRect
    def __cinit__(self, int x0, int y0, int x1, int y1):
        self.cRect = Rectangle(x0, y0, x1, y1)
    def get_area(self):
        return self.cRect.getArea()
    def get_size(self):
        cdef int width, height
        self.cRect.getSize(&width, &height)
        return width, height
    def move(self, dx, dy):
        self.cRect.move(dx, dy)
    def getVector(self):
        return self.cRect.libVectorStuff()
