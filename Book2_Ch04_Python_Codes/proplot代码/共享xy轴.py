# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 15:15:11 2023

@author: james
"""

import proplot as pplt
import numpy as np
state = np.random.RandomState(51423)

# Plots with minimum and maximum sharing settings
# Note that all x and y axis limits and ticks are identical
spans = (False, True)
shares = (False, 'all')
titles = ('Minimum sharing', 'Maximum sharing')
for span, share, title in zip(spans, shares, titles):
    fig = pplt.figure(refwidth=1, span=span, share=share)
    axs = fig.subplots(nrows=4, ncols=4)
    for ax in axs:
        data = (state.rand(100, 20) - 0.4).cumsum(axis=0)
        ax.plot(data, cycle='Set3')
    axs.format(
        abc=True, abcloc='ul', suptitle=title,
        xlabel='xlabel', ylabel='ylabel',
        grid=False, xticks=25, yticks=5
    )