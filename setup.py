#!/usr/bin/env python

from setuptools import setup

description = 'Useful functions for working with data in Python/Pandas.'

setup(
    name='data-helpers',
    version='0.1.0',
    description=description,
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='Geoff Hing',
    author_email='geoffhing@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=[
        'data_helpers',
    ],
    install_requires=[],
)
