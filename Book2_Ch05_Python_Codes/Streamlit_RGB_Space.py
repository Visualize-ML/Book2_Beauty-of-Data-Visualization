import plotly.graph_objects as go
import numpy as np
import streamlit as st

with st.sidebar:
    st.title('RGB色彩空间')
    num = st.slider('颗粒度', 5, 15, 8, 1)
    

Red   = np.linspace(0,255,num)
Green = np.linspace(0,255,num)
Blue  = np.linspace(0,255,num)

RRR,GGG,BBB = np.meshgrid(Red, Green, Blue)
colors_rgb = np.column_stack((RRR.ravel(),
                              GGG.ravel(),
                              BBB.ravel()))


# 提取 R、G、B 值
r_values, g_values, b_values = zip(*colors_rgb)

# 创建 3D 散点图
fig = go.Figure()

fig.add_trace(go.Scatter3d(
    x=r_values,
    y=g_values,
    z=b_values,
    mode='markers',
    marker=dict(
        color=colors_rgb,
        size=6,
    )
))

# 设置布局
fig.update_layout(
    scene=dict(
        xaxis=dict(title='Red'),
        yaxis=dict(title='Green'),
        zaxis=dict(title='Blue')),
    margin=dict(l=0, r=0, b=0, t=0))
fig.layout.scene.camera.projection.type = "orthographic"
st.plotly_chart(fig)