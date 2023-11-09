import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-3*np.pi, 3*np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.figure().set_figwidth(19.2)
plt.plot(X,C, color="green", linewidth=3.5)
plt.plot(X,S, color="red", linewidth=3.5)

plt.text(0, 1.3, 'Lisää myöskin kuvaan selite.' , fontsize=20, color='black', ha='center', va='top')


plt.xticks([-3*np.pi,-5*np.pi/2,-2*np.pi,-3*np.pi/2,-np.pi, -np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi, 5*np.pi/2,3*np.pi],
       [r'$-3\pi$',r'$-5\pi/2$',r'$-2\pi$',r'$-3\pi/2$',r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$',r'$+3\pi/2$',r'$+2\pi$',r'$+5\pi/2$',r'$+3\pi$'])

plt.show()
