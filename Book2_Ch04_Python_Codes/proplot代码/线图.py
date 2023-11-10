# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 15:49:49 2023

@author: james
"""

import proplot as pplt
import numpy as np
state = np.random.RandomState(51423)
gs = pplt.GridSpec(nrows=3, ncols=2)
fig = pplt.figure(refwidth=2.2, span=False, share='labels')

# Vertical vs. horizontal
data = (state.rand(10, 5) - 0.5).cumsum(axis=0)
ax = fig.subplot(gs[0], title='Dependent x-axis')
ax.line(data, lw=2.5, cycle='seaborn')
ax = fig.subplot(gs[1], title='Dependent y-axis')
ax.linex(data, lw=2.5, cycle='seaborn')

# Vertical lines
gray = 'gray7'
data = state.rand(20) - 0.5
ax = fig.subplot(gs[2], title='Vertical lines')
ax.area(data, color=gray, alpha=0.2)
ax.vlines(data, negpos=True, lw=2)

# Horizontal lines
ax = fig.subplot(gs[3], title='Horizontal lines')
ax.areax(data, color=gray, alpha=0.2)
ax.hlines(data, negpos=True, lw=2)

# Step
ax = fig.subplot(gs[4], title='Step plot')
data = state.rand(20, 4).cumsum(axis=1).cumsum(axis=0)
cycle = ('gray6', 'blue7', 'red7', 'gray4')
ax.step(data, cycle=cycle, labels=list('ABCD'), legend='ul', legend_kw={'ncol': 2})

# Stems
ax = fig.subplot(gs[5], title='Stem plot')
data = state.rand(20)
ax.stem(data)
fig.format(suptitle='Line plots demo', xlabel='xlabel', ylabel='ylabel')