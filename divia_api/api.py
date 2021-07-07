from requests import get
from json import loads
from .line import Line
from .stop import Stop
from .exceptions import InvalidWay


valid_ways = ["A", "R"]


class DiviaAPI:
    def __init__(self):
        raw_network = get("https://bo-api.divia.fr/api/reseau/type/json").content.decode("utf-8")
        self.network = loads(raw_network)
        self.lines = self.network["lignes"].values()
        self.stops = self.network["arrets"].values()

    def get_line(self, line_id: str) -> Line:
        corresponding_lines = list(
            item for item in self.network["arborescence"]["lignes"].values() if item["id"] == line_id)
        if len(corresponding_lines) > 0:
            return Line(self, corresponding_lines[0])

    def find_line(self, name: str, way: str = "A") -> Line:
        if way not in valid_ways:
            raise InvalidWay
        corresponding_lines = list(item for item in self.network["arborescence"]["lignes"].values()
                                   if (item["codetotem"] == name) and (item["senstotem"] == way))
        if len(corresponding_lines) > 0:
            return Line(self, corresponding_lines[0])

    def find_stop(self, line_name: str, stop_name: str, way: str = "A") -> Stop:
        line = self.find_line(line_name, way)
        if line is not None:
            return line.find_stop(stop_name)
