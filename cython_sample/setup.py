from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext
import os


# Name of dynamic, make sure the dynamic name has the same name with pyx file
pyxName = "montecarlo"

# Always starts with capital letter as cython will generate a new one
# with small letter
cppName = "MonteCarlo"

localExtension = Extension(
        pyxName,
        sources=[
            "cython_files/" + pyxName + ".pyx",
            "cpp_files/" + cppName + ".cpp"
            ],
        language="c++",
        )

setup(
    name='MonteCarloApp',
    ext_modules=cythonize(localExtension)
    )
