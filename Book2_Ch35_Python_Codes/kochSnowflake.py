"""
Koch snowflake
https://en.wikipedia.org/wiki/Koch_snowflake
"""
import sys
from math import sqrt
import matplotlib.pyplot as plt


def kochCurve(n, xA, yA, xB, yB):
    if n != 0:
        xC = xA + (xB - xA) / 3
        yC = yA + (yB - yA) / 3
        xD = xA + 2 * (xB - xA) / 3
        yD = yA + 2 * (yB - yA) / 3
        xE = (xC + xD) / 2 - (yD - yC) * sqrt(3) / 2
        yE = (yC + yD) / 2 + (xD - xC) * sqrt(3) / 2
        kochCurve(n - 1, xA, yA, xC, yC)
        kochCurve(n - 1, xC, yC, xE, yE)
        kochCurve(n - 1, xE, yE, xD, yD)
        kochCurve(n - 1, xD, yD, xB, yB)
    else:
        plt.plot([xA, xB], [yA, yB], 'b')


def kockCurveConstruction(n):
    kochCurve(n, 0, 0, 1, 0)
    plt.axis("equal")
    plt.show()


def kochSnowflake(n):
    xA, yA = 0, 0
    xB, yB = 1 / 2, sqrt(0.75)
    xC, yC = 1, 0
    kochCurve(n, xA, yA, xB, yB)
    kochCurve(n, xB, yB, xC, yC)
    kochCurve(n, xC, yC, xA, yA)
    plt.axis("equal")
    plt.tight_layout()



fig = plt.figure(figsize = (5,8))

for idx in range(6):

    ax = plt.subplot(3,2,idx + 1)
    kochSnowflake(idx)
    
    ax.set_axis_off()
