# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 15:50:26 2023

@author: james
"""

import proplot as pplt
import numpy as np
import pandas as pd

# Sample data
state = np.random.RandomState(51423)
x = (state.rand(20) - 0).cumsum()
data = (state.rand(20, 4) - 0.5).cumsum(axis=0)
data = pd.DataFrame(data, columns=pd.Index(['a', 'b', 'c', 'd'], name='label'))

# Figure
gs = pplt.GridSpec(ncols=2, nrows=2)
fig = pplt.figure(refwidth=2.2, share='labels', span=False)

# Vertical vs. horizontal
ax = fig.subplot(gs[0], title='Dependent x-axis')
ax.scatter(data, cycle='538')
ax = fig.subplot(gs[1], title='Dependent y-axis')
ax.scatterx(data, cycle='538')

# Scatter plot with property cycler
ax = fig.subplot(gs[2], title='With property cycle')
obj = ax.scatter(
    x, data, legend='ul', legend_kw={'ncols': 2},
    cycle='Set2', cycle_kw={'m': ['x', 'o', 'x', 'o'], 'ms': [5, 10, 20, 30]}
)

# Scatter plot with colormap
ax = fig.subplot(gs[3], title='With colormap')
data = state.rand(2, 100)
obj = ax.scatter(
    *data,
    s=state.rand(100), smin=6, smax=60, marker='o',
    c=data.sum(axis=0), cmap='maroon',
    colorbar='lr', colorbar_kw={'label': 'label'},
)
fig.format(suptitle='Scatter plot demo', xlabel='xlabel', ylabel='ylabel')