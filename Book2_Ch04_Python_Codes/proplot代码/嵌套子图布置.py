# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 15:41:00 2023

@author: james
"""

import proplot as pplt

# Demonstrate that complex arrangements preserve
# spacing, aspect ratios, and axis sharing
gs = pplt.GridSpec(nrows=2, ncols=2)
fig = pplt.figure(refwidth=1.5, share=False)
for ss, side in zip(gs, 'tlbr'):
    ax = fig.add_subplot(ss)
    px = ax.panel_axes(side, width='3em')
fig.format(
    xlim=(0, 1), ylim=(0, 1),
    xlabel='xlabel', ylabel='ylabel',
    xticks=0.2, yticks=0.2,
    title='Title', suptitle='Complex arrangement of panels',
    toplabels=('Column 1', 'Column 2'),
    abc=True, abcloc='ul', titleloc='uc', titleabove=False,
)