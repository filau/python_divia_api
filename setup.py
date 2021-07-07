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

from distutils.core import setup

setup(
    name='divia_api',
    packages=['divia_api'],
    version='1.0.0',
    license='LGPL-3.0',
    description='divia_api is a Python library that allows to retrieve the timetable of Divia’s bus and tramways straight from a Python script.',
    author='Firmin Launay',
    author_email='hey@firminlaunay.me',
    url='https://github.com/filau/python_divia_api',
    download_url='https://github.com/filau/python_divia_api/archive/refs/tags/1.0.0.tar.gz',
    keywords=['divia', 'api', 'firmin', 'launay', 'dijon', 'bus', 'tram'],
    install_requires=[
        'requests'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: LGPL-3.0 License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ]
)
