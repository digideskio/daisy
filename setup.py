#!/usr/bin/env python
from setuptools import setup, find_packages
import sys

long_description = ''

if 'upload' in sys.argv:
    with open('README.rst') as f:
        long_description = f.read()


setup(
    name='daisy',
    version='0.1.0',
    description='dask + lazy = daisy',
    author='Joe Jevnik',
    author_email='joejev@gmail.com',
    packages=find_packages(),
    long_description=long_description,
    license='GPL-2',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: POSIX',
        'Topic :: Software Development :: Pre-processors',
    ],
    url='https://github.com/llllllllll/daisy',
    install_requires=['dask', 'lazy_python'],
    extras_require={
        'dev': [
            'flake8==2.4.0',
            'pytest==2.8.4',
            'pytest-cov==2.2.1',
        ],
    },
)
