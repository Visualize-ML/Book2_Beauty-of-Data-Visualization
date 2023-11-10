# -*- coding: utf-8 -*-
"""
需要安装
pip install basemap

"""

import proplot as pplt

# Table of basemap projections
projs = [
    'cyl', 'merc', 'mill', 'cea', 'gall', 'sinu',
    'eck4', 'robin', 'moll', 'kav7', 'hammer', 'mbtfpq',
    'geos', 'ortho', 'nsper',
    'vandg', 'aea', 'eqdc', 'gnom', 'cass', 'lcc',
    'npstere', 'npaeqd', 'nplaea'
]
fig, axs = pplt.subplots(ncols=3, nrows=8, basemap=True, figwidth=7, proj=projs)
axs.format(
    land=True, labels=False,
    suptitle='Table of basemap projections'
)
for proj, ax in zip(projs, axs):
    ax.format(title=proj, titleweight='bold', labels=False)