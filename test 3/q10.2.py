from sympy import symbols, Poly

def field_dimension(polynomial_str, field_base):
    x = symbols('x')
    polynomial = Poly(polynomial_str, x)
    degree = polynomial.degree()
    return degree

# Example usage
polynomial_str = 'x**4 + x**3 + 1'
field_base = 2  # For Z2
dimension = field_dimension(polynomial_str, field_base)
print(f"The dimension of the field F over Z{field_base} is: {dimension}")