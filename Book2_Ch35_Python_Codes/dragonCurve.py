"""
Dragon curve
https://en.wikipedia.org/wiki/Dragon_curve
"""
import sys
from math import sqrt, cos, sin, pi
import numpy as np
import random
import matplotlib.pyplot as plt


def f1(x, y):
    return (1 / sqrt(2)) * np.array(
        [[cos(pi/4), -sin(pi/4)], [sin(pi/4), cos(pi/4)]]).dot(
            np.array([x, y]))


def f2(x, y):
    return (1 / sqrt(2)) * np.array(
        [[cos(3*pi/4), -sin(3*pi/4)], [sin(3*pi/4), cos(3*pi/4)]]).dot(
            np.array([x, y])) + np.array([1, 0])



def dragon_curve(n):
    x, y = [0], [0]
    for _ in range(n):
        r = random.random()
        if r <= 0.5:
            dot = f1(x[-1], y[-1])
        else:
            dot = f2(x[-1], y[-1])
        x.append(dot[0])
        y.append(dot[1])
        
    return x, y


fig = plt.figure(figsize = (5,8))

for idx in range(6):

    ax = plt.subplot(3,2,idx + 1)
    x,y = dragon_curve(2**(idx + 6))
    
    ax.plot(x, y, '.', markersize=2, color='g')
    ax.set_axis_off()
    
    