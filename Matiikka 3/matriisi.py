import numpy as np
import numpy.linalg as la
from sympy import symbols, solve

x, y, z = symbols('x, y, z')

print(solve([x + y + 3*z - 1,
       3*x + y + z + 5,
       2*x + y + 2*z + 2], [x, y, z]))





# A = np.array([[-1, 2], [3, -5]])
# B = np.array([[2, 0], [-1, 4]])

# print(2*A + 3*B)
# print(A - B)