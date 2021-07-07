from .stop import Stop


class Line:
    def __init__(self, api_data, line_data):
        self.api_data = api_data
        self.line_data = line_data
        self.stops = self.line_data["arrets"]

    def get_stop(self, stop_id: str) -> Stop:
        corresponding_stops = list(
            item for item in self.line_data["arrets"].values() if item["id"] == stop_id)
        if len(corresponding_stops) > 0:
            return Stop(self.api_data, self, corresponding_stops[0])

    def find_stop(self, stop_name: str) -> Stop:
        corresponding_stops = list(item for item in self.line_data["arrets"].values() if item["nom"] == stop_name)
        if len(corresponding_stops) > 0:
            return Stop(self.api_data, self, corresponding_stops[0])
