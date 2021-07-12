# coding=utf-8

"""
setup.py

divia_api is a Python library that allows to retrieve the timetable
of Divia’s bus and tramways straight from a Python script.
Copyright (C) 2021  Firmin Launay

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from setuptools import setup, Extension
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='divia_api',
    packages=['divia_api'],
    version='1.2',
    license='LGPL-3.0',
    description='divia_api is a Python library that allows to retrieve the timetable of Divia’s bus and tramways straight from a Python script.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Firmin Launay',
    author_email='hey@firminlaunay.me',
    url='https://github.com/filau/python_divia_api',
    download_url='https://github.com/filau/python_divia_api/archive/refs/tags/1.2.tar.gz',
    keywords=['divia', 'api', 'firmin', 'launay', 'dijon', 'bus', 'tram'],
    install_requires=[
        'requests'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ]
)
