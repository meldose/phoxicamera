#!/usr/bin/env python
from distutils.core import setup # import setup module from distutils
from catkin_pkg.python_setup import generate_distutils_setup # import generate_distutils_setup from catkin

setup_args = generate_distutils_setup( # setup arguments
    packages=['interfaces'], # set packages as list having package names as strings called by interfaces
    package_dir={'': 'test'}, # set package directory as '': 'test'
)

setup(**setup_args) # call setup function