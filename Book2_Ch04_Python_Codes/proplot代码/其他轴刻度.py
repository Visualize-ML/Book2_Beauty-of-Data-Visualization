# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 15:17:58 2023

@author: james
"""

import proplot as pplt
import numpy as np

# Create figure
n = 30
state = np.random.RandomState(51423)
data = state.rand(n - 1, n - 1)
colors = ('coral', 'sky blue')
cmap = pplt.Colormap('grays', right=0.8)
gs = pplt.GridSpec(nrows=2, ncols=2)
fig = pplt.figure(refwidth=2.3, share=False)
fig.format(grid=False, suptitle='Other axis scales demo')

# Geographic scales
x = np.linspace(-180, 180, n)
y = np.linspace(-85, 85, n)
for i, scale in enumerate(('sine', 'mercator')):
    ax = fig.subplot(gs[i, 0])
    ax.plot(x, y, '-', color=colors[i], lw=4)
    ax.pcolormesh(x, y, data, cmap='grays', cmap_kw={'right': 0.8})
    ax.format(
        yscale=scale, title=scale.title() + ' scale',
        ylim=(-85, 85), ylocator=20, yformatter='deg',
    )

# Exponential scale
n = 50
x = np.linspace(0, 1, n)
y = 3 * np.linspace(0, 1, n)
data = state.rand(len(y) - 1, len(x) - 1)
ax = fig.subplot(gs[0, 1])
title = 'Exponential $e^x$ scale'
ax.pcolormesh(x, y, data, cmap='grays', cmap_kw={'right': 0.8})
ax.plot(x, y, lw=4, color=colors[0])
ax.format(ymin=0.05, yscale=('exp', np.e), title=title)

# Power scale
ax = fig.subplot(gs[1, 1])
title = 'Power $x^{0.5}$ scale'
ax.pcolormesh(x, y, data, cmap='grays', cmap_kw={'right': 0.8})
ax.plot(x, y, lw=4, color=colors[1])
ax.format(ymin=0.05, yscale=('power', 0.5), title=title)