"""
Sierpinsky triangle version 1
https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle
"""
import sys
from math import sqrt
import matplotlib.pyplot as plt


def sierpinskyTriangle(n, x, y, c):
    if n != 0:
        xA, yA = x, y
        xB, yB = x + c, y
        xC, yC = x + c / 2, y + c * sqrt(3)/2
        xE, yE = (xA + xB) / 2, (yA + yB) / 2
        xF, yF = (xB + xC) / 2, (yB + yC) / 2
        xG, yG = (xA + xC) / 2, (yA + yC) / 2
        # Central triangle
        plt.fill([xE, xF, xG], [yE, yF, yG], 'w')
        # Small triangles
        sierpinskyTriangle(n - 1, x, y, c / 2)
        sierpinskyTriangle(n - 1, xG, yG, c / 2)
        sierpinskyTriangle(n - 1, xE, yE, c/2)
    else:
        plt.fill([x, x + c, x + c / 2], [y, y, y + c * sqrt(3) / 2], 'b')



fig = plt.figure(figsize = (5,8))

for idx in range(6):

    ax = plt.subplot(3,2,idx + 1)
    sierpinskyTriangle(idx, 0, 0, 10)
    
    ax.set_axis_off()
