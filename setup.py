from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='theming.toolkit.javascript',
      version=version,
      description="Usefull javascripts for the theming.toolkit",
      long_description=open('README.rst').read() + '\n' +
                     open(os.path.join('docs', 'HISTORY.txt')).read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='javascript',
      author='Jens Krause',
      author_email='jens@propertyshelf.com',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['theming', 'theming.toolkit'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
