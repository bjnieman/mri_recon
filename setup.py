#!/usr/bin/env python

from setuptools import setup

import sys

setup(name="mri_python",
      version='0.12',
      install_requires=[
        'ConfigArgParse>=0.11',
        'numpy',
        'pyminc',
        'typing',
      ],
      #zip_safe= False,
      packages=['mri_python'],
      scripts=['mri_python/mri_recon.py'
               ],
      )
