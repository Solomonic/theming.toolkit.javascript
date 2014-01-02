# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

version = '0.1dev'

setup(
      name='theming.toolkit.javascript',
      version=version,
      description="Useful javascripts for the theming.toolkit",
      long_description=open('README.rst').read() + '\n' +
                     open(os.path.join('docs', 'HISTORY.txt')).read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='javascript',
      author='Jens Krause',
      author_email='jens@propertyshelf.com',
      url='https://github.com/Solomonic/theming.toolkit.javascript',
      license='gpl',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir = {'': 'src'},
      namespace_packages=['theming', 'theming.toolkit'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      extras_require={
             'test': ['plone.app.testing',]
      },
      entry_points="""
        # -*- Entry points: -*- 
        [z3c.autoinclude.plugin]
        target = plone
        """,
      )
