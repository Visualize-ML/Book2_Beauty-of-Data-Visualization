# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 16:32:32 2023

@author: james
"""

import proplot as plot
plot.rc.coastlinewidth = plot.rc.linewidth = 0.8

# Simple figure with just one projection
f, axs = plot.subplots(
    nrows=2, axwidth=2.5,
    proj='robin', proj_kw={'lon_0': 180}
)
axs.format(
    suptitle='Figure with single projection',
    coast=True, latlines=30, lonlines=60
)

#%%
# Complex figure with different projections
f, axs = plot.subplots(
    hratios=(1.5, 1, 1, 1, 1),
    basemap={
        (1, 3, 5, 7, 9): False,
        (2, 4, 6, 8, 10): True
    },
    proj={
        (1, 2): 'mill',
        (3, 4): 'cyl',
        (5, 6): 'moll',
        (7, 8): 'sinu',
        (9, 10): 'npstere'
    },
    ncols=2, nrows=5
)
axs.format(suptitle='Figure with several projections')
axs.format(coast=True, latlines=30, lonlines=60)
axs[:, 1].format(labels=True, lonlines=plot.arange(-180, 179, 60))
axs[-1, -1].format(labels=True, lonlines=30)
axs.format(collabels=['Cartopy projections', 'Basemap projections'])
plot.rc.reset()