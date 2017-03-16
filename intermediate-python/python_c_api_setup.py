# build the modules
# python python_c_api_setup.py install

from distutils.core import setup, Extension

setup(name='addList', version='1.0', \
      ext_modules=[Extension('addList', ['adder.c'])])
