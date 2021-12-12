#!/usr/bin/env python3
# coding=utf-8

import numpy as np
import os

import bokeh
import bokeh.models
from bokeh.plotting import figure, output_file, show

from bokeh.models import ColumnDataSource, DatetimeAxis

plot = figure(plot_width=400, plot_height=400,
              # y_axis_type="log",
              tools='pan, wheel_zoom, reset, hover, crosshair, tap')
# 设置时间轴
plot.add_layout(DatetimeAxis(), 'below')
plot.add_layout(DatetimeAxis(), 'left')
from bokeh.models import ColumnDataSource, DatetimeAxis, DatetimeTickFormatter

xformatter = DatetimeTickFormatter(months="%b %d %Y")
from time import mktime

min_time = dt.datetime.min.time()
xticker = FixedTicker(ticks=[
    mktime(dt.datetime.combine(summer_start, min_time).timetuple()) * 1000,
    mktime(dt.datetime.combine(summer_end, min_time).timetuple()) * 1000
])
xaxis = DatetimeAxis(formatter=xformatter, ticker=xticker)
plot.add_layout(xaxis, 'below')
yaxis = DatetimeAxis()
yaxis.formatter.hours = ['%H:%M']
plot.add_layout(yaxis, 'left')
legend = Legend(items=[
    LegendItem(label=value('sunset'), renderers=[sunset_line_renderer]),
    LegendItem(label=value('sunrise'), renderers=[sunrise_line_renderer]),
])
plot.add_layout(legend)
