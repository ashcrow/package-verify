#!/usr/bin/env python
#
# Copyright (C) 2014 Steve Milner
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
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
