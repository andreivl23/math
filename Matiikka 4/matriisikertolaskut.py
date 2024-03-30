from sympy import Matrix, symbols, init_printing, pprint

init_printing(use_unicode=True)

# 1 a)
A = (Matrix([[-1, 2], [3, 1]]))
B = (Matrix([[0, 1, 3], [2, -3, 5]]))
pprint(A * B)

# 1 b)
A = (Matrix([[1, 3, 5], [0, -2, 1], [2, -1, 4]]))
B = (Matrix([[1], [-3], [-1]]))
pprint(A * B)

# 1 c)
A = (Matrix([[2, 0, 1], [1, -3, 4], [0, 1, 5]]))
B = (Matrix([[3], [-5], [7]]))
pprint(A * B)

# 1 d)
A = (Matrix([[1, -4, 2], [3, 0, -2], [2, 1, 0]]))
B = (Matrix([[5, 1, -1], [-2, 1, 3], [0, 3, 4]]))
pprint(A * B)

M = (Matrix([[4, 9, 0], [-3, 7, -11]]))
pprint(M.T)

M = (Matrix([[8, 9], [-3, 12], [0, -1], [7, 1]]))
pprint(M.T)

M = (Matrix([[5, -6], [8, 10]]))
pprint(M.det())
x = symbols('x')
M = (Matrix([[1 - x, -x], [x, 1 - x]]))
pprint(M.det())
M = (Matrix([[2, 3, 4], [-2, -1, 1], [5, 3, 2]]))
pprint(M.det())
M = (Matrix([[3, 15, 7], [0, -4, 0], [3, 2, 3]]))
pprint(M.det())
M = (Matrix([[-2, 0, 8, 5], [3, -1, 2, 1], [4, 7, 6, 2], [1, 0, 2, 3]]))
pprint(M.det())
