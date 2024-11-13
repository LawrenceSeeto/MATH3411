from sympy import symbols, Poly, div

def power_in_field(coeffs, power, mod):
    x = symbols('x')
    poly = Poly(coeffs, x, domain=f'GF({mod})')
    a = symbols('a')
    
    # Find the polynomial relation a^2 + a + 2 = 0
    relation = Poly(coeffs, a, domain=f'GF({mod})')
    
    # Initialize a^power
    result = Poly(a**power, a, domain=f'GF({mod})')
    
    # Reduce result modulo the relation
    _, remainder = div(result, relation, domain=f'GF({mod})')
    
    return remainder

# Example usage:
# F=Z_3[x]/⟨x2+x+2⟩
# ⟨x2+x+2⟩ <- coefficents of x^2 + x + 2
coeffs = [1, 1, 2]  # Coefficients of x^2 + x + 2
# Express a^? as a linear combination of
# a^? <- ? = power
power = 7
# F=Z_3[x]/⟨x2+x+2⟩
# F=Z_3 <- 3 = mod
mod = 3

remainder = power_in_field(coeffs, power, mod)
print(f"a^{power} = {remainder}")