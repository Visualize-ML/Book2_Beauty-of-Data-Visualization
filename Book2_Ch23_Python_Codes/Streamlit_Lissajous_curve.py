
import time
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from math import gcd

with st.sidebar:
    st.title('利萨茹曲线')
    nx = st.slider('nx', 1, 10, 1, 1)
    ny = st.slider('ny', 1, 10, 1, 1)
    k  = st.slider('k', 1, 10, 1, 1)


t = np.linspace(0, 1/gcd(nx,ny), 1000)


x_traj = np.cos(2*np.pi*nx*t)
y_traj = np.cos(2*np.pi*ny*t + k*np.pi/4/nx)

points = np.array([x_traj, y_traj]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

norm = plt.Normalize(t.min(), t.max())
    
lc = LineCollection(segments, cmap='hsv', norm=norm)
# Set the values used for colormapping
lc.set_array(t)
lc.set_linewidth(2)

fig, ax = plt.subplots(figsize = (3,3))
ax.add_collection(lc)
plt.axis('equal')
plt.axis('off')
plt.show()
st.pyplot(fig)