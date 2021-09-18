#!/usr/bin/env python
import os
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

import pickle_db

tests_requires = [
    'pytest==3.0.3',
    'pytest-cov==2.4.0',
]


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['tests', '--cov=pyconst', '-vrsx']
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(name='pickle_db',
      url='https://github.com/valdergallo/pickle_db',
      download_url='https://github.com/valdergallo/pickle_db/tarball/%s/' % pickle_db.get_version(),
      author="valdergallo",
      author_email='valdergallo@gmail.com',
      keywords=['constants', 'dbm', 'data', 'control', 'database', 'pickle', 'filemanager', 'singleton', 'pyQT', 'simpleGUI', 'tinker', 'kivy'],
      description='PickleDB use pickle file as database similiar as DBM to save state of complex objects',
      license='GPL-3.0',
      classifiers=[
          'Operating System :: OS Independent',
          'Topic :: Utilities',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      include_package_data=True,
      version=pickle_db.get_version(),
      tests_require=tests_requires,
      cmdclass={'test': PyTest},
      packages=['pickle_db'],
      zip_safe=False,
      platforms='any',
)