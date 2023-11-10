import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


def lerp(P_a, P_b, t_array):
    
    P_out = [P_a * (1 - t_idx) + P_b * t_idx for t_idx in t_array]
    P_out = np.array(P_out)
    
    return P_out

def lerp_2nd(P_a_array, P_b_array, t_array):
    
    t_array = t_array.reshape(-1,1)
    P_out = P_a_array * (1 - t_array) + P_b_array * t_array
    
    return P_out

def Bezier_2nd(P_0, P_1, P_2, t_array):
    B_array = lerp_2nd(lerp(P_0, P_1, t_array), lerp(P_1, P_2, t_array), t_array)
    
    # B_array = [(1 - t_idx)**2 * P_2 + 
    #            2 * (1 - t_idx) * t_idx * P_1 + 
    #            t_idx**2 * P_0 for t_idx in t_array]
    # B_array = np.array(B_array_fine)
    
    return B_array


with st.sidebar:
    st.title('二阶贝塞尔曲线原理')
    P_x = st.slider('横坐标',-10,10,4,1)
    P_y = st.slider('纵坐标',-10,10,4,1)

P_0 = np.array([-4, 4])
P_1 = np.array([P_x, P_y]) 
P_2 = np.array([4, -4])

delta_t = 1/16
t_array = np.linspace(delta_t,1,int(1/delta_t - 1), endpoint = False)
t_array_fine = np.linspace(0, 1, 101, endpoint = True)

P_0_1 = lerp(P_0, P_1, t_array)
P_1_2 = lerp(P_1, P_2, t_array)

B_array = lerp_2nd(P_0_1, P_1_2, t_array)
B_array_fine = Bezier_2nd(P_0, P_1, P_2, t_array_fine)


fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

num = len(P_0_1)
colors = plt.cm.rainbow(np.linspace(0,1,num, endpoint = True))

plt.plot([P_0[0],P_1[0]],
         [P_0[1],P_1[1]],
         color = 'k', 
         marker = 'x', ms = 20, lw = 0.5)

plt.plot([P_1[0],P_2[0]],
         [P_1[1],P_2[1]],
         color = 'k', 
         marker = 'x', ms = 20, lw = 0.5)

for i in range(num):
    plt.plot([P_0_1[i, 0], P_1_2[i, 0]], 
             [P_0_1[i, 1], P_1_2[i, 1]], 
             color=colors[i], 
             marker = '.', ms = 10, lw = 0.25)
    
    plt.plot(B_array[i,0],B_array[i,1], 
             marker = 'x', c = colors[i], 
             ms = 10, zorder = 1e5)


plt.plot(B_array_fine[:,0],B_array_fine[:,1],c = 'k', lw = 2)
# plt.plot(([i for (i,j) in P_0_1], [i for (i,j) in P_1_2]),
#          ([j for (i,j) in P_0_1], [j for (i,j) in P_1_2]),
#          c=[0.6,0.6,0.6], alpha = 0.5)


ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal', adjustable='box')
ax.set_axis_off()
st.pyplot(fig)