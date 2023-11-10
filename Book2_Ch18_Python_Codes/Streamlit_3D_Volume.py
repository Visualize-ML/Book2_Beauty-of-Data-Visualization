import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import cm
import plotly.graph_objects as go
import streamlit as st
# 导入色谱模块

p = plt.rcParams
p["font.sans-serif"] = ["Roboto"]
p["font.weight"] = "light"
p["ytick.minor.visible"] = False
p["xtick.minor.visible"] = False
p["axes.grid"] = True
p["grid.color"] = "0.5"
p["grid.linewidth"] = 0.5

def bmatrix(a):
    """Returns a LaTeX bmatrix

    :a: numpy array
    :returns: LaTeX bmatrix as a string
    """
    if len(a.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')
    lines = str(a).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{bmatrix}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv +=  [r'\end{bmatrix}']
    return '\n'.join(rv)

with st.sidebar:
    st.title('体积图')
    st.latex(r'''Q = \begin{bmatrix}
    a & b & c\\
    b & d & e\\
    c & e & f
    \end{bmatrix}''' )   
    
    a = st.slider('a', -5,5,1,1)
    b = st.slider('b', -5,5,0,1)
    c = st.slider('c', -5,5,0,1)
    d = st.slider('d', -5,5,2,1)
    e = st.slider('e', -5,5,0,1)
    f = st.slider('f', -5,5,3,1)

x = np.linspace(-2,2,21)
y = np.linspace(-2,2,21)
z = np.linspace(-2,2,21)

X, Y, Z = np.meshgrid(x,y,z)

Points = np.column_stack([X.ravel(), Y.ravel(), Z.ravel()])

Q = np.array([[a,b,c],
              [b,d,e],
              [c,e,f]])


st.latex('Q =' + bmatrix(Q))
fff = np.diag(Points @ Q @ Points.T)
# fff = np.reshape(fff,X.shape)


fig = go.Figure(data=go.Volume(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=fff.flatten(),
    opacity=0.18, 
    surface_count=11,
    colorscale='RdYlBu'
    ))
fig.update_layout(autosize=False,
                  width=800, height=800,
                  margin=dict(l=65, r=50, b=65, t=90))



st.plotly_chart(fig)
