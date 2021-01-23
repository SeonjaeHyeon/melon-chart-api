# melon-chart-api

Melon Chart API wrapper on Python 3

## Class Structure
```
.
├─ common.py
│  └─ ChartUtil
│     ├─ _check
│     ├─ load
│     ├─ get_date
│     ├─ get_hour
│     └─ get_data (abstract)
├─ fivechart.py
│  └─ FiveGraph
│     ├─ get_data
│     └─ get_graph
├─ hourchart.py
│  ├─ HourChart
│  │  ├─ get_data
│  │  └─ get_artist_chart
│  └─ HourGraph
│  │  ├─ get_data
│  │  └─ get_graph
└─ newhourchart.py
   └─ NewHourChart
      ├─ get_data
      └─ get_artist_chart
```

## Method
### Common
- **_check**: Check whether the chart data is loaded or not. If not, call load().
- **load**: Get chart data from Melon. The data will be stored as JSON object.
- **get_date**: Get date info when the chart was generated.
- **get_hour**: Get hour info when the chart was generated.
- **get_data**: Get chart list from the chart.

### FiveGraph, HourGraph
- **get_graph**: Make a line graph from the chart data with `matplotlib`.

### HourChart, NewHourChart
- **get_artist_chart**: Search the artist passed as argument and get the artist's chart list from the chart data.

## Usage
```Python
# Five chart
import fivechart

five = fivechart.FiveGraph()
print(five.get_data())

# Five chart graph
import fivechart

five = fivechart.FiveGraph()
five.get_graph(set_name="Python 3")

# Hour artist chart
import hourchart

hour = hourchart.HourChart()
print(hour.get_artist_chart("방탄소년단"))
```

## Requirements
[matplotlib](https://pypi.org/project/matplotlib/)
[requests](https://pypi.org/project/requests/)

## Reference
[GuySomeDC](https://github.com/GuySomeDC/melon-chart-api)
