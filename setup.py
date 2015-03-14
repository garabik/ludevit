#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(name='ludevít',
      version='1',
      description='converter from standard Slovak into L. Štúr version',
      author='Radovan Garabík',
      author_email='garabik@kassiopeia.juls.savba.sk',
      url='http://kassiopeia.juls.savba.sk/~garabik/software/ludevit/',
      packages=['ludevit_trans'],
      scripts=['ludevit', 'ludevit_tk'],
     )
