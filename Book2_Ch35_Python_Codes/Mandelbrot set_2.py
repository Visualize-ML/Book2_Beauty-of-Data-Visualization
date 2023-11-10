# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 18:01:29 2023

@author: james
"""
# https://carpentries-incubator.github.io/lesson-parallel-python/06b-exercise-fractals/index.html
from matplotlib import pyplot as plt
import numpy as np


width = 2**8
height = 2**8

center = -0.8+0.0j
extent = 3.0+3.0j

def Mandelbrot_set(max_iter):

    
    
    result = np.zeros((height, width), int)
    for j in range(height):
        for i in range(width):
            c = center + (i - width // 2 + (j - height // 2)*1j) * scale
            z = 0
            for k in range(max_iter):
                z = z**2 + c
                if (z * z.conjugate()).real > 4.0:
                    break
            result[j, i] = k
            
            
    return result
        

fig = plt.figure(figsize = (5,8))

for idx in range(6):
    
    scale = max((extent / width).real, (extent / height).imag)
    
    ax = plt.subplot(3,2,idx + 1)
    plot_extent = (width + 1j * height) * scale
    z1 = center - plot_extent / 2
    z2 = z1 + plot_extent
    max_iter = 2**(idx + 3)
    
    result = Mandelbrot_set(max_iter)
    ax.imshow(result**(1/3), origin='lower', extent=(z1.real, z2.real, z1.imag, z2.imag))
    ax.set_axis_off()

#%%

plt.savefig('Mandelbrot_set.svg', dpi=2000)    