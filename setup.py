#!/usr/bin/env python

from setuptools import setup

import sys

setup(name="mri_recon",
      version='0.12',
      install_requires=[
        'ConfigArgParse>=0.11',
        'numpy',
        'pyminc',
        'typing',
      ],
      packages=['mri_recon'],
      scripts=['mri_recon/mri_recon.py'
               ],
      )
