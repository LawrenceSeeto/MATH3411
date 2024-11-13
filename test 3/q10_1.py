import sympy as sp

# Define the variable a
a = sp.symbols('a')

# Define the matrix A
A = sp.Matrix([[a**3, a**2],
               [a**6, a**7]])

# Define the vector B
B = sp.Matrix([a**2, a**4])

# Solve the equation AX = B for X
X = A.LUsolve(B)

# Extract x and y from the solution vector X
x, y = X

print("Solution vector X:", X)
print("x:", x)
print("y:", y)

# Expected solution
expected_x = a**3
expected_y = a**4
print("Expected x:", expected_x)
print("Expected y:", expected_y)