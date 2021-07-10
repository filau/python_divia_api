# coding=utf-8

"""
line.py

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

from .stop import Stop


class Line:
    def __init__(self, api_data, line_data):
        self.api_data = api_data
        self.line_data = line_data
        self.stops = self.line_data["arrets"]

    def get_stop(self, stop_id: str) -> Stop:
        """Find a stop by specifying its unique identifier."""
        corresponding_stops = list(
            item for item in self.line_data["arrets"].values() if item["id"] == stop_id)
        if len(corresponding_stops) > 0:
            return Stop(self.api_data, self, corresponding_stops[0])

    def find_stop(self, stop_name: str) -> Stop:
        """Find a stop by specifying its name."""
        corresponding_stops = list(item for item in self.line_data["arrets"].values() if item["nom"] == stop_name)
        if len(corresponding_stops) > 0:
            return Stop(self.api_data, self, corresponding_stops[0])
        corresponding_stops = list(item for item in self.line_data["arrets"].values()
                                   if item["nom"].replace(" " + self.line_data["codetotem"], "").lower() ==
                                   stop_name.lower().replace(" " + self.line_data["codetotem"].lower(), ""))
        if len(corresponding_stops) > 0:
            return Stop(self.api_data, self, corresponding_stops[0])
