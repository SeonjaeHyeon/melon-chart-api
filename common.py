import json
from abc import ABCMeta, abstractmethod
import requests


class ChartUtil(metaclass=ABCMeta):
    def __init__(self, chart_url, query_param):
        self.__CHART_URL = chart_url
        self.__QUERY_PARAM = query_param

        self.__session = requests.Session()
        self.__session.headers["User-Agent"] = "AS40; Android 8.1.0; 5.1.2; LM-X415L"
        self.__session.headers["Host"] = "m2.melon.com"
        self.load()

    def _check(self):
        while self.__page is None:
            self.load()

    def load(self):
        self.__page = self.__session.get(self.__CHART_URL, params=self.__QUERY_PARAM, timeout=5)
        if self.__page.status_code != 200:
            print("Failed to load chart page. Status code: %s" % self.__page.status_code)
            self.__page = None

        self.response = json.loads(self.__page.text).get("response")

    def get_date(self):
        self._check()

        if self.response is None:
            return None
        return self.response.get("RANKDAY")

    def get_hour(self):
        self._check()

        if self.response is None:
            return None
        return self.response.get("RANKHOUR")

    @abstractmethod
    def get_data(self):
        pass
