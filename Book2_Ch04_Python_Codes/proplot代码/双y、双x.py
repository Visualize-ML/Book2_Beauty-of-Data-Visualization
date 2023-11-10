# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 15:27:03 2023

@author: james
"""

import proplot as pplt
import numpy as np
state = np.random.RandomState(51423)
c0 = 'gray5'
c1 = 'red8'
c2 = 'blue8'
N, M = 50, 10

# Alternate y axis
data = state.rand(M) + (state.rand(N, M) - 0.48).cumsum(axis=0)
altdata = 5 * (state.rand(N) - 0.45).cumsum(axis=0)
fig = pplt.figure(share=False)
ax = fig.subplot(211, title='Alternate y twin x')
ax.line(data, color=c0, ls='--')
ox = ax.alty(color=c2, label='alternate ylabel', linewidth=1)
ox.line(altdata, color=c2)

# Alternate x axis
data = state.rand(M) + (state.rand(N, M) - 0.48).cumsum(axis=0)
altdata = 5 * (state.rand(N) - 0.45).cumsum(axis=0)
ax = fig.subplot(212, title='Alternate x twin y')
ax.linex(data, color=c0, ls='--')
ox = ax.altx(color=c1, label='alternate xlabel', linewidth=1)
ox.linex(altdata, color=c1)
fig.format(xlabel='xlabel', ylabel='ylabel', suptitle='Alternate axes demo')