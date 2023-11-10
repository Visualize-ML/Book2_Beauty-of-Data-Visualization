import matplotlib.pyplot as plt
from numpy.random import multivariate_normal as multi_norm
import numpy as np
from matplotlib.patches import Rectangle
from scipy.stats import multivariate_normal
import streamlit as st


# np.random.seed(2)
mu_X = 0
mu_Y = 0
MU = [mu_X, mu_Y]
# sigma_X = 1
# sigma_Y = 1
num = 400
X_grid = np.linspace(-3,3,200)
Y_grid = np.linspace(-3,3,200)

XX, YY = np.meshgrid(X_grid, Y_grid)

XXYY = np.dstack((XX, YY))

with st.sidebar:
    st.title('二元高斯分布')
    sigma_X = st.slider('X标准差', 0.5, 2.0, 1.0, 0.1)
    sigma_Y = st.slider('Y标准差', 0.5, 2.0, 1.0, 0.1)
    rho = st.slider('相关性系数', -0.99, 0.99, 0.0, 0.01)

fig = plt.figure(figsize = (6,6))


SIGMA = [[sigma_X**2, sigma_X*sigma_Y*rho], 
         [sigma_X*sigma_Y*rho, sigma_Y**2]] 
bi_norm = multivariate_normal(MU, SIGMA)
pdf_fine = bi_norm.pdf(XXYY)
X, Y = multi_norm(MU, SIGMA, num).T
center_X = np.mean(X)
center_Y = np.mean(Y)

ax = plt.subplot(111)
# plot center of data
plt.plot(X,Y,'.', color = '#223C6C', 
         alpha = 1, markersize = 5)

levels = np.linspace(-pdf_fine.max() * 0.2, pdf_fine.max() * 1.1, 20)
ax.contourf(XX,YY,pdf_fine,levels = levels,
           cmap = 'RdYlBu_r')
ax.contour(XX,YY,pdf_fine,levels = levels,
           colors = 'w')
ax.axvline(x = 0, color = 'k', linestyle = '--')
ax.axhline(y = 0, color = 'k', linestyle = '--')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_xlim((-3,3))
ax.set_ylim((-3,3))

ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])

ax.set_yticks([])
ax.set_xticks([])
ax.axis('off')

st.pyplot(fig)