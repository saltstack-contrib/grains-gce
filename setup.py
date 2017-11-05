#!/usr/bin/env python
"""Distutils setup file."""

from distutils.core import setup

setup(name='salt_grain_gce',
      version='0.0.1',
      description='GCE VPS metadata grain for SaltStack',
      author='Iggy',
      author_email='iggy@theiggy.com',
      url='https://github.com/saltstack-contrib/grains-gce',
      py_modules=['_grains/gce'])
