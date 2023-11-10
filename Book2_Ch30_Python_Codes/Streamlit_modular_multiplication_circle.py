import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


with st.sidebar:
    st.title('模数乘法表，正圆')
    N = st.radio('分割数N', [180, 360, 720])
    k = st.slider('k', 2, N, 2, 1)

theta_array = np.linspace(0,2*np.pi,N+1)
x_array = np.cos(theta_array)
y_array = np.sin(theta_array)
points = np.column_stack((x_array,y_array))

def visualize(k = 2):
    # 可视化
    fig, ax = plt.subplots(figsize=(8,8))
    # 用hsv颜色映射一次渲染每一条弦
    colors = plt.cm.hsv(np.linspace(0, 1, N+1))
    
    # i 为弦第一个点的序号
    for i in range(N+1):
        
        # j 为弦第二个点的序号
        j = (i*k) % N
        
        # 绘制弦线段，两个点分别为
        # point[i], points[j]
        plt.plot([points[i,0], points[j,0]],
                 [points[i,1], points[j,1]],
                 lw = 0.1,c = colors[i])

    ax.axis('off')
    return fig

fig = visualize(k)
st.pyplot(fig)
