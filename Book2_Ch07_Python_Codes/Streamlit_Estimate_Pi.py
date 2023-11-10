import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

p = plt.rcParams
p["font.sans-serif"] = ["Roboto"]
p["font.weight"] = "light"
p["ytick.minor.visible"] = False
p["xtick.minor.visible"] = False
p["axes.grid"] = True
p["grid.color"] = "0.5"
p["grid.linewidth"] = 0.5

with st.sidebar:
    st.title('估算圆周率')
    num = st.slider('散点数',200, 5000, 200, 200)
# 二元，服从连续均匀分布

# 2000 个散点
X = np.random.uniform(low=-1, high=1, size=(num,2))

# 生成面具
mask_inside = (X[:,0]**2 + X[:,1]**2 <= 1)
fig, ax = plt.subplots()

X_inside  = X[mask_inside,:]  # 单位圆内 (包括圆上) 的点
X_outside = X[~mask_inside,:] # 单位圆外部的点

colors = np.array(['#377eb8', '#ff7f00'])

circ = plt.Circle((0, 0), radius=1, edgecolor='k', facecolor='None')
ax.add_patch(circ)
plt.scatter(X_inside[:,0],  X_inside[:,1],  color = colors[0], marker = '.')
plt.scatter(X_outside[:,0], X_outside[:,1], color = colors[1], marker = 'x')

ax.set_aspect('equal', adjustable='box')
plt.xticks(np.linspace(-1,1,11))
plt.yticks(np.linspace(-1,1,11))
plt.xlim(-1, 1)
plt.ylim(-1, 1)


st.write('Number of points inside = ' + str(mask_inside.sum()))
st.write('Percentage of points inside = ' + str(mask_inside.sum()/num*100) + '%')
estimated_pi = mask_inside.sum()/num*4
st.write('Estimated pi = ' + str(np.round(estimated_pi,5)))
st.pyplot(fig)
