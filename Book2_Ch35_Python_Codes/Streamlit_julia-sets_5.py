
# 参考：
# https://mathworld.wolfram.com/JuliaSet.html

import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
import streamlit as st

# m = 480
# n = 320

m = 2**9
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
 

with st.sidebar:
    st.title('朱利亚集合')
    theta = st.slider('角度', 0.0,2*np.pi,0.0,0.01)


c = 0.7885 * np.exp(1j * theta)


N = julia_set(iterations, c)

fig, ax = plt.subplots(figsize = (5,5))

ax.imshow(N, cmap='RdYlBu_r')
ax.set_aspect('equal', adjustable='box')
ax.set_axis_off()
st.pyplot(fig)
    
    