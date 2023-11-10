import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

with st.sidebar:
    st.title('三维Lp范数')
    p = st.slider('p', 1.0, 20.0, 1.0, 0.1)
    
x1 = np.linspace(-2.5, 2.5, num=21);
x2 = x1;
x3 = x1;

xxx1, xxx2, xxx3 = np.meshgrid(x1,x2,x3)

def Lp_norm(p):
    # 计算范数
    if np.isinf(p):
        zz = np.maximum(np.abs(xxx1),np.abs(xxx2),np.abs(xxx3))
    else:
        zz = ((np.abs((xxx1))**p) + 
              (np.abs((xxx2))**p) + 
              (np.abs((xxx3))**p))**(1./p)
        
    return zz


zzz = Lp_norm(p)
fig = go.Figure(data=go.Volume(
    x=xxx1.flatten(),
    y=xxx2.flatten(),
    z=xxx3.flatten(),
    value=zzz.flatten(),
    opacity=0.18, 
    surface_count=10,
    colorscale='RdYlBu'
    ))
fig.update_layout(autosize=False,
                  width=800, height=800,
                  margin=dict(l=65, r=50, b=65, t=90))



st.plotly_chart(fig)