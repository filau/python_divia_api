# coding=utf-8

"""
velodi.py

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
from .normalize_characters import normalize
# from normalize_characters import normalize


def update_source() -> list:
    raw_response = get(
        "https://www.divia.fr/velo/diviavelodi/ou-trouver-les-stations-diviavelodi").content.decode("utf-8")
    data = raw_response.split("var datas = ")[1].split(";")[0]
    return loads(data)["diviavelodi"]


class FreeVelodi:
    def __init__(self, station, bikes: int, docks: int):
        self.station = station
        self.bikes = bikes
        self.docks = docks

    def __str__(self):
        return f"{self.bikes} free bikes & {self.docks} free docks."


class VelodiStation:
    def __init__(self, code: str, raw_name: str, friendly_name: str):
        self.code = code
        self.raw_name = raw_name
        self.friendly_name = friendly_name

    def check_cached(self):  # Checking method used in previous versions, that is signficantly faster but did not really provide realtime results because of caching issues.
        """This may not be realtime data !!!!"""
        velodi_data = update_source()
        query_result = list(item for item in velodi_data if (item["infos"]["code_cykleo"] == self.code))
        try:
            free = query_result[0]["infos"]["qucit"]["realtime"]
            return FreeVelodi(self, free["bikes"], free["docks"])
        except IndexError:
            raise Exception("Data not found.")

    def check(self):
        velodi_data = update_source()
        query_result = list(item for item in velodi_data if (item["infos"]["code_cykleo"] == self.code))
        try:
            response = get("https://www.divia.fr" + query_result[0]["url"]).content.decode("utf-8")
            response = response.split("<span class=\"uk-indicateur-value\">")
            free_bikes = int(response[1].split("</span>")[0])
            free_docks = int(response[2].split("</span>")[0])
            return FreeVelodi(self, free_bikes, free_docks)
        except IndexError:
            raise Exception("Data not found.")


class Velodi:
    def __init__(self):
        self.data = update_source()
        self.stations = []

        for station in self.data:
            station_name = station["infos"]["nom"]
            if " - n°" in station_name.replace("  ", ' ').lower():
                friendly_name = " - ".join(station_name.replace("  ", ' ').split(" - ")[:-1])
            else:
                friendly_name = station_name.split(" n°")[0].split(" N°")[0]
            self.stations.append(VelodiStation(station["infos"]["code_cykleo"], station_name, friendly_name))

    def find_station(self, station_name: str) -> VelodiStation:
        corresponding_stations = list(
            item for item in self.stations if (item.friendly_name == station_name) or (item.raw_name == station_name))
        if len(corresponding_stations) > 0:
            return corresponding_stations[0]
        corresponding_stations = list(item for item in self.stations
                                      if normalize(
            item.friendly_name.lower()) == normalize(station_name.lower()) or normalize(
            item.raw_name.lower()) == normalize(station_name.lower()))
        if len(corresponding_stations) > 0:
            return corresponding_stations[0]

    def get_station(self, station_code: str) -> VelodiStation:
        corresponding_stations = list(item for item in self.stations if item.code == station_code)
        if len(corresponding_stations) > 0:
            return corresponding_stations[0]

    def find_stations(self, station_names: list) -> list:
        stations = []
        for station_name in station_names:
            stations.append(self.find_station(station_name))
        return stations

    def get_stations(self, station_codes: list) -> list:
        stations = []
        for station_code in station_codes:
            stations.append(self.get_station(station_code))
        return stations

    def check_multiple_stations(self, stations: list) -> list:
        velodi_data = update_source()
        results = []
        for station in stations:
            query_result = list(item for item in velodi_data if (item["infos"]["code_cykleo"] == station.code))
            try:
                free = query_result[0]["infos"]["qucit"]["realtime"]
                results.append(FreeVelodi(station, free["bikes"], free["docks"]))
            except IndexError:
                raise Exception("Data not found.")
        return results
