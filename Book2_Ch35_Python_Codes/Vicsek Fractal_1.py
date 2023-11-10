# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 17:58:59 2023

@author: james
"""

import matplotlib.pyplot as plt

def draw_fractal(ax, levels=4, x=0, y=0, size=1):
    if levels == 0:
        ax.add_patch(plt.Rectangle((x, y), size, size, color='navy'))
    else:
        size3 = size / 3
        for i in range(3):
            for j in range(3):
                if (i + j) % 2 == 0:
                    draw_fractal(ax, levels - 1, x + i * size3, y + j * size3, size3)


fig = plt.figure(figsize = (5,8))

for idx in range(6):

    ax = plt.subplot(3,2,idx + 1)
    draw_fractal(ax, idx)
    ax.set_axis_off()
    