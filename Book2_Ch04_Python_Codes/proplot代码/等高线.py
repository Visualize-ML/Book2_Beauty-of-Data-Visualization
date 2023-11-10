# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 15:58:26 2023

@author: james
"""

import proplot as pplt
import numpy as np

# Sample data
state = np.random.RandomState(51423)
data1 = (state.rand(20, 20) - 0.485).cumsum(axis=1).cumsum(axis=0)
data2 = (state.rand(20, 20) - 0.515).cumsum(axis=0).cumsum(axis=1)

# Figure
fig, axs = pplt.subplots(nrows=2, ncols=2, refwidth=2.2, order='F')
axs.format(suptitle='Diverging normalizer demo')
cmap = pplt.Colormap('RdYlBu', cut=0.1)

# Diverging norms
i = 0
for data, mode, fair in zip(
    (data1, data2), ('positive', 'negative'), ('fair', 'unfair'),
):
    for fair in ('fair', 'unfair'):
        norm = pplt.Norm('diverging', fair=(fair == 'fair'))
        ax = axs[i]
        m = ax.contourf(data, cmap=cmap, norm=norm)
        ax.colorbar(m, loc='b')
        ax.format(title=f'{mode.title()}-skewed + {fair} scaling')
        i += 1