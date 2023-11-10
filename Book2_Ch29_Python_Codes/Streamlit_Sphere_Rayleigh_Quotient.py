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
    st.title('三元瑞利商')
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

# 设置步数
intervals = 50
ntheta = intervals
nphi = 2*intervals

# 单位球，球坐标
# theta取值范围为 [0, pi]
theta = np.linspace(0, np.pi*1, ntheta+1)
# phi取值范围为 [0, 2*pi]
phi   = np.linspace(0, np.pi*2, nphi+1)

# 单位球半径
r = 1 

# 球坐标转化为三维直角坐标 
pp_,tt_ = np.meshgrid(phi,theta)

# z轴坐标网格数据
Z = r*np.cos(tt_)

# x轴坐标网格数据
X = r*np.sin(tt_)*np.cos(pp_)

# y轴坐标网格数据
Y = r*np.sin(tt_)*np.sin(pp_)


# 每一行代表一个三维直角坐标系坐标点
# 所有坐标点都在单位球面上
Points = np.column_stack([X.ravel(), Y.ravel(), Z.ravel()])

Q = np.array([[a,b,c],
              [b,d,e],
              [c,e,f]])


st.latex('Q =' + bmatrix(Q))
Rayleigh_Q = np.diag(Points @ Q @ Points.T)
Rayleigh_Q_ = np.reshape(Rayleigh_Q,X.shape)
fig = go.Figure(data=[go.Surface(x=X, y=Y, z=Z, 
                                 surfacecolor=Rayleigh_Q_, 
                                 # cmax = 3,cmin = -3,
                                 colorscale='RdYlBu_r')])
   
fig.update_layout(
autosize=False,
width =800,
height=600,
margin=dict(l=65, r=50, b=65, t=90))
fig.layout.scene.camera.projection.type = "orthographic"

st.plotly_chart(fig)
