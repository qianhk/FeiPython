#!/usr/bin/env python3
# coding=utf-8

import numpy as np
import os

import bokeh
import bokeh.models
from bokeh.plotting import figure, output_file, show, output_notebook
from bokeh.sampledata.stocks import AAPL

# bokeh sample data directory does not exist, please execute bokeh.sampledata.download()
# python3 -c "import bokeh.sampledata; bokeh.sampledata.download()"


# 准备数据
aapl = np.array(AAPL['adj_close'])
aapl_dates = np.array(AAPL['date'], dtype=np.datetime64)

window_size = 30
window = np.ones(window_size) / float(window_size)
aapl_avg = np.convolve(aapl, window, 'same')

# 在notbook中展示
# output_notebook()
# print(f'lookKai filename: {__name__}')
output_file(os.path.expanduser('~/Downloads/demo_bokeh_01.html'))

# 创建新图表
hover = bokeh.models.HoverTool(tooltips=[("x", "@x")], mode="vline")
# 设值数据选取方式
# p = figure(plot_width=800, plot_height=350, x_axis_type="datetime")
p = figure(plot_width=800, plot_height=350, x_axis_type="datetime", tools='pan, crosshair, box_zoom, reset')
p.tools.append(hover)

# 添加图表渲染
data_dic = {'x': aapl_dates, 'y1': aapl, 'y2': aapl_avg}
source = bokeh.models.ColumnDataSource(data_dic)
# p.circle(aapl_dates, aapl, size=4, color='darkgrey', alpha=0.2, legend_field='close')
# p.line(aapl_dates, aapl_avg, color='navy', legend_label='avg')
p.circle('x', 'y1', size=4, color='darkgrey', alpha=0.2, legend_field='close', source=source, hover_color='red')
p.line('x', 'y2', color='navy', legend_label='avg', source=source)

# 设置图表元素
p.title.text = "AAPL One-Month Average"
p.legend.location = "top_left"
p.grid.grid_line_alpha = 0
p.xaxis.axis_label = 'Date'
p.yaxis.axis_label = 'Price'
p.ygrid.band_fill_color = "green"
p.ygrid.band_fill_alpha = 0.2
p.xgrid.band_fill_color = 'blue'
p.xgrid.band_fill_alpha = 0.2

# 设置下拉选项进行性别的选择
# gender = Select(title='Gender', value='male', options=['female', 'male'])
# gender.on_change('value', update)
# # 设置下拉选项进行颜色区分的选择
# color = Select(title='Color', value='region', options=['region', 'smoker', 'children'])
# color.on_change('value', update)
# controls = widgetbox([gender, color], width=200)  # 将小部件放在一起

# 显示图表
show(p)
