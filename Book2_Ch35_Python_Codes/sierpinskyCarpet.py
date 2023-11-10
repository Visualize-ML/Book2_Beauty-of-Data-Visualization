"""
Reference: 
https://github.com/Quentin18/Matplotlib-fractals
"""
import sys
import numpy as np
import matplotlib.pyplot as plt


def sierpinskiCarpet(n):
    n += 1
    T = np.ones((3**n, 3**n))
    a = n
    start = 1
    step = 3
    size = 1
    while a > 0:
        for i in range(start, 3**n, step):
            for j in range(start, 3**n, step):
                for k in range(size):
                    for l in range(size):
                        T[i + k, j + l] = 0
        a -= 1
        start *= 3
        step *= 3
        size *= 3
    
    return T


fig = plt.figure(figsize = (5,8))

for idx in range(6):

    ax = plt.subplot(3,2,idx + 1)
    T = sierpinskiCarpet(idx)
    
    ax.pcolormesh(T, cmap='Blues_r', rasterized = True)
    ax.set_axis_off()
    
    #%%
    
plt.savefig('sierpinskiCarpet_higher_res.png', dpi=2000)    