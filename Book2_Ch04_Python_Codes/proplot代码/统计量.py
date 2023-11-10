# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 16:01:46 2023

@author: james
"""
import proplot as pplt
import numpy as np

# Sample data
N = 500
state = np.random.RandomState(51423)
x = state.normal(size=(N,))
y = state.normal(size=(N,))
bins = pplt.arange(-3, 3, 0.25)

# Histogram with marginal distributions
fig, axs = pplt.subplots(nrows=2, refwidth=2.3)
axs.format(
    abc='A.', abcloc='l', titleabove=True,
    ylabel='y axis', suptitle='Histograms with marginal distributions'
)
colors = ('indigo9', 'red9')
titles = ('Group 1', 'Group 2')
for ax, which, color, title in zip(axs, 'lr', colors, titles):
    ax.hist2d(
        x, y, bins, vmin=0, vmax=10, levels=50,
        cmap=color, colorbar='b', colorbar_kw={'label': 'count'}
    )
    color = pplt.scale_luminance(color, 1.5)  # histogram colors
    px = ax.panel(which, space=0)
    px.histh(y, bins, color=color, fill=True, ec='k')
    px.format(grid=False, xlocator=[], xreverse=(which == 'l'))
    px = ax.panel('t', space=0)
    px.hist(x, bins, color=color, fill=True, ec='k')
    px.format(grid=False, ylocator=[], title=title, titleloc='l')