# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 16:07:05 2023

@author: james
"""

import proplot as pplt
import numpy as np
import pandas as pd

# Sample data
N = 500
state = np.random.RandomState(51423)
data1 = state.normal(size=(N, 5)) + 2 * (state.rand(N, 5) - 0.5) * np.arange(5)
data1 = pd.DataFrame(data1, columns=pd.Index(list('abcde'), name='label'))
data2 = state.rand(100, 7)
data2 = pd.DataFrame(data2, columns=pd.Index(list('abcdefg'), name='label'))

# Figure
fig, axs = pplt.subplots(nrows=3)
axs.format(
    abc='A.', titleloc='l', grid=False,
    suptitle='Boxes and violins demo'
)

# Box plots
ax = axs[0]
obj1 = ax.box(data1, means=True, marker='x', meancolor='r', fillcolor='gray4')
ax.format(title='Box plots')

# Violin plots
ax = axs[1]
obj2 = ax.violin(data1, fillcolor='gray6', means=True, points=100)
ax.format(title='Violin plots')

# Boxes with different colors
ax = axs[2]
ax.box(data2, cycle='pastel2')
ax.format(title='Multiple colors', ymargin=0.15)