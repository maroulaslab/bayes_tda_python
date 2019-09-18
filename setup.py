# setup.py 

from distutils.core import setup
setup(
  name = 'bayes_tda',
  packages = ['bayes_tda'],   
  version = '0.1',      
  license='MIT',        
  description = 'Point process model for Bayesian inference with persistence diagrams.',
  author = 'Christopher Oballe',
  author_email = 'coballejr@gmail.com',      
  url = 'https://github.com/coballejr/bayes_tda/',
  download_url = 'https://github.com/coballejr/bayes_tda/archive/v_01.tar.gz',
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

