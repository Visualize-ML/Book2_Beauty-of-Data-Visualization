# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 15:46:01 2023

@author: james
"""

import proplot as pplt
import numpy as np
state = np.random.RandomState(51423)
data = (state.rand(20, 20) - 0.48).cumsum(axis=1).cumsum(axis=0)
data = 10 * (data - data.min()) / (data.max() - data.min())

# Stacked panels with outer colorbars
for cbarloc, ploc in ('rb', 'br'):
    # Create figure
    fig, axs = pplt.subplots(
        nrows=2, ncols=1, refwidth=1.8, panelpad=0.8,
        share=False, includepanels=True
    )
    axs.format(
        xlabel='xlabel', ylabel='ylabel', title='Title',
        suptitle='Using panels for summary statistics',
    )

    # Plot 2D dataset
    for ax in axs:
        ax.contourf(
            data, cmap='glacial', extend='both',
            colorbar=cbarloc, colorbar_kw={'label': 'colorbar'},
        )

    # Get summary statistics and settings
    axis = int(ploc == 'r')  # dimension along which stats are taken
    x1 = x2 = np.arange(20)
    y1 = data.mean(axis=axis)
    y2 = data.std(axis=axis)
    titleloc = 'upper center'
    if ploc == 'r':
        titleloc = 'center'
        x1, x2, y1, y2 = y1, y2, x1, x2

    # Panels for plotting the mean. Note SubplotGrid.panel() returns a SubplotGrid
    # of panel axes. We use this to call format() for all the panels at once.
    space = 0
    width = '4em'
    kwargs = {'titleloc': titleloc, 'xreverse': False, 'yreverse': False}
    pxs = axs.panel(ploc, space=space, width=width)
    pxs.format(title='Mean', **kwargs)
    for px in pxs:
        px.plot(x1, y1, color='gray7')

    # Panels for plotting the standard deviation
    pxs = axs.panel(ploc, space=space, width=width)
    pxs.format(title='Stdev', **kwargs)
    for px in pxs:
        px.plot(x2, y2, color='gray7', ls='--')