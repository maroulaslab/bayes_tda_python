# setup.py 

from setuptools import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'bayes_tda',
  packages = ['bayes_tda'],   
  version = '0.2',      
  license='MIT',        
  description = 'Point process model for Bayesian inference with persistence diagrams.',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  author = 'Christopher Oballe',
  author_email = 'coballejr@gmail.com',      
  url = 'https://github.com/coballejr/bayes_tda/',
  download_url = 'https://github.com/coballejr/bayes_tda/archive/v_02.tar.gz',
  keywords = ['Persistent Homology', 'Topological Data Analysis', 'Bayesian','Point process', 'Poisson process'],   # Keywords that define your package best
  install_requires=[            
          'numpy',
          'scipy',
          'itertools'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Science/Research',      
    'Topic :: Scientific/Engineering :: Mathematics',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)

