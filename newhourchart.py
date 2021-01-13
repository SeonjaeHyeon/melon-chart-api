from common import ChartUtil


class NewHourChart(ChartUtil):
    __CHART_URL = "https://m2.melon.com/m5/chart/hits/songChartList.json"
    __QUERY_PARAM = {
        "cpId": "AS40",
        "cpKey": "14LNC3",
        "v": "5.0",
        "resolution": "3",
        "appVer": "5.3.0"
    }

    def __init__(self):
        super().__init__(self.__CHART_URL, self.__QUERY_PARAM)

    def get_data(self):
        self._check()

        if self.response is None:
            return None
        chart_list = self.response.get("HITSSONGLIST")
        if chart_list is None:
            return None

        data = []
        for element in chart_list:
            data.append({
                "ARTISTLIST": [artist for artist in element.get("ARTISTLIST")],
                "CURRANK": element.get("CURRANK"),
                "PASTRANK": element.get("PASTRANK"),
                "RANKGAP": element.get("RANKGAP"),
                "RANKTYPE": element.get("RANKTYPE"),
                "SONGID": element.get("SONGID"),
                "SONGNAME": element.get("SONGNAME")
            })

        return data

    def get_artist_chart(self, artist_name):
        if artist_name is None:
            return None

        chart = self.get_data()

        data = []
        for i in chart:
            for j in i["ARTISTLIST"]:
                if j["ARTISTNAME"] == artist_name:
                    data.append(i)

        return data
