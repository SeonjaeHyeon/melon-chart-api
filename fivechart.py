import time
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

from common import ChartUtil


class FiveGraph(ChartUtil):
    __CHART_URL = "https://m2.melon.com/chart/hourly/fiveChartGraph.json"
    __QUERY_PARAM = {
        "cpId": "AS40",
        "cpKey": "14LNC3",
        "v": "4.0",
        "resolution": "2",
        "appVer": "5.1.2"
    }

    def __init__(self):
        super().__init__(self.__CHART_URL, self.__QUERY_PARAM)

    def get_data(self):
        self._check()

        if self.response is None:
            return None

        chart_list = self.response.get("GRAPHDATALIST")
        if chart_list is None:
            return None

        return chart_list

    def get_graph(self, font_path="NanumBarunGothic.ttf", img_path="five.png", set_name="Python 3"):
        chart = self.get_data()
        font_name = font_manager.FontProperties(fname=font_path).get_name()
        rc('font', family=font_name)

        plt.rcParams['axes.facecolor'] = '#434F67'

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        x = list()
        for i in range(0, len(chart[0]['GRAPHDATA']) - 1):
            x.append(i * 5)

        data = []
        for i in chart:
            temp = []
            for j in i["GRAPHDATA"][1:]:
                value = j.get("VAL", 0)
                if value == "":
                    value = 0
                temp.append(float(value))
            data.append({"name": i["GRAPHCHARTINFO"]["SONGNAME"], "data": temp})

        line_color = ['#A7E52E', '#F6894E', '#59AFE5', '#39C5C2', '#FD7DB9', '#C998FF']

        for i in range(0, len(chart)):
            line = plt.plot(x, data[i]['data'], line_color[i], label=data[i]['name'])
            plt.setp(line, linewidth=3.0)

            for j, k in zip(x, data[i]['data']):
                ax.annotate(str(round(k, 2)), xy=(j, k), color=line_color[i], size=15)

        max_data = list()
        for i in range(0, len(chart)):
            max_data.append(max(data[i]['data']))

        y = list()
        for i in range(0, int(max(max_data)) + 2):
            y.append(i)
        ax.set_yticks(y)

        ax.set_xlim(0, 60)
        ax.set_ylim(0, round(max(max_data), 2) + 1.0)

        t = time.localtime()
        plt.title("[%04d%02d%02d %02d:%02d] 멜론 5분 차트  by %s" % (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, x[len(x) - 1], set_name), size=15)

        plt.grid()

        plt.legend()
        legend = plt.legend()
        frame = legend.get_frame()
        frame.set_facecolor('white')

        if os.path.isfile(img_path):
            os.remove(img_path)
        graph = plt.gcf()
        plt.subplots_adjust(top=1, bottom=0, right=1.25, left=0, hspace=0, wspace=0)
        graph.savefig(img_path, bbox_inches='tight', pad_inches=0)

        return None
