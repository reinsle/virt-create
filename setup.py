#!/usr/bin/env python

from setuptools import setup

setup(name='virt-create',
      version='0.0.1',
      description='Virtual Machine creation helper',
      packages=['virtcreate', ],
      install_requires=['sh', 'configparser'],
      entry_points={
          'console_scripts': [
              'virt-create = virtcreate.main:entry_point',
          ]
      },
)
