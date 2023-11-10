# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 15:55:27 2023

@author: james
"""

import proplot as pplt
import numpy as np

# Sample data
N = 20
state = np.random.RandomState(51423)
data = 11 ** (0.25 * np.cumsum(state.rand(N, N), axis=0))

# Create figure
gs = pplt.GridSpec(nrows=2)
fig = pplt.figure(refwidth=2.3, span=False, suptitle='Normalizer types')

# Different normalizers
ax = fig.subplot(gs[0], title='Default linear normalizer')
ax.pcolormesh(data, cmap='magma', colorbar='b')
ax = fig.subplot(gs[1], title="Logarithmic normalizer with norm='log'")
ax.pcolormesh(data, cmap='magma', norm='log', colorbar='b')