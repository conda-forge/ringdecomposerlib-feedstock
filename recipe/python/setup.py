import sys
import sysconfig
from pathlib import Path

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

include_dirs  = [sysconfig.get_paths()["include"]]
library_dirs  = []

static_libs = []
shared_libs   = ['RingDecomposerLib']

root = Path(__file__).parent.resolve()

extensions = [
    Extension('py_rdl.wrapper.DataInternal',
              [str(root / 'py_rdl' / 'wrapper' / 'DataInternal.pyx')],
        extra_objects=static_libs,
        include_dirs=include_dirs,
        libraries=shared_libs,
        library_dirs=library_dirs)]

setup(name = 'py_rdl',
      ext_modules = cythonize(extensions),
      package_dir={'' : str(root)},
      packages=['py_rdl', 'py_rdl.wrapper'])
