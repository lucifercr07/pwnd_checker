#!/usr/bin/env python

from setuptools import setup, find_packages
import os, sys

# if you are not using vagrant, just delete os.link directly,
# The hard link only saves a little disk space, so you should not care
if os.environ.get('USER','') == 'vagrant':
    del os.link

setup(
    name='pwnd_checker',
    version='0.0.1',
    description='Pwnd Checker',
    author='Prashant Shubham',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords="password checker tool cli",
    author_email='prashant1996cr07@gmail.com',
    url='https://github.com/lucifercr07/pwnd_checker',
    packages=find_packages(),
    include_package_data = True,
    install_requires=[
        "click==7.0",
        "requests==2.20.1"
    ] + (["colorama==0.3.3"] if "win" in sys.platform else []),
    entry_points={
        'console_scripts': [
            'pwnd_checker = pwnd_checker.main:main'
        ],
    }
)
