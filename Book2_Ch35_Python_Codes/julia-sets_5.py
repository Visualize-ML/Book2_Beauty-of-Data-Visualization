
# 参考：
# https://mathworld.wolfram.com/JuliaSet.html

import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
 
# m = 480
# n = 320

m = 2**11
n = m
iterations = 2**8
s = m * 0.8


def julia_set(iterations, c):
    
    c = np.full((n, m), c)
    x = np.linspace(-m / s, m / s, num=m).reshape((1, m))
    y = np.linspace(-n / s, n / s, num=n).reshape((n, 1))
    Z = np.tile(x, (n, 1)) + 1j * np.tile(y, (1, m))
    M = np.full((n, m), True, dtype=bool)
    N = np.zeros((n, m))
    
    
    for i in range(iterations):
        Z[M] = Z[M] * Z[M] + c[M]
        M[np.abs(Z) > 2] = False
        N[M] = i
    
    return np.flipud(N)
 


#%%

c = 0.285 + 0.01 * 1j
N = julia_set(iterations, c)

fig, ax = plt.subplots(figsize = (10,10))

ax.imshow(N, cmap='RdYlBu_r')
ax.set_axis_off()

#%%

c = -0.4 + 0.6j
N = julia_set(iterations, c)

fig, ax = plt.subplots(figsize = (10,10))

ax.imshow(N, cmap='RdYlBu_r')
ax.set_axis_off()

#%%
c = -0.70176 - 0.3842 * 1j

N = julia_set(iterations, c)

fig, ax = plt.subplots(figsize = (10,10))

ax.imshow(N, cmap='RdYlBu_r')
ax.set_axis_off()

#%%
c = -0.7269 - 0.1889 * 1j

N = julia_set(iterations, c)

fig, ax = plt.subplots(figsize = (10,10))

ax.imshow(N, cmap='RdYlBu_r')
ax.set_axis_off()


#%%
c = -0.835 - 0.2321 * 1j

N = julia_set(iterations, c)

fig, ax = plt.subplots(figsize = (10,10))

ax.imshow(N, cmap='RdYlBu_r')
ax.set_axis_off()

#%%
for theta_i in np.linspace(0, np.pi, 7):
    c = 0.7885 * np.exp(1j * theta_i)
    
    
    N = julia_set(iterations, c)

    fig, ax = plt.subplots(figsize = (10,10))

    ax.imshow(N, cmap='RdYlBu_r')
    ax.set_axis_off()
    
    
    
    
    