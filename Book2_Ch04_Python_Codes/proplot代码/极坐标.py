# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 15:38:12 2023

@author: james
"""

import proplot as pplt
import numpy as np
N = 200
state = np.random.RandomState(51423)
x = np.linspace(0, 2 * np.pi, N)[:, None] + np.arange(5) * 2 * np.pi / 5
y = 100 * (state.rand(N, 5) - 0.3).cumsum(axis=0) / N
fig, axs = pplt.subplots([[1, 1, 2, 2], [0, 3, 3, 0]], proj='polar')
axs.format(
    suptitle='Polar axes demo', linewidth=1, titlepad='1em',
    ticklabelsize=9, rlines=0.5, rlim=(0, 19),
)
for ax in axs:
    ax.plot(x, y, cycle='FlatUI', zorder=0, lw=3)

# Standard polar plot
axs[0].format(
    title='Normal plot', thetaformatter='tau',
    rlabelpos=225, rlines=pplt.arange(5, 30, 5),
    edgecolor='red8', tickpad='1em',
)

# Sector plot
axs[1].format(
    title='Sector plot', thetadir=-1, thetalines=90, thetalim=(0, 270), theta0='N',
    rlim=(0, 22), rlines=pplt.arange(5, 30, 5),
)

# Annular plot
axs[2].format(
    title='Annular plot', thetadir=-1, thetalines=20, gridcolor='red',
    r0=-20, rlim=(0, 22), rformatter='null', rlocator=2
)