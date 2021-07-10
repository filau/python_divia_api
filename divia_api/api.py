# coding=utf-8

"""
api.py

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

from requests import get
from json import loads
from .line import Line
from .stop import Stop
from .exceptions import InvalidWay


valid_ways = ['A', 'R']


class DiviaAPI:
    def __init__(self):
        raw_network = get("https://bo-api.divia.fr/api/reseau/type/json").content.decode("utf-8")
        self.network = loads(raw_network)
        self.lines = self.network["lignes"].values()
        self.stops = self.network["arrets"].values()

    def get_line(self, line_id: str) -> Line:
        """Find a line by specifying its unique identifier."""
        corresponding_lines = list(
            item for item in self.network["arborescence"]["lignes"].values() if item["id"] == line_id)
        if len(corresponding_lines) > 0:
            return Line(self, corresponding_lines[0])

    def find_line(self, name: str, way: str = 'A') -> Line:
        """Find a line by specifying its name and its way."""
        way = way.upper()
        if way not in valid_ways:
            raise InvalidWay
        corresponding_lines = list(item for item in self.network["arborescence"]["lignes"].values()
                                   if (item["codetotem"].lower() == name.lower()) and (item["senstotem"] == way))
        if len(corresponding_lines) > 0:
            return Line(self, corresponding_lines[0])

    def find_stop(self, line_name: str, stop_name: str, way: str = 'A') -> Stop:
        """Find a stop directly by specifying the name of the line, the name of the stop and the way."""
        line = self.find_line(line_name, way)
        if line is not None:
            return line.find_stop(stop_name)
