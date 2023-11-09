import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-3*np.pi, 3*np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.figure().set_figwidth(19.2)
plt.plot(X,C, color="green", linewidth=3.5)
plt.plot(X,S, color="red", linewidth=3.5)

plt.text(0, 1.3, 'Lisää myöskin kuvaan selite.' , fontsize=20, color='black', ha='center', va='top')

plt.show()