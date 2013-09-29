import os.path
from glob import glob

package = 'dai'     # top-level python package name
packagedir = 'dai'  # location of the python package
sourcedir = 'src'      # location of C/C++ source
verbose = True
includes = ['src']
parsers = ['gccxml']

plugins = ('xdress.autoall', 'xdress.autodescribe', 'xdress.cythongen', 'xdress.stlwrap')
extra_types = 'dai_extra_types'

if True:
  classes = []
  #classes += [(type_name, 'util', 'dai') for type_name in ('Real', 'BigInt')]
  classes += [('VarSet', 'varset', 'dai')]

else:
  all_stems = [os.path.basename(file_path)[:-2]
               for file_path in glob(os.path.join(sourcedir, '*.h'))]
  classes = [('*', stem, 'dai') for stem in all_stems]

