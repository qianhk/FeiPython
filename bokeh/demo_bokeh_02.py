#!/usr/bin/env python3
# coding=utf-8

import numpy as np
import os

import bokeh
import bokeh.models as models
from bokeh.plotting import figure, output_file, show

# x = [0.1, 0.5, 1.0, 1.5, 2.0, 3, 3.5, 4, 5, 6, 7, 8, 9]
# y = [10 ** xx for xx in x]
x = range(0, 100)
y = [5 * xx for xx in x]
# 创建数据

p = figure(plot_width=400, plot_height=400,
           # y_axis_type="log",
           tools='pan, wheel_zoom, reset, hover, crosshair, tap')  # 如果不设置y_axis_type = "log"就是一个对数的展示；
# p.xaxis.ticker = models.SingleIntervalTicker(interval=5)
# p.yaxis.formatter = models.NumeralTickFormatter(format='0.0a')  # 数据位数
p.axis.major_tick_in = -30
p.axis.major_tick_out = 60
upper = models.Span(location=100, dimension='width', line_color='red', line_width=4)
p.add_layout(upper)
lower = models.Span(location=200, dimension='width', line_color='green', line_width=4)
p.add_layout(lower)
p.line(x, y, line_width=2)
p.circle(x, y, fill_color="white", size=8, hover_color='red')

show(p)
