import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

N_steps = 100; 
# number of steps
N_paths = 100;
# number of paths

with st.sidebar:
    st.title('随机行走模式')
    std = st.slider('标准差', 0.5, 2.0, 1.0, 0.1)
    mu = st.slider('均值',  -0.5, 0.5, 0.0, 0.1)

delta_t = 1

delta_X = np.random.normal(loc=0.0, 
                           scale=std*np.sqrt(delta_t), 
                           size=(N_steps,N_paths)) + mu * delta_t
t_n = np.linspace(0,N_steps,N_steps+1,endpoint = True)*delta_t

X = np.cumsum(delta_X, axis = 0); 
X_0 = np.zeros((1,N_paths))
X = np.vstack((X_0,X))

rows = 1
cols = 2

fig, ax = plt.subplots(figsize=(10,8))

num_layers = 3

num_lines = 10

for idx in range(num_layers):
    err_up = mu * t_n + (idx + 1)*std*np.sqrt(t_n)
    err_down = mu * t_n - (idx + 1)*std*np.sqrt(t_n)
    
    plt.fill_between(t_n, err_up, err_down, alpha=0.2, color='#008DF6', edgecolor = None)

ax.plot(t_n, X, lw=0.25,color = '#223C6C')
ax.plot(t_n, np.mean(X,axis = 1),color = 'r')
ax.set_xlim([0,N_steps])
ax.set_ylim(-80,80)
ax.set_yticks([])
ax.set_xticks([])
ax.axis('off')
st.pyplot(fig)