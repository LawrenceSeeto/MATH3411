def euler_totient(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if (exp % 2) == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

# Calculate φ(55)
n = 55
phi_n = euler_totient(n)
print(f"φ({n}) = {phi_n}")

# Calculate 2^55 mod 55
base = 2
exp = 55
mod = 55
result = mod_exp(base, exp, mod)
print(f"{base}^{exp} mod {mod} = {result}")