# 导入包
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.collections import LineCollection
import streamlit as st

def colorline(x, y, cmap):
    
    norm=plt.Normalize(0.0, 1.0)
    # 归一化函数，将数据线性归一化在 [0, 1] 区间
    segments = make_segments(x, y)
    # make_segments 自定义函数，将一条线打散成一系列线段
    
    lc = LineCollection(segments, array = np.linspace(0.0, 1.0, len(x)),
                              cmap=cmap, norm=norm,
                              linewidth=1, alpha=1)
    # LineCollection 可以看成是一系列线段的集合
    # 可以用色谱分别渲染每一条线段
    # 这样可以得到颜色连续变化的效果
    

    ax = plt.gca()
    ax.add_collection(lc)

    return lc

def make_segments(x, y):
    
    # 将一条线打散成一系列线段

    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    return segments

with st.sidebar:
    st.title('平面随机行走')
    seed_num = st.slider('随机数种子', 0, 100, 0, 1)

np.random.seed(seed_num)
N_steps = 10000; 
# 随机轨迹的步数

delta_x = np.random.normal(loc=0.0, scale=1.0, size=(N_steps,1))
delta_y = np.random.normal(loc=0.0, scale=1.0, size=(N_steps,1))
# 生成满足正态分布的随机数
 
disp_x = np.cumsum(delta_x, axis = 0); 
disp_y = np.cumsum(delta_y, axis = 0); 
# 用累加生成平面轨迹

disp_x = np.vstack(([0],disp_x))
disp_y = np.vstack(([0],disp_y))
# 给轨迹添加起点 (0, 0)

fig, ax = plt.subplots(figsize = (6,6))
# plt.style.use('dark_background')

colorline(disp_x, disp_y, cmap='hsv')
# 调用自定义函数 colorline

plt.plot(disp_x[0],disp_y[0],'wx', markersize = 12)
plt.plot(disp_x[-1],disp_y[-1],'wx', markersize = 12)
# 绘制起点、终点

plt.xticks([])
plt.yticks([])
plt.axis('off')

st.pyplot(fig)