# coding=utf-8

"""
exceptions.py

divia_api is a Python library that allows to retrieve the timetable
of Divia’s bus and tramways straight from a Python script.
Copyright (C) 2024  Firmin Launay

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

from sys import exit


# TODO: Improve exceptions implementation, there is a better way.


class InvalidWay(Exception):
    def __init__(self) -> None:
        print("Exception: The way can only be “A” or “R”. Exiting.")
        exit(1)


class LineNotFound(Exception):
    def __init__(self) -> None:
        print("Exception: The line you specified cannot be found. Exiting.")
        exit(1)


class DataNotFound(Exception):
    def __init__(self) -> None:
        print("Exception: The data could not be pulled from the web. Exiting.")
        exit(2)
