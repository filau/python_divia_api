from requests import post
from datetime import datetime, timedelta


two_minutes = timedelta(minutes=2)
one_day = timedelta(days=1)


class Stop:
    def __init__(self, api_data, line, stop_data):
        self.api_data = api_data
        self.line = line
        self.stop_data = stop_data

    def totem(self) -> list:
        result = []
        try:
            html_totem = post("https://www.divia.fr/bus-tram?type=479",
                 headers={
                     "Content-Type": "application/x-www-form-urlencoded",
                     "X-Requested-With": "XMLHttpRequest"
                 },
                 data=f"requete=arret_prochainpassage&requete_val%5Bid_ligne%5D={self.line.line_data['id']}&requete_val%5Bid_arret%5D={self.stop_data['code']}"
                 ).content.decode("utf-8")
            two = False
            if html_totem.count("<span class=\"uk-badge\">") > 1:
                two = True
            now = datetime.now()
            time_1 = html_totem.split("<span class=\"uk-badge\"> ")[1].split("</span>")[0].split(":")
            time_1_today = datetime(now.year, now.month, now.day, int(time_1[0]), int(time_1[1]), 0)

            if (now - two_minutes) > time_1_today:
                result.append(time_1_today + one_day)
            else:
                result.append(time_1_today)
            if two:
                time_2 = html_totem.split("<span class=\"uk-badge\"> ")[2].split("</span>")[0]
                time_2_today = datetime(now.year, now.month, now.day, int(time_2[0]), int(time_2[1]), 0)
                if (now - two_minutes) > time_2_today:
                    result.append(time_2_today + one_day)
                else:
                    result.append(time_2_today)
        finally:
            return result
