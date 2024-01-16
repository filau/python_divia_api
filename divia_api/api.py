# coding=utf-8

"""
api.py

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

from json import loads
from typing import Literal

from requests import get

from .velodi import VelodiAPI
from .line import Line
from .stop import Stop
from .exceptions import InvalidWay, LineNotFound


VALID_WAYS = ['A', 'R']


class DiviaAPI:
    """
    The main API, the entrypoint to perform bus & tram TOTEM requests.
    """
    def __init__(self, req_timeout: int = 20) -> None:
        raw_network = get("https://bo-api.divia.fr/api/reseau/type/json", timeout=req_timeout).content.decode("utf-8")
        self.network = loads(raw_network)
        self.lines = self.network["lignes"].values()
        self.stops = self.network["arrets"].values()
        self.velodi = VelodiAPI()  # Deprecated, directly import and initialize VelodiAPI instead.

    def get_line(self, line_id: str) -> Line:
        """
        Find a line by specifying its unique identifier.
        :param line_id: The unique identifier of the line.
        :return: The line found.
        """
        corresponding_lines = list(
            item for item in self.network["arborescence"]["lignes"].values() if item["id"] == line_id)
        if len(corresponding_lines) > 0:
            return Line(self, corresponding_lines[0])
        raise LineNotFound

    def find_line(self, name: str, way: Literal['A', 'R'] = 'A') -> Line:
        """
        Find a line by specifying its name and its way.
        :param name: The name of the line.
        :param way: The way of the line. This can be “A” or “R”.
        :return: The line found.
        """
        way = way.upper()
        if way not in VALID_WAYS:
            raise InvalidWay
        corresponding_lines = list(item for item in self.network["arborescence"]["lignes"].values()
                                   if (item["codetotem"].lower() == name.lower()) and (item["senstotem"] == way))
        if len(corresponding_lines) > 0:
            return Line(self, corresponding_lines[0])
        raise LineNotFound

    def find_stop(self, line_name: str, stop_name: str, way: Literal['A', 'R'] = 'A') -> Stop:
        """
        Find a stop directly by specifying the name of the line, the name of the stop and the way.
        :param line_name: The name of the line.
        :param stop_name: The name of the stop.
        :param way: The way of the line. This can be “A” or “R”.
        :return: The stop found for the line found.
        """
        line = self.find_line(line_name, way)
        if line is not None:
            return line.find_stop(stop_name)
        raise LineNotFound
