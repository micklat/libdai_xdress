package = 'dai'     # top-level python package name
packagedir = 'dai'  # location of the python package
sourcedir = 'src'      # location of C/C++ source
verbose = True
includes = ['src']

plugins = ('xdress.autoall', 'xdress.autodescribe', 'xdress.cythongen', 'xdress.stlwrap')
extra_types = 'dai_extra_types'

classes = [
  ('VarSet', 'varset', 'dai'),
  ]
