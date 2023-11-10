import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

with st.sidebar:
    st.title('平面Lp范数')
    p = st.slider('p', 1.0, 20.0, 1.0, 0.1)
    
x1 = np.linspace(-2.5, 2.5, num=101);
x2 = x1;

xx1, xx2 = np.meshgrid(x1,x2)

def Lp_norm(p):
    # 计算范数
    if np.isinf(p):
        zz = np.maximum(np.abs(xx1),np.abs(xx2))
    else:
        zz = ((np.abs((xx1))**p) + (np.abs((xx2))**p))**(1./p)
        
    return zz

fig, ax = plt.subplots(figsize=(6, 6))


zz = Lp_norm(p)

# 绘制等高线
ax.contourf(xx1, xx2, zz, 20, cmap='RdYlBu_r')

# 绘制Lp norm = 1的等高线
ax.contour (xx1, xx2, zz, [1], colors='k', linewidths = 2) 

# 装饰
ax.axhline(y=0, color='k', linewidth = 0.25)
ax.axvline(x=0, color='k', linewidth = 0.25)
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])
# ax.set_xlabel('$x_1$')
# ax.set_ylabel('$x_2$')
ax.set_title('p = ' + str(p))
ax.set_aspect('equal', adjustable='box')

st.pyplot(fig)