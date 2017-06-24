from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext
import os


localExtension = Extension(
        "rectangle",
        sources=["rectangle.pyx", "Rectangle.cpp"],
        language="c++",
        # extra_compile_args=["-I ./"],
        # extra_link_args=[]
        # depends=["Rectangle.h"]
        # libraries=["m"]
        )

setup(
    name='rectangleApp',
    # include_dirs=["/usr/lib/python3/dist-packages()"],
    # cmdclass={ 'build_ext' : build_ext },
    ext_modules=cythonize(localExtension)
    )
