# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 15:12:25 2023

@author: james
"""

import proplot as pplt
import numpy as np
fig, axs = pplt.subplots(ncols=2, nrows=2, refwidth=2, share=False)
state = np.random.RandomState(51423)
N = 60
x = np.linspace(1, 10, N)
y = (state.rand(N, 5) - 0.5).cumsum(axis=0)
axs[0].plot(x, y, linewidth=1.5)
axs.format(
    suptitle='Format command demo',
    abc='A.', abcloc='ul',
    title='Main', ltitle='Left', rtitle='Right',  # different titles
    ultitle='Title 1', urtitle='Title 2', lltitle='Title 3', lrtitle='Title 4',
    toplabels=('Column 1', 'Column 2'),
    leftlabels=('Row 1', 'Row 2'),
    xlabel='xaxis', ylabel='yaxis',
    xscale='log',
    xlim=(1, 10), xticks=1,
    ylim=(-3, 3), yticks=pplt.arange(-3, 3),
    yticklabels=('a', 'bb', 'c', 'dd', 'e', 'ff', 'g'),
    ytickloc='both', yticklabelloc='both',
    xtickdir='inout', xtickminor=False, ygridminor=True,
)

fig.save('对数坐标.svg')

