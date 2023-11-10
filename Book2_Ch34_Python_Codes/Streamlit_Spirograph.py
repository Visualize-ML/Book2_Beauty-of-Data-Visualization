import matplotlib.pyplot as plt
import numpy as np
from math import lcm
from matplotlib.collections import LineCollection
import streamlit as st

def draw_spirograph(R, r, d, Ratio = 1):
    
    num = lcm(R,r)/R

    theta = np.linspace(0,num*2*np.pi*Ratio, 10000)
    colors = np.arange(0, 1, 1/len(theta))
    x = (R-r) * np.cos(theta) + d * np.cos((R-r)/r * theta)
    y = (R-r) * np.sin(theta) - d * np.sin((R-r)/r * theta)
    dist = np.sqrt(x**2 + y**2)
    
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    norm = plt.Normalize(theta.min(), theta.max())
        
    lc = LineCollection(segments, cmap='hsv', norm=norm)
    # Set the values used for colormapping
    lc.set_array(theta)
    lc.set_linewidth(0.25)
    
    fig, ax = plt.subplots(figsize = (3,3))
    ax.add_collection(lc)
    plt.axis('equal')
    plt.axis('off')
    plt.show()
    return fig

with st.sidebar:
    st.title('繁花曲线')
    R = st.slider('R', 2, 100, 2, 1)
    r = st.slider('r', 1, R, 1, 1)
    d = st.slider('d', 0.0, float(r), 0.0, 0.1)
    Ratio = st.slider('Ratio', 0.1, 1.0, 1.0, 0.05)
    
fig = draw_spirograph(R, r, d, Ratio)
st.pyplot(fig)