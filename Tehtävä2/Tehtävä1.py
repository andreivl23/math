from matplotlib import pyplot as plt, patches
import numpy as np
from fractions import Fraction as fr

import matplotlib as mpl

fig = plt.figure()
ax = fig.subplots()

ymp = patches.Circle((0, 0), radius=1, fill=0)
ax.add_patch(ymp)

# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis('equal')

plt.xticks([-1, 0, 1], minor=True)
plt.yticks([-1, 0, 1])

pist=np.array([np.pi/6, np.pi/4, np.pi/3, np.pi/2,2*np.pi/3,5*np.pi/6,np.pi,3*np.pi/2])
varit=np.array(['red', 'green', 'blue','yellow','orange','violet','cyan','pink'])

y = np.sin(pist)
x = np.cos(pist)
for i in pist:
    plt.scatter(x,y, color=varit, marker='X')

plt.annotate(r'$(\frac{\pi}{4})$',
            xy=(np.cos(np.pi/4), np.sin(np.pi/4)), xycoords='data',
            xytext=(+30, +0), textcoords='offset points', fontsize=12,
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))
plt.annotate(r'$(\frac{\pi}{3})$',
            xy=(np.cos(np.pi/3), np.sin(np.pi/3)), xycoords='data',
            xytext=(+30, +5), textcoords='offset points', fontsize=12,
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))
plt.annotate(r'$(\frac{\pi}{2})$',
            xy=(np.cos(np.pi/2), np.sin(np.pi/2)), xycoords='data',
            xytext=(+10, +30), textcoords='offset points', fontsize=12,
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))
plt.annotate(r'$(\frac{2\pi}{3})$',
            xy=(np.cos(2*np.pi/3), np.sin(2*np.pi/3)), xycoords='data',
            xytext=(+0, +30), textcoords='offset points', fontsize=12,
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))
plt.annotate(r'$(\frac{5\pi}{6})$',
            xy=(np.cos(5*np.pi/6), np.sin(5*np.pi/6)), xycoords='data',
            xytext=(-20, +30), textcoords='offset points', fontsize=12,
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))
plt.annotate(r'$({\pi})$',
            xy=(np.cos(np.pi), np.sin(np.pi)), xycoords='data',
            xytext=(-40, +10), textcoords='offset points', fontsize=12,
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))
plt.annotate(r'$(\frac{3\pi}{2})$',
            xy=(np.cos(3*np.pi/2), np.sin(3*np.pi/2)), xycoords='data',
            xytext=(+30, -20), textcoords='offset points', fontsize=12,
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))
plt.annotate(r'$(\frac{\pi}{6})$',
            xy=(np.cos(np.pi/6), np.sin(np.pi/6)), xycoords='data',
            xytext=(+30, +0), textcoords='offset points', fontsize=12,
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))



plt.show()