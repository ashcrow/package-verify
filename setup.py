#!/usr/bin/env python
"""
Build script.
"""

__docformat__ = 'restructuredtext'


import os
import sys

from setuptools import setup, find_packages

sys.path.insert(0, 'src')

from package_verify import __version__


setup(
    name="package_verify",
    version=__version__,
    description="Package verification tool.",
    long_description="Package verification tool.",
    author='Steve Milner',
    author_email="stevem@gnulinux.net",
    platforms=['any'],

    license="GPLv3+",
    package_dir={
        'package_verify': os.path.join('src', 'package_verify')
    },
    packages=find_packages('src'),
    entry_points={
        'console_scripts': [
            'package-verify=package_verify.script:main',
        ]
    },
    classifiers=[
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python'],
)
