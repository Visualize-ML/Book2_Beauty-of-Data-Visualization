# -*- coding: utf-8 -*-
"""
需要安装
conda install -c conda-forge proj-data
"""

import proplot as pplt

# Table of cartopy projections
projs = [
    'cyl', 'merc', 'mill', 'lcyl', 'tmerc',
    'robin', 'hammer', 'moll', 'kav7', 'aitoff', 'wintri', 'sinu',
    'geos', 'ortho', 'nsper', 'aea', 'eqdc', 'lcc', 'gnom',
    'npstere', 'nplaea', 'npaeqd', 'npgnom', 'igh',
    'eck1', 'eck2', 'eck3', 'eck4', 'eck5', 'eck6'
]
fig, axs = pplt.subplots(ncols=3, nrows=10, figwidth=7, proj=projs)
axs.format(
    land=True, reso='lo', labels=False,
    suptitle='Table of cartopy projections'
)
for proj, ax in zip(projs, axs):
    ax.format(title=proj, titleweight='bold', labels=False)
    
    